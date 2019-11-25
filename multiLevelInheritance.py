class person:
    def __init__(self,name):
        self.name = name
    def dis(self):
        print("Name : %s"%(self.name))
        
class teacher(person):
    def __init__(self,name,exp):
        super().__init__(name)
        self.exp = exp
    def display(self):
        self.dis()
        print("exp : %s"%(self.exp))

class hod(teacher):
    def __init__(self,name,exp,sub):
        super().__init__(name,exp)
        self.sub = sub
    def d(self):
        self.display()
        print("Sub is : %s"%(self.sub))

h = hod("Andrew","5","ML")
h.d()