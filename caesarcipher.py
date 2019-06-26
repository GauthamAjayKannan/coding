n=input("Enter the string:")
    k=int(input("Enter the key:"))
    r=""
    for i in n:
        if i.isalpha():
            t=ord(i)+k
            if (i.isupper() and t>90):
                while t>90:
                  t=64+(t-90)
            elif (i.islower() and t>122):
                while t>122:
                  t=96+(t-122)
        else:
            t=ord(i)
        r+=chr(t)
    print(r)
