a,b = input("Enter range : ").split(" ")
(a,b) = (int(a),int(b))
if a>b:
    for i in range(b,a+1):
        print(i)
else:
    for i in range(a,b+1):
        print(i)
