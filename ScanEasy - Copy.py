import PIL.Image, PIL.ImageTk
from tkinter import *
from tkinter import ttk 
import tkinter as tk
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))
##Change the path of the Image Files to your corresponding location before launching it in your desktop



def callback(*args):
        btn.config(bg='light grey')
        btn2.config(bg='light grey')
        btn3.config(bg='light grey')
        btn4.config(bg='light grey')
        btn5.config(bg='light grey')
        btn6.config(bg='light grey')
        btn7.config(bg='light grey')
        btn8.config(bg='light grey')

def nothing():
    name = selectedScanner.get()
    print(name) 
    if name == "Zebra":
        ctr=1
    elif name == "Heroje Wireless":
        ctr=2
    elif name == "Heroje Wired":
        ctr=3
    else:
        ctr=0
    return ctr

def c_det():
    
    global n1
    
    print(n1)
    
    n2=nothing()
    
    print(n1-n2)
    
    if ((n1-n2)!=0):
        btn.config(bg='light grey')
        btn2.config(bg='light grey')
        btn3.config(bg='light grey')
        btn4.config(bg='light grey')
        btn5.config(bg='light grey')
        btn6.config(bg='light grey')
        btn7.config(bg='light grey')
        btn8.config(bg='light grey')
        n1=n2
        
    variable.trace("w", callback)
    



def showImage():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk)
    if ctr==2:
        lbl8.configure(image=imagehero_tk)
    if ctr==3:
        lbl8.configure(image=imageherow_tk)
        
    if btn.config('text')[-1] == 'Enable':
        btn2.config(bg='light grey')
        btn.config(bg='light green')
        print ("pressed enabled")
        
def showImage1():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk1)
    if ctr==2:
        lbl8.configure(image=imagehero_tk1)
    if ctr==3:
        lbl8.configure(image=imageherow_tk1)
        
    if btn2.config('text')[-1] == 'Disable':
        btn2.config(bg='red')
        btn.config(bg='light grey')
        print ("pressed disabled")
   
def showImage2():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk2)
    if ctr==2:
        lbl8.configure(image=imagehero_tk2)
    if ctr==3:
        lbl8.configure(image=imageherow_tk2)
        
    if btn3.config('text')[-1] == 'Enable':
        btn4.config(bg='light grey')
        btn3.config(bg='light green')
        print ("pressed enabled")

def showImage3():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk3)
    if ctr==2:
        lbl8.configure(image=imagehero_tk3)
    if ctr==3:
        lbl8.configure(image=imageherow_tk3)
            
    if btn4.config('text')[-1] == 'Disable':
        btn4.config(bg='red')
        btn3.config(bg='light grey')
        print ("pressed disabled")

def showImage4():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk4)
    if ctr==2:
        lbl8.configure(image=imagehero_tk4)
    if ctr==3:
        lbl8.configure(image=imageherow_tk4)
        
    if btn5.config('text')[-1] == 'Enable':
        btn6.config(bg='light grey')
        btn5.config(bg='light green')
        print ("pressed enabled")
        
def showImage5():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk5)
    if ctr==2:
        lbl8.configure(image=imagehero_tk5)
    if ctr==3:
        lbl8.configure(image=imageherow_tk5)
    if btn6.config('text')[-1] == 'Disable':
        btn6.config(bg='red')
        btn5.config(bg='light grey')
        print ("pressed disabled")

def showImage6():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk6)
    if ctr==2:
        lbl8.configure(image=imagehero_tk6)
    if ctr==3:
        lbl8.configure(image=imageherow_tk6)
        
    if btn7.config('text')[-1] == 'Enable':
        btn8.config(bg='light grey')
        btn7.config(bg='light green')
        print ("pressed enabled")

def showImage7():
    ctr = nothing()
    c_det()
    if ctr==1:
        lbl8.configure(image=image_tk7)
    if ctr==2:
        lbl8.configure(image=imagehero_tk7)
    if ctr==3:
        lbl8.configure(image=imageherow_tk7)
        
    if btn8.config('text')[-1] == 'Disable':
        btn8.config(bg='red')
        btn7.config(bg='light grey')
        print ("pressed disabled")


    

def reset():
    print("Reset")
    c_det()
    ctr = nothing()
    if ctr==1:
        lbl9.configure(image=image_tk9)
    if ctr==2:
        lbl9.configure(image=imagehero_tk9)
    if ctr==3:
        lbl9.configure(image=imageherow_tk9)
   
        
