import os
import sys

def base_dir():
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    current = os.path.dirname(os.path.abspath(__file__))

    return os.path.dirname(current)


def resource_path(*parts):
    return os.path.join(base_dir(), "TBot2PC", "resources", *parts)
