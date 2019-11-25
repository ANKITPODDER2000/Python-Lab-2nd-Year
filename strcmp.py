a = input("Enter 1st string : ")
b = input("Enter 2nd string : ")
if len(a)!=len(b):
    print("%s is not same as %s"%(a,b))
else:
    for i in range(len(a)):
        if a[i]!=b[i]:
            print("%s is not same as %s"%(a,b))
            break
    else:
        print("%s is same as %s"%(a,b))