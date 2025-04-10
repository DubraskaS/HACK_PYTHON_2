"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    dic = {"a": "1",
           "b": 2,
           "c": "3",
           "d": 4,
           "e": "5"}
    _ls = []
    for n in range(0,len(result)):
        if result[n] in dic:
            _ls.append(dic[result[n]]) #se aplica el diccionario
        else:
            _ls.append(result[n])  #se deja el mismo valor (caso 0)
    result = _ls

    return result

#Practica interna
print(fn_hack_7(["a","b","c","d","e"]))