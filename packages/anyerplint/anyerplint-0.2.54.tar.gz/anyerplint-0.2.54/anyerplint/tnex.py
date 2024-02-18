"""tnex - Trivial Nested EXpressions.

Easier to read/write than s-expr's I guess

"""
import re

from anyerplint import util
from anyerplint.ast import Expression, FuncCall


def tokenize(s: str) -> list[str]:
    # negative lookbehind for \ escaping, split to parts separated by ; ( ) "
    tokens = re.split(r"([\(\)\";])", s)
    return list(filter(None, tokens))


class ParseError(Exception):
    """Exceptions raised by parser."""


def _parse_string(toks: list[str]) -> tuple[str, int]:
    assert toks[0] == '"'
    # eat up tokens to produce just one str
    result = ['"']
    escape = False
    for tok in util.skip(toks, 1):
        result.append(tok)
        if tok.endswith("\\"):
            backslashes = util.count_trailing(tok, "\\")
            escape = (backslashes % 2) != 0
        elif tok == '"' and not escape:
            value = "".join(result)
            return value, len(result)
        else:
            escape = False

    msg = "Unterminated string"
    raise ParseError(msg)


def _parse_accessor(toks: list[str]) -> tuple[str, int]:
    if len(toks) > 1 and toks[1] == '"':
        s, moved = _parse_string(toks[1:])
        return toks[0] + s, moved + 1

    return toks[0], 1


def emit_nested_sequence(parts: list[str]) -> tuple[list[Expression], int]:
    res: list[Expression] = []
    i = 0
    while i < len(parts):
        it = parts[i]
        if it == '"':
            s, moved = _parse_string(parts[i:])
            res.append(s)
            i += moved
        elif it == ";":
            if i > 0 and parts[i - 1] == ";":
                res.append("")
            i += 1
        elif it == ")":
            i += 1
            break
        elif it == "(":
            nested, moved = emit_nested_sequence(parts[i + 1 :])
            func_name = parts[i - 1].strip()
            res = res[0:-1]
            func = FuncCall(name=func_name, args=nested)
            res.append(func)
            i += moved
        elif it.startswith(","):
            # actually call previous output with "nesting" output
            try:
                previous = res.pop()
            except IndexError as exc:
                msg = f"',format' syntax called without preceding expression: '{it}'"
                raise ParseError(msg) from exc
            s, moved = _parse_accessor(parts[i:])

            # Not actually a function call
            fmt = FuncCall(s, [previous])
            res.append(fmt)
            i += moved

        # special foo,"hello" accessor that accesses property of foo.
        # lexer breaks it because of " char, so reassemble it here
        elif it.endswith(","):
            s, moved = _parse_accessor(parts[i:])
            res.append(s)
            i += moved
        else:
            res.append(it.strip())
            i += 1

    return (res, i + 1)


def parse(s: str, expand_entities: bool = True) -> Expression:
    if expand_entities:
        s = expand_xml_entities(s)
    tokens = tokenize(s)
    parsed, _ = emit_nested_sequence(tokens)
    if not parsed:
        msg = f"Empty parse result for expression: '{s}'"
        raise ParseError(msg)

    return parsed[0]


def expand_xml_entities(xml_string: str) -> str:
    entity_pattern = re.compile(r"&([^;]+);")

    def replace_entity(match: re.Match[str]) -> str:
        entity = match.group(1)
        if entity == "lt":
            return "<"
        elif entity == "gt":
            return ">"
        elif entity == "amp":
            return "&"
        elif entity == "quot":
            return '"'
        else:
            return match.group(0)

    return entity_pattern.sub(replace_entity, xml_string)
