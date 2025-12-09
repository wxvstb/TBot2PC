import os
import sys
import subprocess

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
si.wShowWindow = 0

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
PYTHON_EXE = os.path.join(BASE_DIR, "python", "python.exe")
MAIN_SCRIPT = os.path.join(BASE_DIR, "TBot2PC", "main.py")

subprocess.Popen([PYTHON_EXE, MAIN_SCRIPT], startupinfo=si)
