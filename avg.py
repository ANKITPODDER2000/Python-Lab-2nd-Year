def avg(a,b):
    return (a+b)/2
a,b = input("Enter two numbers : ").split(" ")
a,b = float(a),float(b)
print("Avg of %d & %d is %.f"%(a,b,avg(a,b)))