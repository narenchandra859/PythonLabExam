def sublist(l1, l2):
  checkInd = 0
  for i in range(0,len(l2)):
    if l2[i]==l1[checkInd]:
      checkInd = checkInd + 1
  if checkInd >= len(l1):
    return True
  return False

print(sublist([15, 1, 100], [20, 15, 30, 50, 1, 100]))
print()
print(sublist([15, 50, 20], [20, 15, 30, 50, 1, 100]))
print()