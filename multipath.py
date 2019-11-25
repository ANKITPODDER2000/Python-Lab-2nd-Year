class result:
    def __init__(self,no):
        self.no = no
class IT(result):
    def __init__(self,year,no):
        super().__init__(no)
        self.year = year
class univ(result):
    def __init__(self,rno):
        self.rno = rno
class stud(univ,IT):
    def __init__(self,name,rno,no,year):
        univ.__init__(self,rno)
        IT.__init__(self,year,no)
        self.name = name
    def dis(self):
        print(self.name,self.no,self.rno,self.year,sep="\n")

s = stud("Fizza","13000218193","9.5","2nd year")
s.dis()