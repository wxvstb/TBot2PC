import telebot
import os
from pathlib import Path
from pydub import AudioSegment
from io import BytesIO
import json


with open('Resources/api.json', 'r') as file:
    data = json.load(file)
a = data["api"]

tok = a
bot = telebot.TeleBot(tok)    

pid = os.getpid()
data = {
        "api": a,
        "pid": pid
    }
with open('Resources/api.json', 'w') as file:
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

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    file_id = message.voice.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    dowd = down()

    if not os.path.exists(dowd):
        os.makedirs(dowd)

    dowf = bot.download_file(file_path)

    audio = AudioSegment.from_ogg(BytesIO(dowf))

    file_name = file_path.split('/')[-1].replace('.oga', '.mp3')
    full_file_path = os.path.join(dowd, file_name)

    audio.export(full_file_path, format="mp3")

    bot.reply_to(message, f"Голосове повідомлення збережено в папці: {full_file_path}")
 
bot.polling()