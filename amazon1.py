totalspace=100
    arr=[10,20,30,40]
    r=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if abs(arr[i]+arr[j])>sum(r) and totalspace-abs(arr[i]+arr[j])==40:
                r=[arr[i],arr[j]]
    print(r)