root = tk.Tk() 
root.title('ScanEasy')

'''

def button_callback(state):
    print('Button Callback', state)
      
class Button(ttk.Button):
     
    def __init__(self, parent, active_color=None, **kwargs):
        self.active_color = active_color
        super().__init__(**kwargs)
         
        self.callback = kwargs['command'] if 'command' in kwargs else None
        self['command'] = self.change_color
        self.bg_color = self['bg']
        self.state = False
         
    def change_color(self):
        self.state = not self.state
        self['bg'] = self.active_color if self.state else self.bg_color
        if self.callback: self.callback(self.state)
  
#Button(root, '#00ffff', text='one', command=button_callback).pack()
#Button(root, '#90ee90', text='two').pack()
#Button(root, '#90ee90',text='three').pack()

'''


c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=4, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c1 = ttk.Frame(root, padding=(5, 5, 12, 0))
c1.grid(column=6, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c2 = ttk.Frame(root, padding=(5, 5, 12, 0))
c2.grid(column=4, row=2, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c3 = ttk.Frame(root, padding=(5, 5, 12, 0))
c3.grid(column=6, row=2, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c4 = ttk.Frame(root, padding=(5, 5, 12, 0))
c4.grid(column=4, row=4, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c5 = ttk.Frame(root, padding=(5, 5, 12, 0))
c5.grid(column=6, row=4, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c6 = ttk.Frame(root, padding=(5, 5, 12, 0))
c6.grid(column=4, row=6, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c7 = ttk.Frame(root, padding=(5, 5, 12, 0))
c7.grid(column=6, row=6, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

c8 = ttk.Frame(root, padding=(5, 5, 12, 0))
c8.grid(column=5, row=10, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

creset = ttk.Frame(root, padding=(5, 5, 12, 0))
creset.grid(column=8, row=10, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)



#ZEBRA SCANNER
fname = "C:/DS2208/zebrabarcode_enable.png"
image_tk = PIL.ImageTk.PhotoImage(PIL.Image.open(fname))

fname1 = "C:/DS2208/zebrabarcode_disable.png"
image_tk1 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname1))  # new image object

fname2 = "C:/DS2208/zebracode93_enable.png"
image_tk2 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname2))

fname3 = "C:/DS2208/zebracode93_disable.png"
image_tk3 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname3))

fname4 = "C:/DS2208/zebradatamatrix_enable.png"
image_tk4 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname4))

fname5 = "C:/DS2208/zebrabarcode_disable.png"
image_tk5 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname5))

fname6 = "C:/DS2208/zebraqrcode_enable.png"
image_tk6 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname6))

fname7 = "C:/DS2208/zebraqrcode_disable.png"
image_tk7 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname7))

fname8 = "C:/DS2208/zebrabarcode_enable.png"
image_tk8 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname8))

fname9 = "C:/DS2208/zebra_reset.png"
image_tk9 = PIL.ImageTk.PhotoImage(PIL.Image.open(fname9))


#HEROJE Wireless
fnamehero = "C:/DS2208/herojebarcode_enable.png"
imagehero_tk = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero))

fnamehero1 = "C:/DS2208/herojebarcode_disable.png"
imagehero_tk1 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero1))  # new image object

fnamehero2 = "C:/DS2208/herojecode93_enable.png"
imagehero_tk2 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero2))

fnamehero3 = "C:/DS2208/herojecode93_disable.png"
imagehero_tk3 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero3))

fnamehero4 = "C:/DS2208/herojedm_enable.png"
imagehero_tk4 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero4))

fnamehero5 = "C:/DS2208/herojedm_disable.png"
imagehero_tk5 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero5))

fnamehero6 = "C:/DS2208/herojeqr_enable.png"
imagehero_tk6 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero6))

fnamehero7 = "C:/DS2208/herojeqr_disable.png"
imagehero_tk7 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero7))

fnamehero8 = "C:/DS2208/herojebarcode_enable.png"
imagehero_tk8 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero8))

fnamehero9 = "C:/DS2208/heroje_reset.png"
imagehero_tk9 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnamehero9))


#HEROJE Wired
fnameherow = "C:/DS2208/herojewbarcode_enable.png"
imageherow_tk = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow))

fnameherow1 = "C:/DS2208/herojewbarcode_disable.png"
imageherow_tk1 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow1))  # new image object

fnameherow2 = "C:/DS2208/herojewcode93_enable.png"
imageherow_tk2 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow2))

