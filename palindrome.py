a = input("Enter the string : ")
l = list(a)
l.reverse()
l = "".join(l)
if l==a:
    print("Palindrome")
else:
    print("Nott palindrome")