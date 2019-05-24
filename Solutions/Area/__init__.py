from math import sqrt

def circArea(r):
  return 3.14*r*r

def rectArea(l, b):
  return l*b

def triArea(a, b, c):
  s=(a+b+c)//2
  return sqrt(s*(s-a)*(s-b)*(s-c))
