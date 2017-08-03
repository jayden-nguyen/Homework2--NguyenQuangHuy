
def let_app(strg):
    st = list(strg.lower())
    st = [lo for lo in st if lo != " "]
    st.sort()
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
        print(li[i],'   ',n)
        
let_app("ThiS is String with Upper and lower case Letters")

