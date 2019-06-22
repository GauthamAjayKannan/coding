map={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w'
    ,24:'x',25:'y',26:'z'}
    n=input('Enter a number')
    s=1
    res=[]
    while s<=len(n):
        k=True
        e=s
        r=""
        u=0
        for i in range(1,len(n)+1):
            if int(n[u:e]) in map:
                print("int",n[u:e])
                r+=map[int(n[u:e])]
                u=e
                e=e+s
                if u>=len(n):
                    break
            else:
                k=False
        if k:
            res.append(r)
        s+=1
    print(res)
