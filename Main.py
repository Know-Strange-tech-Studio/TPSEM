import time
from tkinter import *
from tkhtmlview import HTMLLabel
from PIL import Image, ImageTk
import pygame
from math import *

class Mark:
    def __init__(self,canvas:Canvas) -> None:
        self.canvas = canvas
        self.id = self.canvas.create_text(0,0,text="X",anchor="center",fill="#ff0000",font=('Arial', 15, 'bold'))
    def goto(self,long,lat):
        x = (long-118.2)*(948/6)
        y = 748-((lat-21.5)*(748/5))
        self.canvas.moveto(self.id,x,y)

class Wave:
    def __init__(self,canvas:Canvas,index:str,x,y) -> None:
        self.canvas = canvas
        self.id = self.canvas.create_oval(0,0,10,10,width=4,outline="#ff0000")
        self.index = index
        self.loop = 0
        self.scale = 1
        self.x = (x-118.2)*(948/6)
        self.y = 748-((y-21.5)*(748/5))
        pygame.mixer.music.load("./Resource/audios/EEW.wav")
        pygame.mixer.music.play(1)
        #pygame.time.delay(1000)
    def spread(self):
        self.canvas.moveto(self.id,self.x-5*self.scale+5,self.y-5*self.scale+5)
        if self.loop > 500:
            self.delete()
        else:
            self.canvas.scale(self.id,self.x,self.y,1/self.scale,1/self.scale)
            self.loop += 1
            self.scale += 0.1
            self.canvas.scale(self.id,self.x,self.y,self.scale,self.scale)
    def delete(self):
        self.canvas.delete(self.id)
        randering_wave_c.pop(self.index)
        del self

class Time_stamp:
    def __init__(self,canvas:Canvas) -> None:
        self.canvas = canvas
        self.id = self.canvas.create_text(10,720,text="等待時間更新",anchor="w",fill="#ffffff",font=('Arial', 20))
    def refresh_time(self,time:str):
        self.canvas.itemconfig(self.id,text=time)

randering_wave = {}
pygame.mixer.init()

window = Tk()
window.configure(bg="#1e1e1e")
window.title("LTSPM - LT震動與P波監視")
window.geometry("1280x760")
#window.minsize(width=350,height=100)
window.resizable(0,0)
window.iconbitmap(bitmap="./icon.ico")
window.attributes("-topmost",1)


img = Image.open('./tw.png')
tk_img = ImageTk.PhotoImage(img)

canvas = Canvas(window, width=948, height=748,background="#1e1e1e")
canvas.create_image(0, 0,anchor="nw", image=tk_img)
#canvas.create_image(237.0,299.2,anchor="center",image=mark_img)
#canvas.create_rectangle(0,0,100,25)
#a = canvas.create_polygon()
#canvas.scale(a,119,25,10000,10000)
canvas.pack(side="left",padx=5,expand=0)

window.update()

mark = Mark(canvas)
tm = Time_stamp(canvas)

info_zone = Frame(window,bg="#1e1e1e")
info_zone.pack(side="left",fill="both",expand=1)

status = LabelFrame(info_zone,text="status",bg="#f1d171",bd=10) #,height=100
status.pack(fill="x")

status_zone = Canvas(status,bg="#f1d171",height=50)
status_zone.pack(fill="x")

status_icon_img = PhotoImage(file="./Resource/image//0.png")
status_icon = status_zone.create_image(5, 10, anchor="nw",image=status_icon_img)
status_text = status_zone.create_text(50, 5, text="嘉義市 西區", anchor="nw", font=("Arial",20))
status_gal = status_zone.create_text(50, 35, text="0 gal", anchor="nw", font=("Arial",10))

long = Entry(info_zone,width=20,textvariable=StringVar(value="120.5"),justify="center")
long.pack(fill="x")


lat = Entry(info_zone,width=20,textvariable=StringVar(value="23.5"),justify="center")
lat.pack(fill="x")

def wave():
    global randering_wave
    index = str(len(randering_wave) + 1)
    try:
        randering_wave[index] = Wave(canvas,index,float(long.get()),float(lat.get()))
        console.config(text=f"成功發送 id:{floor(time.time()*100)}")
    except:
        console.config(text="這不是數字")

submit = Button(info_zone,text="mark",command=wave,width=20)
submit.pack(fill="x")


console = Label(info_zone,text="nothing",justify="center",bg="#1e1e1e",fg="#ffffff")
console.pack(fill="x")

"""def new_w():
    new_win = Toplevel(window)
    new_win.title("New Window")
 
    # sets the geometry of toplevel
    new_win.geometry("200x200")
    new_win.attributes("-topmost",1)
 
    # A Label widget to show in toplevel
    Label(new_win,
          text ="This is a new window").pack() 

new = Button(info_zone,text="new",command=new_w)
new.pack()"""

    

while True:
    try:
        mark.goto(float(long.get()),float(lat.get()))
    except:pass
    randering_wave_c = randering_wave.copy()
    for cir in randering_wave:
        randering_wave[cir].spread()
    randering_wave = randering_wave_c
    now = time.localtime(time.time())
    tm.refresh_time("%04d/%02d/%02d %02d:%02d:%02d" %(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec))#""
    window.update()
    time.sleep(0.1)
