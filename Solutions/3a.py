class Vehicle():
  def __init__(self,name):
    self.name=name
class Bike(Vehicle):
  def __init__(self,name,age):
    Vehicle.__init__(self,name)
    self.age=age

class Car(Vehicle):
  def __init__(self,name,age,type):
    Vehicle.__init__(self,name)
    self.age=age
    self.type=type
  def __str__(self):
    s = "Car name = "+self.name+"  Age = "+str(self.age)+"  Type = "+self.type
    return s

class PedalBikes(Bike):
  def __init__(self,name,age,type):
    Bike.__init__(self,name,age)
    self.type=type
  def __str__(self):
    s = "Bike name = "+self.name+"  Age = "+str(self.age)+"  Type = "+self.type
    return s

class MotorBikes(Bike):
  def __init__(self,name,age,type):
    Bike.__init__(self,name,age)
    self.type=type
  def __str__(self):
    s = "Bike name = "+self.name+"  Age = "+str(self.age)+"  Type = "+self.type
    return s

print("Creating Car, Age 10 and type Hyper")
A=Car("A",10,"Hyper")
print(A)
print("Creating Pedal Bike, Age 5 and type Electric")
PB=PedalBikes("PB",5,"Electric")
print(PB)
print("Creating Motor Bike, Age 4 and type Petrol")
MB=MotorBikes("MB",4,"Petrol")
print(MB)
