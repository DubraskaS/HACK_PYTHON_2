"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    dic = {"f",
           "n",
           "b"}
    _ls = ""
    for n in result:
        if n not in dic:
            _ls += n
    
    result = _ls

    return result

#Prueba interna
print(fn_hack_4("fooziman"))