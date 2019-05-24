def partition(l):
  for p in l:
    if ord(p[0])>=65 and ord(p[0])<=77:
      print(p)

partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
print()
print()
partition(['Xena', 'Sammy', 'Owen'])