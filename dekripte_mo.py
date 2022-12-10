
def dekripte():
    alfabe= "abcdefghijklmnopqrstuvwxyz"
    tab=[]
    n = (input("entre sa ou vle dekripte a"))
    for i in n.split("-"):
            tab.append(alfabe[int(i)])
    return "".join(tab)

print(dekripte())

