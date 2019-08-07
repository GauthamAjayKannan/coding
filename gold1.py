    s="aaaabbbccddddeeeee"
    r=""
    num=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            num+=1
        else:
            r+=s[i]+str(num)
            num=1
    r+=s[len(s)-1]+str(num)
    print(r)
