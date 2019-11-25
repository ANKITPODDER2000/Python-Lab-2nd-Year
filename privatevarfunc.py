class increment:
    def __init__(self,num):
        self.__num = num
        self.__display()
    def add(self,a):
        self.__num = self.__num + a
        self.__display()
    def __display(self):
        print("Value stored is : ",self.__num)
n = increment(10)
#n.display()
n.add(10)
n._increment__display()
print(n._increment__num)
#del n
"""
    n.display() ##n is already removed from memory b del n
    free(n)    ======    del n
"""