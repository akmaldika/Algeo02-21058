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
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

from covariance import getCovariance
from eigen import getEigen, CalculateEigenface
from identification import *
from initialization import *
from mean import *
from selisih import *
from video import VideoCapture

# ---- Inisialisasi Tkinter ---- #
window = Tk()
window.title('Face Recognition by Face-X')
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
    command = lambda: select_dataset(),
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
    command = lambda: select_image(),
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
    command = lambda: start_process(),
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
    x = 410.0, y = 473.0,
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
    font = ('Montserrat 15 bold'),
    fg = '#ffffff',
    justify = 'center')

status_label.bind('<Button-1>', lambda e: 'break')

status_label.place(
    x = 745.0, y = 526.5,
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

# ---- Inisialisasi ---- #
processing = False
processing_video = False
db_updated = False

saved_pathdataset = None
saved_totalImage = None
pathdataset = None
imageInput = None

# ---- Fungsi Utama ---- #
def select_dataset():
    if processing or processing_video:
        return
        
    global pathdataset

    pathdataset = filedialog.askdirectory()

    if (len(pathdataset) != 0):
        current = entry_dataset.get()
        entry_dataset.delete(0, END)
        entry_dataset.insert(0, os.path.basename(pathdataset))
    else:
        check_entry()

def select_image():
    if processing or processing_video:
        return

    global image, imageInput

    path = filedialog.askopenfilename()

    current = entry_image.get()
    entry_image.delete(0, END)
    entry_image.insert(0, os.path.basename(path))

    if len(path) > 0:
        imageInput = readImage(path)

        image = Image.open(path)

        resized_image = image.resize((276, 276), Image.Resampling.LANCZOS)

        image = ImageTk.PhotoImage(resized_image)

        left_img_label.configure(image = image)
        left_img_label.image = image
    else:
        check_entry()

def update_status(status):
    status_label.config(text=status)

def stopwatch():
    start = time.time()
    while processing:
        time_label.config(text=f"{(time.time() - start):.2f}s")

def start_process():
    global processing
    if processing or processing_video:
        return
    if pathdataset is None or imageInput is None:
        messagebox.showerror("Error", "Please select dataset and image")
        return
    processing = True
    threading.Thread(target=start, daemon=True).start()
    threading.Thread(target=stopwatch, daemon=True).start()
    update_status('Processing')

def start():
    global processing, saved_pathdataset, saved_totalImage, db_updated

    if ((pathdataset != saved_pathdataset) and (saved_totalImage != totalImage(pathdataset))):
        db_updated = False

    if not db_updated:
        saved_pathdataset = pathdataset
        saved_totalImage = totalImage(pathdataset)
        updateDatabase(pathdataset)
        selisih(pathdataset)
        covmat, diffmat = getCovariance(pathdataset)
        eigenvector, eigenvalue = getEigen(covmat, diffmat)
        print(eigenvector)
        db_updated = True

    processing = False
    update_status('Done')

def close():
    global processing_video
    processing_video = False
    window.destroy()
    sys.exit()

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()