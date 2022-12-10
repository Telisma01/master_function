def separe_mo():
    mot= input("entrer mot ou vle a : ")
    nouvo_mo = []
    for i in mot:
        nouvo_mo.append(i)
    return ",".join(nouvo_mo)
print("nouvo a se : ",separe_mo())



