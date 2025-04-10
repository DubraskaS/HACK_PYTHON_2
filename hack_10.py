"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    abc = "abcdefghijklmnopqrstuvwxyz"
    _ls = []
    for n in result: #pasa por cada elemento de la lista input
        if isinstance(n, dict): #chequea si es un diccionario o un conjunto. Si es un diccionario:
            for key,val in n.items():
                if key in abc:
                    key = abc.index(key) + 1  #añade el indice de la letra en el string abc para reemplazarla
                if val in abc:
                    val = abc.index(val) + 1  #añade el indice de la letra en el string abc para reemplazarla
                _ls.append({f"{key}": f"{val}"}) #anade como diccionario de strings en lista 
        else:
            conj = set() #Creando un conjunto vacio
            for item in n:
                if item in abc:
                    conj.add(f"{abc.index(item) + 1}")  #añade el indice de la letra en el string abc como elemento de conjunto
            _ls.append(conj) #añade como conjunto a la lista

    result = _ls
    return result

#Practica interna
print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))