import time
from tkinter import *

window = Tk()
window.geometry("500x500")

canvas = Canvas(window,width=400,height=400,bg="black")
oval = canvas.create_oval(10,10,30,30,fill="blue")
canvas.pack(pady=20)

def m():
    canvas.move(oval,-2,0)
    time.sleep(1)
    canvas.after(10,m)

if __name__ == "__main__":
    m()
    window.mainloop()