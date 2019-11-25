a = input("Enter sen : ")
s = a.split(" ")
Dict = {}
for i in s:
    if i not in Dict:
        Dict[i] = 1
    else:
        Dict[i]+=1
s = ""
for i in Dict:
    s = s + i + " "
s = s[:len(s)-1] + "."
print(s)
print(Dict)