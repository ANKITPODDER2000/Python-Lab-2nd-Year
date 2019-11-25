"""
class student:
    num = 1
    def __init__(self,x = 0,scl = None):
        self.x = x
        self.scl = scl
s1 = student()
"""

class student:
    num = 1
    def __init__(self,x = 0,scl = None):
        self.x = x
        self.scl = scl
    def display(self):
        print("Student age %d & Student name : %s"%(self.x,self.scl))
s1 = student(10,"k K Hindu")
s1.display()

s2 = student(20,"k K Hindu")
s2.display()

print(student.num)