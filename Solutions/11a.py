def names():
  d={}
  while(1):
    s=input("Enter next name: ")
    if s == "":
      break
    if s in d.keys():
      d[s] = d[s] + 1
    else:
      d[s] = 1
  for k in sorted(d.keys()):
    if d[k]==1:
      print("There is",d[k],"student named",k)
    else:
      print("There are",d[k],"students named",k)

names()