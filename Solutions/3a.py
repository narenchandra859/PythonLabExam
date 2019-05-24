class Vehicle():
  def __init__(self,name):
    self.name=name
class Bike(Vehicle):
  def __init__(self,name,age):
    Vehicle.__init__(self,name)
    self.age=age
class Car(Vehicle):
  def __init__(self,name="Vehicle",age=1):
    Vehicle.__init__(self,name)
    self.age=age
class PedalBikes(Bike):
  def __init__(self,name="Vehicle",age=0,type="Petrol"):
    Bike.__init__(self,name,age)
    self.type=type
class MotorBikes(Bike):
  def __init__(self,name="Vehicle",age=0,type="Diesel"):
    Bike.__init__(self,name,age)
    self.type=type

A=PedalBikes()
B=MotorBikes()
C=Car()
