import string
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def kripte_mo():
    m = input("antre mo ou a :")
    mo = []
    for i in m:
        mo.append(str(string.ascii_lowercase.index(i)))
    return "-".join(mo)


