import string

aksepte=string.ascii_letters+string.digits+"-"
fraz=input("entrer yn fraz")
for i in fraz:
    if i not in aksepte:
        fraz= fraz.replace(i,"-")
print("slug la se : ",fraz)


