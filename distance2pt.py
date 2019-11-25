import math
x1,y1 = input("Enter a x and y of 1st pt : ").split(" ")
x2,y2 = input("Enter a x and y of 2nd pt: ").split(" ")
x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
dis = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
print("Distance from (%d,%d) to (%d,%d) is : %f"%(x1,y1,x2,y2,dis))