from anyerplint.ast import Expression, FuncCall
from anyerplint.tnex import ParseError, parse


def removequote(s: str) -> str:
    return s.removeprefix('"').removesuffix('"')


def translate_str(s: str) -> str | list[str]:
    parsed = parse(s)
    translator = Translator()
    result = translator.translate(parsed)
    errors = translator.errors
    return errors if errors else result


# these will be converted to uppercase variants. Eventually this should be empty but needs fixing a lot of templates

allow_wrong_case = {
    "F,Calc",
    "F,Combine",
    "F,Eval",
    "F,IsChanged",
    "F,Not",
    "F,SetData",
    "F,ToDate",
}

# some 'trivial' translations
nullary_funcs = {
    "F,GUID",
    "F,NOW",
}
# these will be translated to name(arg1; arg2)
# xxx remove the mixed case variants
nnary_funcs: dict[str, int | tuple[int, int]] = {
    "F,ADDXMLNS": 4,
    "F,CSV": (2, 3),
    "F,DATEADD": 3,
    "F,DATEDIFF": 3,
    "F,DBSELECT": (2, 999),
    "F,FLOOR": 1,
    "F,ISCHANGED": 2,
    "F,ISDATE": (1, 2),
    "F,ISNOTHING": 1,
    "F,ISNUMERIC": 1,
    "F,LPAD": 3,
    "F,PARSE": 1,
    "F,RANGE": 4,
    "F,ROUND": (2, 3),
    "F,RPAD": 3,
    "F,SAPSELECT": 6,
    "F,SAPSELECTWS": 8,
    "F,XMLENCODE": 1,
}


class Translator:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def translate(self, tree: Expression) -> str:
        """Convert to pretty mostly-infix notation."""
        # only function calls are translated
        if not isinstance(tree, FuncCall):
            return str(tree)

        translate = self.translate
        if tree.name in allow_wrong_case:
            tree.name = tree.name.upper()
        match (tree.name, tree.args):
            case "F,EVAL", [obj, operation, comp, iftrue, iffalse]:
                return f"({translate(obj)} {removequote(translate(operation))} {translate(comp)} ? {translate(iftrue)} : {translate(iffalse)})"
            case "F,EXISTS", ["v", key]:
                return f"defined({key})"
            case "F,EXISTS", [obj, key]:
                return f"({key} in {translate(obj)})"
            case "F,EXISTS", [obj]:
                return f"(exists {translate(obj)})"

            case "F,REPLACE", [src, frome, toe]:
                return (
                    f"{translate(src)}.replace({translate(frome)} -> {translate(toe)})"
                )
            case "F,LOWER", [exp]:
                return f"{translate(exp)}.lower()"
            case "F,UPPER", [exp]:
                return f"{translate(exp)}.upper()"
            case "F,TRIM", [exp]:
                return f"{translate(exp)}.trim()"
            case "F,LTRIM", [exp]:
                return f"{translate(exp)}.ltrim()"
            case "F,RTRIM", [exp]:
                return f"{translate(exp)}.rtrim()"

            case "F,NVL", [exp, default]:
                return "(" + translate(exp) + " ?? " + translate(default) + ")"

            case "F,TONUMBER", [exp, '"."']:
                return f"num({translate(exp)})"
            case "F,TONUMBER", [exp, sep]:
                return f"num({translate(exp)} - {translate(sep)})"
            case "F,TOCHAR", [exp, str(format)]:
                return f"num({translate(exp)}.tochar({format})"
            case "F,TOCHAR", [exp, str(format), str(culture)]:
                return f"num({translate(exp)}.tochar({format}, {culture})"
            case "F,FORMAT", [exp, format]:
                return f"{translate(exp)}.format({translate(format)})"
            case "F,COMBINE", parts:
                translated = [translate(part) for part in parts]
                return "(" + " & ".join(translated) + ")"
            case "F,GETDATA", [ds, key]:
                return f"{translate(ds)}[{translate(key)}]"
            case "F,GETNODE", [src, path]:
                return f"{translate(src)}.node({translate(path)})"
            case "F,SETDATA", [ds, key, value]:
                return f"{translate(ds)}[{translate(key)}] := {translate(value)}"
            case "F,IF", [src, op, tgt]:
                return (
                    f"if {translate(src)} {removequote(translate(op))} {translate(tgt)}"
                )
            case "F,LEN", [o]:
                return f"len({translate(o)})"
            case "F,CALC", parts:
                return "(" + " ".join(translate(part) for part in parts) + ")"
            case "F,NOT", [exp]:
                return "not " + translate(exp)
            case "F,AND", conds:
                translated = [translate(part) for part in conds]
                return "(" + " && ".join(translated) + ")"
            case "F,OR", [*conds]:
                translated = [translate(part) for part in conds]
                return "(" + " || ".join(translated) + ")"
            case "F,ROWCOUNT", [o]:
                return f"{translate(o)}.rowcount()"
            case "F,TODATE", [d, str(format)]:
                return f"{translate(d)}.todate({format})"
            case "F,CHR", [str(code)] if code.isdigit():
                return f"char '{chr(int(code))}' {code}"
            case "F,CURSORINDEX", [str(src)]:
                return f"{src}.cursorindex()"
            case "F,SUBSTR", [exp, beg, count]:
                return f"{translate(exp)}.substr({translate(beg)}, {translate(count)})"
            case "F,INSTR", [haystack, needle, then, else_]:
                return f"{translate(needle)} in_string {translate(haystack)} ? {translate(then)} : {translate(else_)}"
            case "F,RIGHT", [exp, count]:
                return f"{translate(exp)}[-{translate(count)}:]"
            case "F,LEFT", [exp, count]:
                return f"{translate(exp)}[:{translate(count)}]"
            case "F,REGEXP_STRING", [s, pat]:
                return f"{translate(s)}.re_search({translate(pat)})"
            case "F,REGEXP_POSITION", [s, pat]:
                return f"{translate(s)}.re_search_pos({translate(pat)})"

            case str(func), [] if func in nullary_funcs:
                return f"{func.removeprefix('F,')}()".lower()

            case str(func), [param] if func.startswith(","):
                return f"{translate(param)}.pipe({func})"
            case str(func), args if func in nnary_funcs:
                match nnary_funcs[func]:
                    case int(n):
                        arity = (n, n)
                    case (int(begg), int(endd)):
                        arity = (begg, endd)

                if not arity[0] <= len(args) <= arity[1]:
                    self.errors.append(
                        f"Invalid number of arguments for {func} - got {len(args)}, expected {nnary_funcs[func]}"
                    )
                name = f"{func.removeprefix('F,')}".lower()
                joined = "; ".join(translate(part) for part in args)
                return f"{name}({joined})"

            case str(func), args:
                newname = func.removeprefix("F,")
                self.errors.append(f"Unknown function {func} ({len(args)} arguments)")
                return f"~(~{newname}(" + ";".join(translate(r) for r in args) + ")~)~"

        s = f"Unmatched pattern {tree}"
        raise ParseError(s)
