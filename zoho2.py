 s='12345'
    r=[]
    i=0
    j=len(s)-1
    f=""
    while i<j:
        r.append(f+s[i]+" "*((j+1)-(i+2))+s[j]+f)
        i+=1
        j-=1
        f=" "*(i)
    r.append(f+s[i]+f)
    t,i=0,0
    while i<len(r):
        print(r[i])
        i+=1
    i-=2
    while i>=0:
        print(r[i])
        i-=1
