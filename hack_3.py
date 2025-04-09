"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    dic = {"a" : "@",
           "e" : "3",
           "i" : "¡",
           "o" : "0",
           "u" : "v"}
    _ls = ""

    for n in result:
        if n in dic:
            _ls += dic[n]
        elif n == "m" or n=="z" or n=="r":
            _ls += n
        else:
            _ls += n.upper()
    
    result = _ls

    return result

#Prueba interna
print(fn_hack_3("fooziman"))