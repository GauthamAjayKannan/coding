    n=int(input("Enter the no. of lines(odd numbers)"))
    mid=n//2
    res=[]
    print(mid)
    i=1
    while i<=n:
        res.append(" "*mid+"*"*i+" "*mid)
        i+=2
        mid-=1
    for i in res:
        print(i)
    if n%2:
        res=res[:len(res)-1]
    res=res[::-1]
    for i in res:
        print(i)
