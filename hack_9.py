"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""
#FOR

def fn_hack_9(s):
    result = s
    dic = {}
    for key, val in result.items(): #por cada key y valor en los elementos del diccionario de entrada:
        if key == "foo":
            key = key.capitalize() #Pone en mayuscula la primera letra
            val = "Fooziman"
            dic.update({key: val}) #agrega a dic
        else:
            pass #no hace nada, para omitir barziman

    result = dic
    return result

#Practica interna
print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))