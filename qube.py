import math
def qube(num):
    return math.pow(num,3)
for i in range(1,11):
    print("Qube of %d is : %d"%(i,qube(i)))