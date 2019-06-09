 s=input()
    i=0
    t=""
    r=""
    while i<len(s):
        n=""
        if s[i].isalpha():
            t=s[i]
            i+=1
        elif s[i].isnumeric():
            while i<len(s) and s[i].isnumeric():
                n+=s[i]
                print(n)
                i+=1
            r+=t*int(n)
    print(r)
