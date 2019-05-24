class City:
  def __init__(self,name="default",places=[]):
    self.name=name
    self.places=places

  def addplace(self,place):
    self.places.append(place)

  def remplace(self,place):
    self.places.remove(place)

  def printplace(self):
    for p in self.places:
      print(p)

while(1):
  i=int(input("1.Enter City\n2.Enter City and Place\n3.Add place\n4.Remove place\n5.Displace Places\n6.Exit\n"))
  if i == 1:
    c=input("Enter city name : ")
    city=City(c)
  elif i == 2:
    c=input("Enter city name : ")
    print("Enter list of places : ")
    l=[x for x in input().split()]
    city=City(c,l)
  elif i == 3:
    p=input("Enter place to add : ")
    city.addplace(p)
  elif i == 4:
    p=input("Enter place to remove : ")
    city.remplace(p)
  elif i == 5:
    city.printplace()
  else:
    break

