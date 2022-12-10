
def inisyal():
    nom = input("mete nonw pou k baw inisyal ou : ")
    add = []
    inis = ""
    for i in nom:
        nom = nom.replace(" ", "-")
    for mo in nom.split("-"):
        add.append(mo)
    for k in add:
        inis += k[0].upper()
    print("inisyal ou a c :", inis)
inisyal()