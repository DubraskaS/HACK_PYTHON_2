"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    _ls = []
    abc = "abcdefghijklmnopqrstuvwz"
    n = len(result)
    if n % 2 != 0: #si es impar la longitud del input:
        while (n > 0):
            _ls.append(f"{abc[n-1]}"+"-"+f"{n}") 
            n -= 1
    else: #si es par:
        while(n > 0):
            _ls.append(f"{n}")
            n -= 1
    
    result = _ls
    return result

abc = "abcdefghijklmnopqrstuvwz"
print(fn_hack_8(["a","b","c","d","e"]))