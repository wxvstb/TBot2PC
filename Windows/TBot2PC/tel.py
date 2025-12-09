import telebot
import os
from pathlib import Path
from io import BytesIO
import json
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

sys.path.append(PARENT_DIR)

from TBot2PC.path import resource_path, base_dir

python_exe = os.path.join(base_dir(), "python", "python.exe")
file_api = resource_path("api.json")
file_logo = resource_path("icon.icns")
file_st = os.path.join(base_dir(), "TBot2PC", "py.py")

with open(file_api, 'r') as file:
    data = json.load(file)
a = data["api"]
pid_m = data["pid_m"]

tok = a
bot = telebot.TeleBot(tok)    

pid = os.getpid()
data = {
        "api": a,
        "pid": pid,
        "pid_m": pid_m
    }
with open(file_api, 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


def down():
    dowd = Path.home() / 'Downloads'
    if not dowd.exists():
            dowd = Path.home() / 'Завантаження'
    return str(dowd)

def get_file_name(message):
    if message.content_type == 'photo':
        return message.photo[-1].file_id + '.jpg' 
    elif message.content_type == 'video':
        return message.video.file_id + '.mp4'
    elif message.content_type == 'document':
        return message.document.file_name

@bot.message_handler(content_types=['photo', 'video', 'document'])
def handle_file(message):
    bot.reply_to(message, f"Очікуйте файл загружається...")
    file_name = get_file_name(message)

    if message.content_type == 'photo':
        file_id = message.photo[-1].file_id 
    elif message.content_type == 'video':
        file_id = message.video.file_id 
    elif message.content_type == 'document':
        file_id = message.document.file_id 

    file_info = bot.get_file(file_id)
    file_path = file_info.file_path 

    dowd = down()

    if not os.path.exists(dowd):
        os.makedirs(dowd)

    full_file_path = os.path.join(dowd, file_name)

    dowf = bot.download_file(file_path)

    with open(full_file_path, 'wb') as new_file:
        new_file.write(dowf)

    bot.reply_to(message, f"Файл збережено в папці: {file_name}")


try:
   bot.polling()
except Exception as e:
    pid = -1
    data = {
        "api": a,
        "pid": pid
    }
    with open(file_api, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Bot stopped")
finally:
    pid = -1
    data = {
        "api": a,
        "pid": pid
    }
    with open(file_api, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Bot stopped")