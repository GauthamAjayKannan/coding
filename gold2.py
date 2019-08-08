    s=input()
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            print(s[i])
            break
    else:
        print(-1)
