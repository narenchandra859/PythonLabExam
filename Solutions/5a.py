class NegBalance(Exception):
  pass

class AddNeg(Exception):
  pass

class BankAccount:
  def __init__(self,amt=0):
    self.num=amt
  def deposit(self,amt=0):
    try:
      if amt<0:
        raise(AddNeg)
      else:
        pass
    except AddNeg:
      print("Can't deposit negetive amount!")
    else:
      self.num=self.num+amt
  def withdraw(self,amt=0):
    try:
      if self.num-amt<0:
        raise(NegBalance)
      else:
        pass
    except NegBalance:
      print("Can't have negetive balance!")
    else:
      self.num=self.num-amt
  def bal(self):
    print("Balance = ",self.num)

p=int(input("Enter the principal amount in the bank : "))
B=BankAccount(p)
while(1):
  print("Enter 1 to deposit and 2 to withdraw or 3 to show balance and 4 to exit")
  i=int(input())
  if i == 1:
    d=int(input("Enter the amount to deposit : "))
    B.deposit(d)
  elif i == 2:
    w=int(input("Enter the amount to withdraw : "))
    B.withdraw(w)
  elif i == 3:
    B.bal()
  else:
    break
