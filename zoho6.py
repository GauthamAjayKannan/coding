 def perfect(n):
        for i in range(1,n):
            if i*i==n:
                return True
        return False
    s=[10,36,54,89,12]
    r=[]
    for i in s:
        tot=0
        if i%4==0 and i%6==0:
            tot+=4
        if perfect(i):
            tot+=5
        if i%2==0:
            tot+=3
        r.append([i,tot])
    for i in range(len(r)):
        for j in range(i+1,len(r)):
            if r[i][1]>r[j][1]:
                r[i],r[j]=r[j],r[i]
    print(r)
