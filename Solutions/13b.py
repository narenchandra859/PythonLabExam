def rotatelist(ls, k):
  k = k % len(ls)
  k = len(ls) - k
  if k>=0:
    newl = ls[k:]
    newl.extend(ls[:k])
  else:
    newl = ls[:]
  return newl

print(rotatelist([1,2,3,4,5],1)) #output is [5, 1, 2, 3, 4]
print(rotatelist([1,2,3,4,5],3)) #output is [3, 4, 5, 1, 2]
print(rotatelist([1,2,3,4,5],12)) #output is [4, 5, 1, 2, 3]
print(rotatelist([1,2,3,4,5],-20)) #output same list