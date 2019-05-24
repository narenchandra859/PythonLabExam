def wellbracketed(s):
  l=[]
  for c in s:
    if c == "(":
      l.append(c)
    elif c == ")":
      if l == []:
        return False
      l.pop()
    else:
      pass
  if l == []:
    return True
  else:
    return False

print(wellbracketed("22)"))
print(wellbracketed("(a+b)(a-b)"))
print(wellbracketed("(a(b+c)-d)((e+f)"))