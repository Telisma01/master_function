import random
import string
def alfanimerik():
    kod = []
    n = int(input("konbyn karakte ou vle nan kod la"))
    while n > 0:
        let_chif = string.ascii_letters+string.digits
        chwa = random.choice(let_chif)
        if chwa not in kod:
            kod.append(chwa)
            n -= 1
    return "".join(kod)

print("kod ki jenere pou ou a se : "+alfanimerik())
