from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox
import tkinter
import pyautogui
from fetch import run
import os
import sys
import glob
import os.path
import urllib.request


url = "https://altibo.000webhostapp.com/CHECK.txt"
try:
    file = urllib.request.urlopen(url)
except:
    time.sleep(1)
    file = urllib.request.urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
win = Tk()
win.iconbitmap("imgPC/ico.ico")

win.geometry("280x300")
win.minsize(280, 300)
win.maxsize(280, 300)
win.title("Beaver")
def open_prompt():
   if password.get() ==decoded_line:
        btn1['state']=tkinter.DISABLED
        btn2['state']=tkinter.ACTIVE
        messagebox.showinfo("Message", "Code is Correct")
   else:
        messagebox.showerror("Message", "Password is not correct")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()     
def Close():
    win.destroy()
def restart():
    win.destroy()
    os.startfile("run.py")
    
def runP():
    btn2['state']=tkinter.DISABLED
    for i in range(20):
        progress['value']+= 10
        win.update_idletasks()
        time.sleep(0.1)
    run()
    for i in range(20):
        progress['value']+= 10
        win.update_idletasks()
        time.sleep(0.1)
    btn2['state']=tkinter.ACTIVE
    messagebox.showinfo("Message", "DONE")
    
def del_file(path):
    files = glob.glob(f'{path}')
    for f in files:
        os.remove(f)
def opentxt():
    os.system("exe.cmd")  
def runProgram():
    if os.stat('answears.txt').st_size != 0:
        if messagebox.askokcancel("Message", "Your Answears.txt file is still full, click OK to clear it Before i start!"):
            with open("answears.txt", 'r+') as f:
                    f.truncate(0)
    if os.path.isfile('temp/an.jpg') or os.path.isfile('temp/an.png'):
        del_file("temp/*.png")
        del_file("temp/*.jpg")
        del_file("imgAn/*.png")
    runP()

Font_tuple = ("@Microsoft JhengHei Light", 13)
Label(win, text= "Click Start To run Bot",font = Font_tuple).pack(pady=(16,0))
Label(win, text= "Write Password To start!",font = Font_tuple).pack()
password = StringVar()

passwordEntry = Entry(win, textvariable=password,font=("Cursive",15,"bold"), show='*')
passwordEntry.insert(0, 'ADMIN')
passwordEntry.pack(pady=10)
btn1 = Button(win, text="CHECK",width=36, command= open_prompt)
btn1.pack()

btn2 = Button(win, text= "START",width=36, command= runProgram)
btn2.pack()
btn3 = Button(win, text= "CLOSE",width=36, command= Close)
btn3.pack(pady=3)
btn3 = Button(win, text= "RESTART",width=36, command=restart)
btn3.pack(pady=4)
btn3 = Button(win, text= "OPEN answears.txt",width=36, command=opentxt)
btn3.pack()
progress = Progressbar(win, orient = HORIZONTAL,
              length = 240, mode = 'indeterminate')
btn2['state']=tkinter.DISABLED

progress.pack(pady = 10)
win.protocol("WM_DELETE_WINDOW", on_closing)

win.mainloop()
