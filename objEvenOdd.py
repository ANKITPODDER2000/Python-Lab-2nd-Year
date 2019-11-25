class evod:
    even = []
    odd = []
    def __init__(self,num):
        if num%2==0:
            evod.even.append(num)
        else:
            evod.odd.append(num)
        self.list_show()
    def list_show(self):
        print("Odd Numbers are : ",end="")
        for i in evod.odd:
            print(i,end=" ")
        print()
        print("Even Numbers are : ",end="")
        for i in evod.even:
            print(i,end=" ")
        print()
n = evod(10)
n = evod(20)
n = evod(15)
n = evod(25)
print("==============================")
print(evod.even)
print("==============================")
print(evod.odd)