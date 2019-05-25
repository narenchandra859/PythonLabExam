class NegBalance(Exception):
  pass

class AddNeg(Exception):
  pass

class MinBal(Exception):
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
      elif self.num-amt<1000:
        raise(MinBal)
      else:
        pass
    except NegBalance:
      print("Can't have negetive balance!")
    except MinBal:
      print("Need to have minimum balance 1000!")
    else:
      self.num=self.num-amt
  def bal(self):
    print("Balance = ",self.num)

try:
  p=int(input("Enter the principal amount in the bank : "))
  if p<1000:
    raise(MinBal)
  B=BankAccount(p)
except MinBal:
  print("Need to have minimum balance 1000!")
else:
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
