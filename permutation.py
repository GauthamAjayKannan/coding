def permutation(a,num):
    t=[]
    for i in range(len(num)+1):
        t.append("".join(num[:i]+[a]+num[i:]))
    return t
l=['3456789']
for j in l:
  st=list(j)
  for i in range(len(st)):
    r=permutation(st[i],st[:i]+st[i+1:])
    for i in r:
        if i not in l:
            l.append(i)
print(l,len(l))
