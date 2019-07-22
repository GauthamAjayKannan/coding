    n=input()
    i=1
    sum=0
    while i<=5:
        sum=str(int(n)+int(n[::-1]))
        if sum==sum[::-1]:
            print(sum)
            break
        i+=1
        n=sum
    else:
        print(-1)
