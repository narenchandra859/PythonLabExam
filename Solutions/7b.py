# Brute force all possible (nC3) possible pairs to check for target

def subsetSum(l, t):
  for i in range(0,len(l)):
    for j in range(i+1,len(l)):
      for k in range(j+1,len(l)):
        if l[i]+l[j]+l[k]==t:
          return True
  return False

print("Enter the list : ")
l=[int(x) for x in input().split()]
t=int(input("Enter the target : "))
print(subsetSum(l,t))