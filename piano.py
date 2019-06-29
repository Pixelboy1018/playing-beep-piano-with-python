from tkinter import *
import winsound as w

#常量
time=500
low=(0,200,250,300,400,500,600,700)
normal=(0,800,900,1000,1100,1200,1300,1400)
high=(0,1500,1600,1700,1800,1900,2000,2100)

def dol(event):
     w.Beep(low[1],time)     
def rel(event):
     w.Beep(low[2],time)
def mil(event):
     w.Beep(low[3],time)
def fal(event):
     w.Beep(low[4],time)
def sol(event):
     w.Beep(low[5],time)
def lal(event):
     w.Beep(low[6],time)
def sil(event):
     w.Beep(low[7],time)
def do(event):
     w.Beep(normal[1],time)
def re(event):
     w.Beep(normal[2],time)
def mi(event):
     w.Beep(normal[3],time)
def fa(event):
     w.Beep(normal[4],time)
def so(event):
     w.Beep(normal[5],time)
def la(event):
     w.Beep(normal[6],time)
def si(event):
     w.Beep(normal[7],time)
def doh(event):
     w.Beep(high[1],time)
def reh(event):
     w.Beep(high[2],time)
def mih(event):
     w.Beep(high[3],time)
def fah(event):
     w.Beep(high[4],time)
def soh(event):
     w.Beep(high[5],time)
def lah(event):
     w.Beep(high[6],time)
def sih(event):
     w.Beep(high[7],time)
def slow(event):
     global time    #我就是要在函数里修改全局变量
     time=800
def fast(event):
     global time
     time=150
def middle(event):
     global time
     time=500


root=Tk()
root.title('PB vocal piano')
pic=PhotoImage(file='background.gif')

msg=Frame(root)
#low
msg.bind("<Control-Key-1>",dol)
msg.bind("<Control-Key-2>",rel)
msg.bind("<Control-Key-3>",mil)
msg.bind("<Control-Key-4>",fal)
msg.bind("<Control-Key-5>",sol)
msg.bind("<Control-Key-6>",lal)
msg.bind("<Control-Key-7>",sil)
#normal
msg.bind("<KeyPress-1>",do)
msg.bind("<KeyPress-2>",re)
msg.bind("<KeyPress-3>",mi)
msg.bind("<KeyPress-4>",fa)
msg.bind("<KeyPress-5>",so)
msg.bind("<KeyPress-6>",la)
msg.bind("<KeyPress-7>",si)
#high
msg.bind("<Alt-Key-1>",doh)
msg.bind("<Alt-Key-2>",reh)
msg.bind("<Alt-Key-3>",mih)
msg.bind("<Alt-Key-4>",fah)
msg.bind("<Alt-Key-5>",soh)
msg.bind("<Alt-Key-6>",lah)
msg.bind("<Alt-Key-7>",sih)
#extra
msg.bind("<Key-s>",slow)      #注意区分大小写
msg.bind("<Key-d>",middle)
msg.bind("<Key-f>",fast)

msg.focus_set()
msg.pack()

box=Label(msg,
      text="Music on Keyboard\nplay it with 1 to 7",
      justify=LEFT,
      image=pic,
      compound=CENTER,
      font=("宋体",20),
      fg="blue"
      )
box.pack()

mainloop()
