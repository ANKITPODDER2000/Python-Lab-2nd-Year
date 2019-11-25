class increment:
    def __init__(self,num):
        self.num = num
    def add(self,a):
        self.num = self.num + a
    def display(self):
        print("Value stored is : ",self.num)
n = increment(10)
n.display()
n.add(10)
n.display()