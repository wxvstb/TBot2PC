from tkinter import *
import json
import sys, subprocess
import psutil


root = Tk()
root.title("Setting")
root.geometry('450x250')

def b_cl():
    with open('resources/api.json', 'r') as file:
        data = json.load(file)
    pid = data["pid"]
    a = e.get()
    data = {
        "api": a,
        "pid": pid
    }
    with open('resources/api.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    err.config(text="API saved", fg='green')
    err.place(x=190, y=155)

def start_p():
    with open('resources/api.json', 'r') as file:
        data = json.load(file)
    appo = data["api"]
    if appo == "":
        err.config(text="Error API", fg='red')
        err.place(x=190, y=155)
    else:
        err.config(text="Successfuly start", fg='green')
        err.place(x=172, y=155)
        subprocess.Popen([sys.executable, 'tel.py'])

def ch_d():
    
    with open('resources/api.json', 'r') as file:
        data = json.load(file)
    pid = data["pid"]
    api = data["api"]
    if pid == -1:
        err.config(text="Nothing to stop", fg='red')
        err.place(x=175, y=155)
    else:
        err.config(text="Bot is stopped", fg='green')
        err.place(x=172, y=155)
        p = psutil.Process(pid)
        p.terminate()
    data = {
        "api": api,
        "pid": -1
    }
    with open('resources/api.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    

err = Label(text='', fg='red')
err.place(x=190, y=155)
e = Entry(root, width=40)
e.place(x=40, y=80)
sava = Button(root, text="Save API", command=b_cl, width=30)
sava.place(x=90, y=110)
b = Button(root, text='Start', command=start_p)
b.place(x=90, y=150)
stop = Button(root, text="Stop", command=ch_d)
stop.place(x=320, y=150)
texts = Label(text="Paste your Telegram API")
texts.place(x=150, y=50)


root.mainloop()