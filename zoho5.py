    s=[["luke","shaw"],["wayne","rooney"],["rooney","ronaldo"],["shaw","rooney"]]
    g="ronaldo"
    coun=0
    for i in range(len(s)):
        if s[i][1]==g:
            g=s[i][0]
            break
    for i in range(len(s)):
        if s[i][1]==g:
            coun+=1
    print(coun)
