    a1=[2,4,5,6,7,9,10,13]
    a2=[2,3,4,5,6,7,8,9,11,15]
    r=[]
    i,j=0,0
    while i<len(a1) and j<len(a2):
        if a1[i]==a2[j] and a1[i] not in r:
            r.append(a1[i])
        else:
            if a2[j] not in r:
              r.append(a2[j])
            if a1[i] not in r:
              r.append(a1[i])
        i+=1
        j+=1
    while i<len(a1):
        if a1[i] not in r:
         r.append(a1[i])
        i+=1
    while j<len(a2):
        if a2[j] not in r:
         r.append(a2[j])
        j+=1
    for i in range(len(r)-1):
        for j in range(i+1,len(r)):
            if r[i]>r[j]:
                r[i],r[j]=r[j],r[i]
    print(r)
