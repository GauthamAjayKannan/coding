    s=input("Enter the sequence:")
    cn=[]
    r=""
    for i in s:
        if i.isalnum():
            cn.append(i)
    for i in s:
        if i.isalnum():
            r+=cn.pop()
        else:
            r+=i
    print(r)
