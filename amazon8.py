    s='aba'
    i=0
    l=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
         t=s[i:j]
         print(t)
         if len(t)==1 or t[0]==t[len(t)-1]:
            l.append(t)
    print(l)
