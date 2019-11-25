a,b = input("Enter two number : ").split(" ")
a,b = int(a),int(b)
try:
    d = a/b
    print("Division is : ",d)
except ZeroDivisionError:
    print("Error")
else:
    print("OK")