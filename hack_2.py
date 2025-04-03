"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    _ls = ""
    vocales = "aeiou"  #string de vocales
    for n in result:
        if n not in vocales: #compara con el string para identificar las vocales del input
            _ls += n
    result = _ls

    return result

#prueba interna
print(fn_hack_2("fooziman"))