vowel = ["a","A","E","e","i","I","O","o","U","u"]
a = input("Enter the string : ")
v = 0
c = 0
for i in a:
    if i in vowel:
        v+=1
    elif i!=" ":
        c+=1
print("Consonent = %d  &&  Vowel  =  %d"%(c,v))