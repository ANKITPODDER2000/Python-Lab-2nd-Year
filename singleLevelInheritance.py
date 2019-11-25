class person:
    def __init__(self,name):
        self.name = name
    def disname(self):
        print("Person name is : %s"%(self.name))

class student(person):
    def __init__(self,name,course):
        self.course = course
        super().__init__(name)
    def display(self):
        self.disname()
        print("Course name : %s"%(self.course))

a = student("ankit Podder","B.Tech(IT)")
a.display()