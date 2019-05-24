from Solutions import Area
while(1):
  i=int(input("Enter \n1.Area of Circle\n2.Area of Rectangle\n3.Area of Scalene Triangle\n"))
  if i == 1:
    r=int(input("Enter radius : "))
    print(Area.circArea(r))
  elif i == 2:
    l=int(input("Enter length : "))
    b=int(input("Enter breadth : "))
    print(Area.rectArea(l,b))
  elif i == 3:
    print("Enter 3 sides : ")
    x=[int(a) for a in input().split()]
    print(Area.triArea(x[0],x[1],x[2]))
  else:
    break


