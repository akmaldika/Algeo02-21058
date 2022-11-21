import cv2
import pickle
import numpy
import os
import time
import sys
import threading
import base64
import math
from tkinter import *
from PIL import ImageTk, Image

from covareigen import *
from eigen import *
from identification import *
from initialization import *
from mean import *
from selisih import *
from video import VideoCapture

# ---- Inisialisasi Tkinter ---- #
window = Tk()
window.title('Face Recognition')
icon = PhotoImage(file = 'src/UI/Icon.png')
window.tk.call('wm', 'iconphoto', window._w, icon)

# ---- Window ---- #
window.geometry('1080x600')
window.configure(bg = '#ffffff')
canvas = Canvas(
    window,
    bg = '#ffffff',
    width = 1080,
    height = 600,
    bd = 0,
    highlightthickness = 0,
    relief='ridge')
canvas.place(x = 0, y = 0)

# ---- Background ---- #
background_img = PhotoImage(file = 'src/UI/Background.png')
background = canvas.create_image(
    540.0, 300.0,
    image = background_img)

# ---- Button Choose Dataset ---- #
choosedataset_img = PhotoImage(file = 'src/UI/Button1.png')
choosedataset_button = Button(
    # command = lambda: select_dataset(),
    image = choosedataset_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat')

choosedataset_button.place(
    x = 100, y = 185,
    width = 160,
    height = 50)

# ---- Button Choose Image ---- #
chooseimage_img = PhotoImage(file = 'src/UI/Button1.png')
chooseimage_button = Button(
    # command=lambda: select_image(),
    image = chooseimage_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat')

chooseimage_button.place(
    x = 100, y = 339,
    width = 160,
    height = 50)

# ---- Button Start ---- #
start_img = PhotoImage(file = 'src/UI/Button2.png')
start_button = Button(
    # command=lambda: start_thread(),
    image = start_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat')

start_button.place(
    x = 100, y = 460,
    width = 160,
    height = 50)

# ---- Button Start/Stop Video ---- #
startvideo_img = PhotoImage(file = 'src/UI/Button3.png')
stopvideo_img = PhotoImage(file = 'src/UI/Button4.png')
startstop_button = Button(
    # command=lambda: threading.Thread(target=start_video, daemon=True).start(),
    image = startvideo_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat')

startstop_button.place(
    x = 100, y = 522.5,
    width = 160,
    height = 50)

# ---- Entry Dataset ---- #
entrydataset_img = PhotoImage(file = 'src/UI/TextBox2semilong.png')
entrydataset_entry = canvas.create_image(
    180, 260.0,
    image = entrydataset_img)

entry_dataset = Entry(
    bd = 0,
    bg = '#5878e5',
    highlightthickness = 0,
    font = ('Montserrat 10 bold'),
    fg = '#ffffff',
    justify = 'center')

entry_dataset.bind('<Button-1>', lambda e: 'break')

entry_dataset.place(
    x = 115.0, y = 247.5,
    width = 130.0,
    height = 25)

# ---- Entry Image ---- #
entryimage_img = PhotoImage(file = 'src/UI/TextBox2semilong.png')
entryimage_entry = canvas.create_image(
    180.0, 415.0,
    image = entryimage_img)

entry_image = Entry(
    bd = 0,
    bg = '#5878e5',
    highlightthickness = 0,
    font = ('Montserrat 10 bold'),
    fg = '#ffffff',
    justify = 'center')

entry_image.bind('<Button-1>', lambda e: 'break')

entry_image.place(
    x = 115.0, y = 402.5,
    width = 130.0,
    height = 25)

# ---- Entry Checking ---- #
def check_entry():
    var1 = entry_dataset.get()
    var2 = entry_image.get()
    if var1 == '':
        entry_dataset.insert(0, 'No File Chosen')
    if var2 == '':
        entry_image.insert(0, 'No File Chosen')

check_entry()

# ---- Label Time ---- #
time_label_img = PhotoImage(file = 'src/UI/TextBox2Short.png')
time_label_bg = canvas.create_image(
    482.5, 500.0,
    image = time_label_img)

time_label = Label(
    bd = 0,
    bg = "#5878e5",
    highlightthickness = 0,
    font = ('Montserrat 20 bold'),
    fg = '#ffffff',
    justify = 'center')

time_label.bind('<Button-1>', lambda e: 'break')

time_label.place(
    x = 410.0, y = 475.0,
    width = 150.0,
    height = 50)

# ---- Label Status ---- #
status_label_img = PhotoImage(file = 'src/UI/TextBox2Short.png')
status_label_bg = canvas.create_image(
    821.0, 553.5,
    image=status_label_img)

status_label = Label(
    bd = 0,
    bg = "#5878e5",
    highlightthickness = 0,
    font = ('Montserrat 20 bold'),
    fg = '#ffffff',
    justify = 'center')

status_label.bind('<Button-1>', lambda e: 'break')

status_label.place(
    x = 745.0, y = 528.5,
    width = 150.0,
    height = 50)

# ---- Label Result ---- #
result_label_img = PhotoImage(file = 'src/UI/TextBox2Long.png')
result_label_bg = canvas.create_image(
    876.5, 486.0,
    image = result_label_img)

result_label = Label(
    bd = 0,
    bg = "#5878e5",
    highlightthickness = 0,
    font = ('Montserrat 10 bold'),
    fg = '#ffffff',
    justify = 'center')

result_label.bind('<Button-1>', lambda e: 'break')

result_label.place(
    x=745, y=475,
    width=265,
    height=25)

# ---- Left Image ---- #
left_img_label = Label()
left_img_label.place(
    x = 400, y = 170,
    anchor = NW, width = 276, height = 276)

left_img_bg = PhotoImage(file = 'src/UI/ImageBackground.png')
left_img_label.config(image = left_img_bg)
left_img_label.image = left_img_bg

canvas.pack()

# window.protocol("WM_DELETE_WINDOW", on_window_close)
window.resizable(False, False)
window.mainloop()