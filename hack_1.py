"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    _ls = []

    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)] #hace una lista dividiendo los caracteres de "s" en grupos de tres
                                        #secuencia de números que comienzan en 0, terminan antes de la longitud de result, y se incrementan de 3 en 3
    
    for txt in txt_ls: #para cada item en la lista de grupos de caracteres:
       if len(txt) % 2 != 0:  #si la cantidad de caracteres es impar
          content = f"{txt[0]}{txt[1].upper()}{txt[2]}"  #el del medio lo pone mayuscula
          _ls.append(content)
       else: #si es par
          _ls.append(txt)    #lo deja todo igual
    result = "".join(_ls)  #une todos los elementos de la lista _ls en una sola cadena, utilizando una cadena vacía ("") como separador
    return result

#prueba interna
print(fn_hack_1("fooziman"))