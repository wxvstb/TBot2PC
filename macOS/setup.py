from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('resources', ['resources/icon.icns', 'resources/icon5.png', 'resources/icon_on.png', 'resources/api.json']),
]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'resources/icon.icns',
    'packages': ['rumps', 'pydub', 'psutil', 'anyio', 'telebot', 'tkinter', "os", "ttkthemes"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
