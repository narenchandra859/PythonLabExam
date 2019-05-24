try:
  print("Enter two integers : ")
  x=int(input())
  y=int(input())
  print("Sum = ",x+y)
  print("Enter 5 list elements : ")
  l=[int(x) for x in input().split()]
  i=int(input("Enter index to print element : "))
  print("Element = ",l[i])
  print("Enter the keys and values into dict : (-1 to stop)")
  d={}
  while(1):
    l=[x for x in input().split()]
    if(l[0]=="-1"):
      break
    else:
      d[l[0]]=l[1]
  k=input("Enter key to find value : ")
  print("Value is ",d[k])
except KeyError:
  print("Key not found!")
except ValueError:
  print("Non integer value given!")
except IndexError:
  print("Index out of range!")
else:
  pass
