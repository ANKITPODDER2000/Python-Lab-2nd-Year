import math
def isprime(num):
    for i in range(2,math.ceil(math.sqrt(num))):
        if num%i==0:
            return False
    return True
a = int(input("Enrter number : "))
if isprime(a):
    print("%d is a Prime no"%(a))
else:
    print("%d is not a Prime no"%(a))