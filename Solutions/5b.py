from Solutions import Stack
from Solutions import Queue

i=int(input("Enter 1 for Stack and 2 for Queue : "))
l = []
while(1):
  c=int(input("Enter 1.Push\t2.Pop\t3.Disp\t4.Exit : "))
  if c == 1:
    x=int(input("Enter element : "))
    if i==1:
      Stack.push(l,x)
    else:
      Queue.enqueue(l,x)
  elif c == 2:
    if i==1:
      print("Element popped : ",Stack.pop(l))
    else:
      print("Element dequeued : ",Queue.dequeue(l))
  elif c == 3:
    for x in l:
      print(x, end = " ")
  else:
    break
