class student:
    def setid(self,id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

s = student()
s.setid(1234)
s.setname('Raghul')
print(s.getid())
print(s.getname())
