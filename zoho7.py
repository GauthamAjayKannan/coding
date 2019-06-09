    s=map(int,input().split(" "))
    r=[]
    i,j=0,len(s)-1
    while i<=j:
        if i==j:
            r.append(s[i])
        else:
            r.append(s[j])
            r.append(s[i])
        i+=1
        j-=1
    print(r)