fnameherow3 = "C:/DS2208/herojewcode93_disable.png"
imageherow_tk3 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow3))

fnameherow4 = "C:/DS2208/herojewdm_enable.png"
imageherow_tk4 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow4))

fnameherow5 = "C:/DS2208/herojewdm_disable.png"
imageherow_tk5 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow5))

fnameherow6 = "C:/DS2208/herojewqr_enable.png"
imageherow_tk6 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow6))

fnameherow7 = "C:/DS2208/herojewqr_disable.png"
imageherow_tk7 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow7))

fnameherow8 = "C:/DS2208/herojewbarcode_enable.png"
imageherow_tk8 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow8))

fnameherow9 = "C:/DS2208/herojew_reset.png"
imageherow_tk9 = PIL.ImageTk.PhotoImage(PIL.Image.open(fnameherow9))

variable = StringVar(root)


# Drop down List
ScannerList = ["Choose Scanner","Zebra", "Heroje Wireless", "Heroje Wired"]
selectedScanner = StringVar()
selectedScanner.set(ScannerList[0])
ScannerMenu = OptionMenu(root,selectedScanner, *ScannerList)
ScannerMenu.grid(column=8,row=0)

variable.set(ScannerList[0])

n1 = nothing()

# Button for selection
#selectBtn = Button(root,text="Confirm Scanner",command=nothing)
#selectBtn.grid(column=8,row=2)

#Button for Factory Reset

variable.trace("w", callback)



factoryBtn = Button(root,text="Reset",command=reset)
factoryBtn.grid(column=8,row=4)


l1 = Label(root,text="Bar Code")
l1.grid(row=0,column=2,padx=10, pady=10)
btn = tk.Button(c, text="Enable", command=showImage)
lbl1 = ttk.Label(c)
btn.grid(column=0, row=0, sticky=N, pady=5, padx=5)
lbl1.grid(column=4, row=0, sticky=N, pady=5, padx=5)

btn2 = tk.Button(c1, text="Disable", command=showImage1)
lbl2 = ttk.Label(c1)
btn2.grid(column=2, row=0, sticky=N, pady=5, padx=5)
lbl2.grid(column=6, row=0, sticky=N, pady=5, padx=5)





l1 = Label(root,text="Code93")
l1.grid(row=2,column=2,padx=10, pady=10)

btn3 = tk.Button(c2, text="Enable", command=showImage2)
lbl3 = ttk.Label(c2)
btn3.grid(column=0, row=2, sticky=N, pady=5, padx=5)
lbl3.grid(column=4, row=2, sticky=N, pady=5, padx=5)

btn4 = tk.Button(c3, text="Disable", command=showImage3)
lbl4 = ttk.Label(c3)
btn4.grid(column=2, row=2, sticky=N, pady=5, padx=5)
lbl4.grid(column=6, row=2, sticky=N, pady=5, padx=5)


l1 = Label(root,text="Data Matrix")
l1.grid(row=4,column=2,padx=10, pady=10)

btn5 = tk.Button(c4, text="Enable", command=showImage4)
lbl5 = ttk.Label(c4)
btn5.grid(column=0, row=4, sticky=N, pady=5, padx=5)
lbl5.grid(column=4, row=4, sticky=N, pady=5, padx=5)

btn6 = tk.Button(c5, text="Disable", command=showImage5)
lbl6 = ttk.Label(c5)
btn6.grid(column=2, row=4, sticky=N, pady=5, padx=5)
lbl6.grid(column=6, row=4, sticky=N, pady=5, padx=5)



l1 = Label(root,text="QR Code")
l1.grid(row=6,column=2,padx=10, pady=10)

btn7 = tk.Button(c6, text="Enable", command=showImage6)
lbl7 = ttk.Label(c6)
btn7.grid(column=0, row=6, sticky=N, pady=5, padx=5)
lbl7.grid(column=4, row=6, sticky=N, pady=5, padx=5)

btn8 = tk.Button(c7, text="Disable", command=showImage7)
lbl8 = ttk.Label(c7)
btn8.grid(column=2, row=6, sticky=N, pady=5, padx=5)
lbl8.grid(column=6, row=6, sticky=N, pady=5, padx=5)

lbl8 = ttk.Label(c8)
lbl8.grid(column=4, row= 8, sticky=N,pady=5,padx=5)

lbl9 = ttk.Label(creset)
lbl9.grid(column=8,row=8,sticky=N,pady=5,padx=5)



variable.trace("w", callback)



root.mainloop()