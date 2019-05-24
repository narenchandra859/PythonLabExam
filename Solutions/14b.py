f=open("graffit.txt","r+")
print("Initial File:")
s = f.read()
print(s)
s1 = ""
for c in s:
  if ord(c)>=97:
    c=ord(c)-32
    s1 = s1 + chr(c)
  else:
    s1 = s1 + c
f.seek(0)
f.write(s1)
f.seek(0)
print("After change:")
s = f.read()
print(s)
