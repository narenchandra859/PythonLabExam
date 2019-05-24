import fileinput
def filewrite():
  s=input("Enter the contents to be written into file : ")
  f=open("File1.txt","w")
  f.write(s)
  f.close()
  f=open("File1.txt","r")
  w=0
  for line in f:
    l=line.split()
    w=w+len(l)
  print("Number of words = ",w)

filewrite()