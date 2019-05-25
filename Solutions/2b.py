def geometric(l):
  r=l[1]//l[0]
  f=True
  for i in range(1,len(l)):
    if(l[i]//l[i-1]!=r):
      f=False
      break
    else:
      pass
  return(f)
print("Enter the list of integers : ",end="")
l=[int(x) for x in input().split()]
print(geometric(l))