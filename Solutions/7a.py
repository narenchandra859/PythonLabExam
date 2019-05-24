def add():
  w=input("Enter word : ")
  m=input("Enter meaning : ")
  d[w]=m

def search():
  print("Enter word to find meaning : ")
  w=input()
  if w in d.keys():
    print("Meaning : ",d[w])
  else:
    print("Word not found")

def findsim():
  print("Enter meaning to find similar words : ")
  m=input()
  for k, v in d.items():
    if v == m:
      print("Similar word = ",k)

def rem():
  print("Enter word to be removed : ")
  w=input()
  if w in d.keys():
    d.pop(w)
  else:
    print("Word not found")

def disp():
  for k in sorted(d.keys()):
    print(k)

d={}
while(1):
  i=int(input("Enter 1.Add 2.Search 3.FindSim 4.Rem 5.Disp 6.Exit : "))
  if i == 1:
    add()
  elif i == 2:
    search()
  elif i == 3:
    findsim()
  elif i == 4:
    rem()
  elif i == 5:
    disp()
  else:
    break
