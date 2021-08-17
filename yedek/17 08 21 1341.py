import os , subprocess, tkinter , time

def impo(x):
    x = x.split(",")
    for q in x:
        if "as" not in q and " " in q:
            exec("from " + q.split(" ")[0] + " import " + q.split(" ")[1] + '\nprint("-------- imported ' + q + ' --------")', globals())
        else:
            exec("import " + q +'\nprint("-------- imported'+q+' --------")',
            globals())

def cmdd(x): return subprocess.getoutput(x)
print("------------ IMPORTED ---------")

os.chdir("adb")


class window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.portnow=5037
        self.started_time=time.time()
        self.create_window()
        self.clock()
    
    def create_window(self):
        self.nowport = tkinter.StringVar()
        self.myip = tkinter.StringVar()
        self.targetip = tkinter.StringVar()
        self.nowport.set("5037")
        self.myip.set("192.168.1.1")
        self.targetip.set("192.168.1.100-105")

        
        self.protocol('WM_DELETE_WINDOW', self.exit)
        self.title("adbPython")
        self.geometry("600x400")
        
        self.lfback = tkinter.LabelFrame(self , bg="black")
        self.lfback.pack(expand="yes",fill="both")

        self.lfsol= tkinter.LabelFrame(self.lfback ,bg="light blue",width=120)
        self.lfsol.pack(side="left",anchor="n",fill="y",)

        self.lfust= tkinter.LabelFrame(self.lfback ,height=50 ,bg="cyan2")
        self.lfust.pack(anchor="n",fill="x")

        self.lforta = tkinter.LabelFrame(self.lfback,bg="gray80")
        self.lforta.pack(anchor="n",fill="both",expand=True)

        tkinter.Label(self.lfust, font=9, bg="gray60", width=10, text="My ip").grid(column=0, row=0)
        tkinter.Label(self.lfust, font=9, bg="gray50", width=10, text="Target ip").grid(column=0, row=1)
        self.tipbutton = tkinter.Label(self.lfust, font=9,bg="gray80", text=self.targetip.get())
        self.mipbutton = tkinter.Label(self.lfust, font=9, bg="gray90", text=self.myip.get())
        self.mipbutton.grid(column=1, row=0)
        self.tipbutton.grid(column=1, row=1)


        self.labeltime=tkinter.Label(self.lfsol,width=20,font=10,height=1 ,bg="grey", anchor='nw',text=str(round(time.time()-self.started_time,2)))
        self.labeltime.pack(pady=5,anchor="s")
        self.devices = tkinter.Button(self.lfsol,text="devices")
        self.devices.pack()

    def clock(self):
        self.labeltime.configure(text=str(round(time.time()-self.started_time,2)))
        self.targetip.set(time.time())
        self.after(78,self.clock)

    def exit(self):self.after(1,self.destroy)

if __name__ == '__main__':
    window1 = window()
    window1.mainloop()

"""
    self.protocol('WM_DELETE_WINDOW', self.exit)
    self.title("adbPython")
    self.geometry("600x400")
  grid(column=1, row=0, ipadx=10, pady=10,sticky="o")
  pack(side="left",anchor="n",expand=True,fill="both") #n, ne, e, se, s, sw, w, nw
Button(self.frameleft1, bd=5, font=8, height=1, width=9, text="devices", command=self.com1)
Label(self.frameleft1, bg="grey", height=2, width=12,anchor='w', font=10,textvariable=self.entvar1).configurate(text...)
Entry(self.frameleft1,font=10,width=10,justify="center",textvariable=self.entvar1)
ENTER.trace("w", lambda *args: self.valueControl())

from tkinter import messagebox
messagebox.showinfo( "Hello Python", "Hello World")

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

CheckVar1 = IntVar()
C1 = Checkbutton(window, text = "Music", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5, width = 20)


E1 = Entry(window, bd =5)

Lb1 = Listbox(window)
Lb1.insert(1, "C")
Lb1.insert(2, "C++")
Lb1.pack()

self.update_clock()
self.root.after(1000, self.update_clock)
-----------------------------------------------------------------------
def devices():lbl.configure(text=cmdd("adb devices"))
def killserver():lbl.configure(text=cmdd("adb kill-server"))

lbltop=tkinter.Label(width=10,height=20)
lbltop.grid()

tkinter.Frame

btn1 = tkinter.Button(lbltop,text="devices",fg="red",command=devices)
btn1.grid(collom)

btn1 = tkinter.Button(lbltop,text="kill server",fg="red",command=killserver)
btn1.grid()


top.mainloop()
"""
