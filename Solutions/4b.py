class Mylist:
  def __init__(self, list=[]):
    self.l=list[:]
  def __add__(self, m):
    return self.l+m
  def __str__(self):
    s=""
    for x in self.l:
      s=s+" "+str(x)
    return s
print("Enter a list : ")
x=[int(x) for x in input().split()]
l=Mylist(x)
print("Enter elements to add : ")
x=[int(x) for x in input().split()]
l=l+x
l=Mylist(l)
print("Final list = ")
print(l)
print("Type of final list = ",type(l))