import tkinter as tk
def nextLabel():
  label = tk.Label(m,text = "Nice job!..").pack()

def nextButton():
  button1 = tk.Button(m,text = "Second Button", command = nextLabel)
  button1.pack()

m = tk.Tk()

canvas = tk.Canvas(m,height=200,width=200)
canvas.pack()

button=tk.Button(m,text = "First Button",command = nextButton)
button.pack()

m.mainloop()