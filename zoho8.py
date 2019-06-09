zeros=['zero','one','two','three','four','five','six','seven','eight','nine']
    ele=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',]
    tens=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    n=input("Enter the number(0-999)")
    if len(n)==1:
        print(zeros[int(n)])
    elif len(n)==2:
        if n[0]=='1':
            print(ele[int(n[1])])
        else:
            if n[1]=='0':
                print(tens[int(n[0])-2])
            else:
                print(tens[int(n[0])-2]+" "+zeros[int(n[1])])
    elif len(n)==3:
            if n[1:]=="00":
                print(zeros[int(n[0])]+" "+"hundred")
            elif n[1]=='0':
                print(zeros[int(n[0])]+" "+"hundred and"+" "+zeros[int(n[2])])
            elif n[1]=='1':
                print(zeros[int(n[0])]+" hundred and "+ele[int(n[2])])
            elif n[2]=='0':
                if n[1]=='1':
                    t=ele[0]
                else:
                    t=tens[int(n[1])-2]
                print(zeros[int(n[0])]+" hundred and "+t)
            else:
                print(zeros[int(n[0])]+" hundred and "+tens[int(n[1])-2]+" "+zeros[int(n[2])])
