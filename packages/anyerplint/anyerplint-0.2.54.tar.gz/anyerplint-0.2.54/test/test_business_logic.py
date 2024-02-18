from pathlib import Path

import pytest
from anyerplint import business_logic

root = Path(__file__).absolute().parent


def test_brace_check() -> None:
    tested = business_logic.brace_check("(({[]}))")
    assert tested == []
    tested = business_logic.brace_check("[")
    [err] = tested
    assert err.startswith("File ended with mismatched braces")


def test_check_minimal_without_lib() -> None:
    minimal_script = root / "minimal_script.xml"
    res = business_logic.do_check(
        [], [str(minimal_script)], teaching=False, nostdlib=True
    )
    expected = {
        str(minimal_script): {
            "Unknown tags": [
                "<erpConnector>",
                "<error>",
                "<section name>",
                "<sections>",
            ],
            "Other errors": [
                "File ended with mismatched braces, remaining in stack (char, linenum): ( 5",
            ],
        },
    }
    assert res == expected


def test_check_malformed() -> None:
    malformed_file = root / "malformed.xml"
    res = business_logic.do_check(
        [], [str(malformed_file)], teaching=False, nostdlib=True
    )
    expected = {
        str(
            malformed_file,
        ): "FATAL, not well-formed (invalid token): line 4, column 19",
    }
    assert res == expected


@pytest.mark.skip()
def test_check_expression_like_regexes() -> None:
    input_file = root / "regexes.xml"
    res = business_logic.do_check([], [str(input_file)], teaching=False, nostdlib=True)
    expected = {
        "Unknown tags": [
            "<erpConnector>",
            "<section name>",
            "<sections>",
            "<variable name>",
        ],
    }

    errs = res.get(str(input_file), {})
    assert isinstance(errs, dict)
    assert not errs.get("Other errors")
    assert errs == expected


def test_check_expressions() -> None:
    input_file = root / "expressions.xml"
    res = business_logic.do_check([], [str(input_file)], teaching=False, nostdlib=True)
    expected = {
        "Unknown functions": [
            "F,NOW - line 4",
        ],
        "Unknown tags": [
            "<erpConnector>",
            "<section name>",
            "<sections>",
            "<variable name>",
        ],
        "Expression errors": [
            {
                "Error": "Line 5, expression contains no comma: {nocomma}",
                "Simple": "N/A",
                "Msg": [],
            }
        ],
    }

    errs = res.get(str(input_file), {})
    assert isinstance(errs, dict)
    assert not errs.get("Other errors")
    assert errs == expected
