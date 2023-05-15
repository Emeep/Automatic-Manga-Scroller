import tkinter as tk
from PIL import ImageTk, Image
import os

import easyocr

import sys
sys.path.insert(0, '') # Full path to MangaScroller folder
import scrape # import functions of scrape.py

path = 'MangaScroller\\Images'

chapter = 7 # no. chapter u want to start reading 

winwidth = 1000 # horizontal pixels
fontsize = 20
timeperword = 0.5 # seconds

# tkinter win init
root = tk.Tk()
frame = tk.Frame(root, width=300, height=300)
page = tk.Label(frame, fg="black", font=("Helvetica", fontsize))
timer = tk.Label(frame, fg="black", font=("Helvetica", fontsize))

while True:
    url = f'https://www.shounenabyss.com/manga/boys-abyss-chapter-{chapter}/' # URL of manga site

    try: scrape.delete_images(path)
    except: continue

    scrape.main(url, path)
    
    for image in os.listdir(path):
        imgpath = f'{path}\\{image}'
        img = Image.open(imgpath)
        zoom_percent = winwidth / img.size[0]
        tkimg = ImageTk.PhotoImage(img.resize(tuple(int(i * zoom_percent) for i in img.size)))
        width, height = tkimg.width(), tkimg.height()
        root.geometry(f'{width}x{height + fontsize * 4}')

        imgLabel = tk.Label(root, image=tkimg)
        imgLabel.place(anchor='n', relx=0.5, y=fontsize * 3)

        frame.place(anchor='n', relx=0.5, y=5)

        page.config(text=f'ch {chapter} | {image} | time remaining:')
        page.pack(side='left')

        reader = easyocr.Reader(['en']).readtext(imgpath, detail=0)
        read_time = int(len(reader) * timeperword)

        for i in range(read_time):
            timer.config(text=f'{read_time - i}')
            timer.pack(side='left')
            root.after(1000, root.update())

    chapter += 1
    
