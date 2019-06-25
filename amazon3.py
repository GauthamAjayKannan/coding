 n=int(input("Enter the number of elements:"))
    a=[int(input()) for i in range(n)]
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            t=abs(a[i]-a[j])
            if res<t:
                res=t
    print(res)
