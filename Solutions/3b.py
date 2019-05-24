import tkinter as tk
def cir():
  canvas.create_oval(5,5,100,100,width=2)
m=tk.Tk()
canvas=tk.Canvas(m,width=200,height=200)
canvas.configure(background="green")
canvas.pack()
b=tk.Button(m,text="Create circle!",command=cir)
b.pack()
m.mainloop()
