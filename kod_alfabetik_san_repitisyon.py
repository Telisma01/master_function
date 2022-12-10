import random
import string

'''def kod_alfabetik(n):
    kod=[]
    while n > 0:
        let = ["a","b","c","d","e","f","g","h","h","c"]
        for i in let:
            if i not in kod:
                kod.append((i))
            n -= 1
    return "".join(kod)
print("votre mot de passe est :",kod_alfabetik(26))'''

def kod_alfabetik(n=int(input("konbyn let ou vle nan kod ou a"))):
    kod=[]
    while n > 0:
        let = string.ascii_letters
        nb = random.choice(let)
        if nb not in kod:
            kod.append((nb))
            n -= 1
    return "".join(kod)
print("kod ki jenere pou ou an c :",kod_alfabetik())


