import argparse
import contextlib
import sys

from rich.console import Console

from anyerplint.ast import Expression, FuncCall
from anyerplint.preprocessor import PreprocessError, get_expressions
from anyerplint.tnex import ParseError, parse
from anyerplint.translate import Translator
from anyerplint.util import glob_plus, open_text_file

console = Console(highlight=False)


def emit(s: str) -> None:
    console.print(s)


def color(text: str, color: str) -> str:
    return f"[{color}]{text}[/{color}]"


def print_recursive_lists(tree: Expression, indent: int) -> None:
    if isinstance(tree, FuncCall):
        emit("  " * indent + color(tree.name, "deep_sky_blue1"))
        for arg in tree.args:
            print_recursive_lists(arg, indent + 1)
    else:
        el = tree
        if el.startswith('"') and el.endswith('"'):
            col = "dark_orange"
        elif el.lower().startswith("v,"):
            col = "bright_green"
        elif el.isdecimal():
            col = "bright_yellow"
        else:
            col = None

        t = color(el, col) if col else el
        emit("  " * indent + t)


def color_translation_errors(expr: str) -> str:
    return expr.replace("~(~", "[red]").replace("~)~", "[/red]")


def search_calls(ast: FuncCall, func_name: str) -> list[FuncCall]:
    res = []
    func = func_name.upper()

    if ast.name.upper() == func:
        res.append(ast)

    for arg in ast.args:
        if isinstance(arg, str):
            continue
        child_results = search_calls(arg, func_name=func_name)
        res.extend(child_results)

    return res


def pretty_flat_call(ast: FuncCall) -> str:
    ret = ast.name

    pretty_args = []
    for arg in ast.args:
        match arg:
            case str(a):
                pretty_args.append(repr(a))
            case FuncCall(name, args):
                pretty_args.append(f"{name}({len(args)})")

    return " ; ".join([ret, *pretty_args])


def search_and_print_calls(fname: str, func_name: str) -> None:
    cont = open_text_file(fname).read()
    exps = get_expressions(cont)
    for exp in exps:
        parsed = parse(exp[0])
        if not isinstance(parsed, FuncCall):
            continue
        hits = search_calls(parsed, func_name=func_name)
        for hit in hits:
            printed = pretty_flat_call(hit)
            with contextlib.suppress(UnicodeEncodeError):
                print(str(fname) + " ; " + printed)


def print_formatted_expression(
    exp: str, linenum: int, errors_only: bool, log_all: bool
) -> None:
    try:
        parsed = parse(exp)

        translator = Translator()
        translated = translator.translate(parsed)
    except (ValueError, ParseError) as e:
        emit(f"[red]Failed to parse[/]: {exp} ({e})")
        return

    if errors_only and not translator.errors:
        return

    non_trivial_expr = translated != exp
    if non_trivial_expr or log_all:
        emit(f"L[yellow]{linenum}[/]\t[grey66]{exp}[/]")
    if non_trivial_expr:
        emit("=>\t" + color_translation_errors(translated))
        expr = parsed
        if not isinstance(expr, FuncCall):
            return
        print_recursive_lists(expr, 1)
        emit("")


def print_all_expressions(cont: str, errors_only: bool, log_all: bool) -> None:
    try:
        expressions = get_expressions(cont)
    except PreprocessError as e:
        emit(f"[red]{e}[/red]")
    else:
        for exp, linenum in expressions:
            print_formatted_expression(exp, linenum, errors_only, log_all)


def handle_parse(args: argparse.Namespace) -> None:
    errors_only = args.errors
    console.no_color = args.no_color
    if args.fun:
        if not args.filename:
            print(
                "With 'parse --fun' mode, you must specify file or directory to check"
            )
            return
        for pat in args.filename:
            fnames = glob_plus(pat)
            for f in fnames:
                with contextlib.suppress(
                    PreprocessError, ParseError, UnicodeDecodeError, PermissionError
                ):
                    search_and_print_calls(str(f), args.fun)

        return

    if not args.filename:
        console.rule("stdin")
        cont = sys.stdin.read()
        print_all_expressions(cont, errors_only, log_all=True)

    for pat in args.filename:
        fnames = glob_plus(pat)
        for f in fnames:
            console.rule(str(f))
            cont = open_text_file(f).read()
            print_all_expressions(cont, errors_only, log_all=False)


def init_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Declare arguments you need here."""
    parser.add_argument("filename", nargs="*", help="Files to parse")
    parser.add_argument(
        "--errors", action="store_true", help="Print only expressions with errors"
    )
    parser.add_argument("--fun", help="Only print certain functions, e.g. --fun F,EVAL")
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="No colors, good for redirecting to file",
    )
    parser.set_defaults(func=handle_parse)
    return parser
