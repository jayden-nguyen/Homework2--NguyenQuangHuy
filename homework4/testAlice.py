

inp = open("alicefiles.txt","r")
text = inp.read()
inp.close()
text=text.lower()
text=text.replace("#"," ")
text=text.replace("$"," ")
text=text.replace("("," ")
text=text.replace(")"," ")
text=text.replace("'s"," ")
text=text.replace(";"," ")
text=text.replace("1"," ")
text=text.replace("2"," ")
text=text.replace("3"," ")
text=text.replace("4"," ")
text=text.replace("5"," ")
text=text.replace("6"," ")
text=text.replace("7"," ")
text=text.replace("8"," ")
text=text.replace("9"," ")
text=text.replace("."," ")
text=text.replace("*"," ")
text=text.replace("0"," ")
text=text.replace("’"," ")
text=text.replace(","," ")
text=text.replace("["," ")
text=text.replace("]"," ")
text=text.replace("'"," ")
text=text.replace("_"," ")
text=text.replace("%"," ")
text=text.replace("!"," ")
text=text.replace("-"," ")
text=text.replace(":"," ")
text=text.replace("?"," ")
text=text.replace("”"," ")
text=text.replace("/"," ")
st = text.split()
main = {}
def check_app(st):
    li = []
    for lo in st:
        if lo in li:
            continue
        else:
            li.append(lo)
    for i in range(len(li)):
        n = 0
        for j in range(len(st)):
            if li[i] == st[j]:
                n += 1
            else:
                continue
        main[li[i]] = n
    return main
main = check_app(st)
li_key = sorted(main)
li_val = []
for i in range(len(li_key)):
    li_val.append(main[li_key[i]])
out = open("alicesuper.txt","w")
out.write("Word            "+"Count"+"\n")
out.write("=====================\n")
for i in range(len(li_key)):
    out.write("%-16s%-5s"%(li_key[i],li_val[i])+"\n")
out.close()
def checkword(word):
    for i in range(len(li_key)):
        if word == li_key[i]:
            print(word,"     ",li_val[i])
        else:
            continue
        
checkword("alice")
