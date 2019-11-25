class increment:
    def __init__(self,num):
        self.num = num
    def add(self,a):
        self.num = self.num + a
    def display(self):
        print("Value stored is : ",self.num)
    def __del__(self):
        print("From Del func")
        self.display()
n = increment(10)
n.display()
n.add(10)
n.display()
del n
"""
    n.display() ##n is already removed from memory b del n
    free(n)    ======    del n
"""