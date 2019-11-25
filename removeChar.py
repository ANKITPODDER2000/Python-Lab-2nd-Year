a = input("Enter the string : ")
a = a.upper()
s = ""
for i in a:
    if i not in s:
        s+=i
    else:
        s += '@'
print("String is : ",s)