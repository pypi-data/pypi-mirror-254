from anyerplint.translate import translate_str


def test_translate_syntax() -> None:
    assert (
        translate_str(
            'F,EVAL(obj.A,AssetCode;=;"";F,EVAL(obj.A,SUM;"&gt;";"0";40;50);F,EVAL(obj.A,SUM;"&gt;";"0";70;75))'
        )
        == '(obj.A,AssetCode = "" ? (obj.A,SUM > "0" ? 40 : 50) : (obj.A,SUM > "0" ? 70 : 75))'
    )

    assert (
        translate_str(
            "F,EVAL(F,EXISTS(v;config);=;1;F,REPLACE(F,LOWER(v,config);rootconfig;systemvars);&quot;&quot;)"
        )
        == '(defined(config) = 1 ? v,config.lower().replace(rootconfig -> systemvars) : "")'
    )
