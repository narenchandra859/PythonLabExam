def exclamation(s):
  s1=""
  vow = ['a','e','i','o','u','A','I','E','O','U']
  for x in s:
    if x in vow:
      s1=s1+4*x
    else:
      s1=s1+x
  s1=s1+"!"
  return s1

print(exclamation("argh"))
