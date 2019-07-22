    s=input("Enter the string:")
    vow=[]
    vowel=['a','e','i','o','u']
    r=""
    for i in s:
        if i in vowel:
            vow.append(i)
    for i in s:
        if i in vowel:
            r+=vow.pop()
        else:
            r+=i
    print(r)
