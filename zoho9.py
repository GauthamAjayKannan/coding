 def rev(str,n):
        n-=1
        if n==0:
            return str[n]
        else:
            return str[n]+rev(str,n)
 t=input()
 print(rev(t,len(t)))
