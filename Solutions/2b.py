def geometric():
  print("Enter the list of integers : ",end="")
  l=[int(x) for x in input().split()]
  r=l[1]//l[0]
  f=True
  for i in range(1,len(l)):
    if(l[i]//l[i-1]!=r):
      f=False
      break
    else:
      pass
  print(f)

geometric()