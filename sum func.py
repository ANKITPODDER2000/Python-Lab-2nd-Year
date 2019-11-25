def sum(a=0,b=0):
    print("Sum is : %d"%(a+b))
a,b = input("Enter number : ").split(" ")
a,b = int(a),int(b)
sum(a,b)