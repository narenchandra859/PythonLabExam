class Point:
  def __init__(self, x=0, y=0):
    self.X=x
    self.Y=y
  def __add__(self,p):
    A=Point()
    A.X=self.X+p.X
    A.Y=self.Y+p.Y
    return A
  def read(self):
    self.X=int(input("Enter X coord : "))
    self.Y=int(input("Enter Y coord : "))
  def write(self):
    print("X Coord = ",self.X,"Y Coord = ",self.Y)

A=Point()
A.read()
B=Point(6,10)
C=A+B
C.write()