Dict = {"Rno":22,"Name":"ABC","course":"B.Tech"}
d = {x:2*x for x in range(1,5)}
print(Dict)
print(d)
Dict["Dur"] = "4 yrs"
print(Dict)
Dict["Name"] = "Ankit"
print(Dict)
del Dict["Name"]
print(Dict)
#Dict.clear()
print(Dict.pop("Rno"))
print(Dict)
print("Values : ",end="")
for i in Dict.values():
    print(i,end=" ")
print("\n=============")
print("Keys : ",end="")
for i in Dict:
    print(i,end=" ")
a = input("Enter key : ")
if a not in Dict:
    Dict[a] = input("Enter value for %s"%(a))
print("==========================")
print(Dict)