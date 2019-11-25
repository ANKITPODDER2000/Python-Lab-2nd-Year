a,b = input("Enter two number : ").split(" ")
a,b = int(a),int(b)
temp = a
a = b
b = temp
print("a = %d and b = %d"%(a,b))