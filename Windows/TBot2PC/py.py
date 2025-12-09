from tkinter import *
import json
import sys, subprocess
import psutil
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

sys.path.append(PARENT_DIR)

from TBot2PC.path import resource_path, base_dir

python_exe = os.path.join(base_dir(), "python", "python.exe")
file_api = resource_path("api.json")
file_logo = resource_path("icon.icns")
file_st = os.path.join(base_dir(), "TBot2PC", "tel.py")
file_logo = os.path.join(base_dir(), "TBot2PC", "resources", "icon2.ico")

root = Tk()
root.title("TBot2PC Setting")
root.geometry('450x250')
root.iconbitmap(True, file_logo)

def b_cl():
    with open(file_api, 'r') as file:
        data = json.load(file)
    pid = data["pid"]
    a = e.get()
    data = {
        "api": a,
        "pid": pid
    }
    with open(file_api, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    err.config(text="API saved", fg='green')
    err.place(x=190, y=155)

def start_p():
    with open(file_api, 'r') as file:
        data = json.load(file)
    appo = data["api"]
    if appo == "":
        err.config(text="Error API", fg='red')
        err.place(x=190, y=155)
    else:
        err.config(text="Successfuly start", fg='green')
        err.place(x=172, y=155)
        subprocess.Popen([python_exe, file_st])

def ch_d():
    
    with open(file_api, 'r') as file:
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
    with open(file_api, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    

err = Label(text='', fg='red')
err.place(x=190, y=155)
e = Entry(root, width=40)
e.place(x=102, y=80)
sava = Button(root, text="Save API", command=b_cl, width=33)
sava.place(x=102, y=110)
b = Button(root, text='Start', command=start_p)
b.place(x=102, y=150)
stop = Button(root, text="Stop", command=ch_d)
stop.place(x=309, y=150)
texts = Label(text="Paste your Telegram API", width=30)
texts.place(x=120, y=50)

try:
   root.mainloop()
except Exception as e:
    print("Error:", e)
    