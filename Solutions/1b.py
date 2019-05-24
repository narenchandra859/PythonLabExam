import tkinter
m=tkinter.Tk()
m.counter=0
def inc():
  m.counter = m.counter+1
  L['text']=m.counter
def dec():
  m.counter = m.counter-1
  L['text']=m.counter
b=tkinter.Button(m,text='Up',command=inc)
b1=tkinter.Button(m,text='Down',command=dec)
b.pack()
b1.pack()
L=tkinter.Label(m,text=m.counter)
L.pack()
m.mainloop()