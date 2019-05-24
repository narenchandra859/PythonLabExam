class time:
  def __init__(self,h=0,m=0,s=0):
    self.hours=h
    self.minutes=m
    self.seconds=s

  def findseconds(self):
    total = self.seconds
    total = total + (self.minutes*60)
    total = total + (self.hours*60*60)
    return total

  def printTime(self):
    print("Time is : ",self.hours,":",self.minutes,":",self.seconds,sep="")

print("Enter the time : ")
h=int(input("Enter hours : "))
m=int(input("Enter minutes : "))
s=int(input("Enter seconds : "))

T=time(h,m,s)

T.printTime()
print("Total seconds = ",T.findseconds())
