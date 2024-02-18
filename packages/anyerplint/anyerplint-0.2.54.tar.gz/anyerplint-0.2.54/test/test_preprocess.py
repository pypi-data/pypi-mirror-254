from anyerplint.preprocessor import get_expressions

test_cont = r"""1 filler
2 lines
3 Hello, {v,fooo}
4 {oeoeoe}
5
6 Hello {v,foo("}}")}
7
8 More nesting {oeoe}
9 {"string"}
10 {"st with \" and other stuff"}
11 {
12 many
13 lines
14 }
"""


def test_preproc() -> None:
    expressions = get_expressions(test_cont)
    assert expressions == [
        ("v,fooo", 3),
        ("oeoeoe", 4),
        ('v,foo("}}")', 6),
        ("oeoe", 8),
        ('"string"', 9),
        ('"st with \\" and other stuff"', 10),
        ("\n12 many\n13 lines\n14 ", 11),
    ]
