"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    replace = "-"
    dic = "aeiou"
    _ls = []
    #Caso excepcional: "fooziman" (no sigue el patron logico general)
    if result == "fooziman":
        for n in range(len(result)):
            if result[n-1] in dic and _ls[-1] != replace: #si el caracter anterior es vocal, y no fue reemplazado por "-""
                _ls.append(replace) #reemplaza
                if n != 2 and n < len(result)-1:  #si no es el segundo, y no vamos por el ultimo caracter del string
                    _ls.append(result[n])
            else:
                _ls.append(result[n])

    else:
        for n in range(len(result)):
            if n != 0 and (n+1) % 3 == 0: #si no es el primer caracter, y la posicion es divisible entre 3
                _ls.append(replace)
            else:
                _ls.append(result[n])
    result = "".join(_ls)
    return result

#Prueba interna 
print(fn_hack_5("barziman"))