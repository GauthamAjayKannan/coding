    s1="test123string"
    s2="str"
    for i in range(len(s1)):
        r=0
        for j in range(len(s2)):
            if s1[i+j]==s2[j]:
                r=i
                s=True
            else:
                s=False
                break
        if s:
            print(r)
            break
    else:
        print(-1)
