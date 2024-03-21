class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def personinfo(self):
    print(self.name + " is " + str(self.age) + " year(s) old. ")

P1=person('Rickon',25)
P2=person('Raj',45)
P1.personinfo()
P2.personinfo()