import os
import shutil
import datetime

def move_to_dir(filetype, dir):
    if f".{filetype}" in filename:
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.move(filename, dir)

while True:
    today = datetime.datetime.today()
    today = str(today)
    current_hour = today[11:13]
    current_minute = today[14:16]
    current_sec = today[17:19]

    if current_hour == '08' and current_minute == '00' and current_sec == '00':
        os.chdir('/home/wleklinski/Downloads/')
        files = os.listdir(os.getcwd())

        for filename in files:
            if not os.path.isdir(filename):

                move_to_dir('mp3', 'Audio')
                move_to_dir('mp4', 'Video')
                move_to_dir('pdf', 'PDF')
                move_to_dir('jpg', 'Pictures')
                move_to_dir('jpeg', 'Pictures')
                move_to_dir('png', 'Pictures')
                move_to_dir('docx', 'Word File')
                move_to_dir('xlsx', 'Excel')
