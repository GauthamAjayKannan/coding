   n=int(input())
    res=[]
    mid=n//2
    print(mid)
    f,b=mid,mid
    t=""
    while f>=0 and b<=n-1:
     t=""
     for i in range(n):
        if i==f or i==b:
            t+='*'
        else:
            t+=" "
     res.append(t)
     f-=1
     b+=1
    print(res)
    for i in res:
        print(i)
    res=res[::-1]
    if n%2:
        res=res[1:]
    for i in res:
        print(i)
