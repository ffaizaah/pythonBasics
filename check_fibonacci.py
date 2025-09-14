while(True):
    try:
        num=int(input("Enter the number to be checked: "))
        break
    except ValueError as e:
        print(e)
        print("Try Again")
        continue
k=num
t1,t2=0,1
tn,count=0,2
if num==t1:
    print(num, "occurs at position 1")
elif num==t2:
    print(num, "occurs at position 2")
else:
    while (t2+t1)<=num:
        count = count + 1
        q=t2+t1
        t1=t2
        t2=q
        if(t2==num):
            print(num, "occurs at position", count)
            tn=10
            break
    if(tn!=10):
        print(num, "does not occur")