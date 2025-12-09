import pystray
from PIL import Image
import os
import sys, subprocess
import json
import psutil

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
si.wShowWindow = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

sys.path.append(PARENT_DIR)

from TBot2PC.path import resource_path, base_dir

python_exe = os.path.join(base_dir(), "python", "python.exe")
file_api = resource_path("api.json")
file_logo = resource_path("icon.icns")
file_st = os.path.join(base_dir(), "TBot2PC", "py.py")
file_tg = os.path.join(base_dir(), "TBot2PC", "tel.py")

state = {"enabled": False}

with open(file_api, 'r') as file:
    data = json.load(file)
pid = data["pid"]
pid_m = data["pid_m"]


if psutil.pid_exists(pid):
   print("ok")
else:
    pid = -1
    data["pid"] = -1
    with open(file_api, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
    state["enabled"] = False

if pid != -1:
    state["enabled"] = True


def toggle(icon, item):
    with open(file_api, 'r') as file:
        data = json.load(file)
    pid = data["pid"]
    if state["enabled"] == False:
        state["enabled"] = True
        if pid == -1:
            subprocess.Popen([python_exe, file_tg], startupinfo=si)
    else:
        print("exit")
        if pid != -1:
            p = psutil.Process(pid)
            p.terminate()
            pid = -1
            data["pid"] = -1
            with open(file_api, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            state["enabled"] = False

def settings(icon, item):
    subprocess.Popen([python_exe, file_st])

def exit_app(icon, item):
    with open(file_api, 'r') as file:
         data = json.load(file)
    pid = data["pid"]
    if psutil.pid_exists(pid):
        p = psutil.Process(pid)
        p.terminate()
        pid = -1
        data["pid"] = -1
        data["pid_m"] = -1
        with open(file_api, "w", encoding="utf-8") as file:
             json.dump(data, file, ensure_ascii=False, indent=4)
        state["enabled"] = False
    data["pid_m"] = -1
    with open(file_api, "w", encoding="utf-8") as file:
             json.dump(data, file, ensure_ascii=False, indent=4)
    icon.stop()

icon_path = os.path.join(os.path.dirname(__file__), file_logo)
image = Image.open(icon_path)

icon = pystray.Icon(
    "app",
    icon=image,
    title="TBot2PC",
    menu=pystray.Menu(
        pystray.MenuItem("Toggle", toggle, checked=lambda item: state["enabled"]),
        pystray.MenuItem("Settings", settings),
        pystray.MenuItem("Exit", exit_app)
    )
)

if psutil.pid_exists(pid_m):
    exit_app(icon, None)
    print("yes")
else:
    pid_m = os.getpid()
    data["pid_m"] = pid_m
    with open(file_api, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
    print("Running...")
    icon.run()


