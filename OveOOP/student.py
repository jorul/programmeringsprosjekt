class student:
    def __init__(self, name, aer):
        self.name = name
        self.aer = aer
        #def nya(self):
#            self.aer += 1

class smarting(student):
    def __init__(self, name, aer):
        self.name = name
        self.aer = aer
        self.smart = True

class dumming(student):
    def __init__(self, name, aer):
        self.name = name
        self.aer = aer
        self.smart = False

p = student("Per",4)
print(p.name)
j = smarting("Jørgen", 7)
print(j.name)
print(j.smart)
d = dumming("dumgutt", 0)
print(d.name)
print(d.smart)
#p.nya()
print(p.aer)
