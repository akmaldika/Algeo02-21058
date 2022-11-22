import time
import sys
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

from initialization import *
from mean import *
from selisih import *
from covariance import *
from eigen import *
from identification import *
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
    command = lambda: threading.Thread(target = start_video, daemon=True).start(),
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
    x=745, y=473,
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

# ---- Right Image ---- #
right_img_label = Label()
right_img_label.place(
    x = 739, y = 170,
    anchor = NW, width = 276, height = 276)

right_img_bg = PhotoImage(file = 'src/UI/ImageBackground.png')
right_img_label.config(image = right_img_bg)
right_img_label.image = right_img_bg

canvas.pack()

# ---- Inisialisasi ---- #
processing = False
processing_video = False
db_updated = False

t1 = None
eigenvector = None
saved_pathdataset = None
saved_totalImage = None
pathdataset = None
imageInput = None

video_capture = VideoCapture()

# ---- Fungsi Utama ---- #
def resize(image):
    width, height = image.shape[1], image.shape[0]

    if (width > height):
        start_row = 0
        end_row = height

        start_col = (width - height) / 2
        end_col = width - start_col
    else:
        max = width
        start_row = (height - width) / 2
        end_row = height - start_row

        start_col = 0
        end_col = width

    crop_img = image[int(start_row):int(end_row), int(start_col):int(end_col)]

    dim = (276, 276)

    if (crop_img.shape[0] < 276):
        resized_image = cv2.resize(crop_img, dim, interpolation=cv2.INTER_CUBIC)
    else:
        resized_image = cv2.resize(crop_img, dim, interpolation=cv2.INTER_AREA)

    return resized_image

def select_dataset():
    if processing or processing_video:
        return
        
    global pathdataset, t1

    pathdataset = filedialog.askdirectory()

    if (len(pathdataset) != 0):
        current = entry_dataset.get()
        entry_dataset.delete(0, END)
        entry_dataset.insert(0, os.path.basename(pathdataset))
    else:
        check_entry()

    t1 = threading.Thread(target=update_dataset, daemon=True)
    t1.start()

def update_dataset():
    global pathdataset, imageInput, eigenvector, saved_pathdataset, saved_totalImage, db_updated

    if ((pathdataset != saved_pathdataset) or (saved_totalImage != totalImage(pathdataset))):
        db_updated = False

    if not db_updated:
        update_status('Updating')
        saved_pathdataset = pathdataset
        saved_totalImage = totalImage(pathdataset)
        updateDatabase(pathdataset)
        selisih(pathdataset)
        covmat, diffmat = getCovariance(pathdataset)
        # Opsi 1
        Q, R = getQR(covmat)
        eigenvector = np.dot(diffmat, Q)
        # Opsi 2
        # eigenvector = getEigen(covmat, diffmat)
        # besteigenvector = pickEigen(eigenvector)
        CalculateEigenface(eigenvector)
        db_updated = True
        update_status('Updated')

def select_image():
    if processing or processing_video:
        return

    global image, imageInput

    path = filedialog.askopenfilename()

    entry_image.delete(0, END)
    entry_image.insert(0, os.path.basename(path))

    if len(path) > 0:
        image = cv2.imread(path)

        resized_image = resize(image)

        image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)

        image = ImageTk.PhotoImage(image)

        left_img_label.configure(image = image)
        left_img_label.image = image

        imageInput = readImage(path)
    else:
        check_entry()

def update_status(status):
    status_label.config(text=status)

def stopwatch():
    start = time.time()
    while processing:
        time_label.config(text=f"{(time.time() - start):.4f}s")

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

def stop_video():
    global processing_video, imageInput
    processing_video = False
    video_capture.stop()
    startstop_button.config(
        command = lambda: threading.Thread(
        target = start_video, daemon = True).start(), image = startvideo_img)
    left_img_bg = PhotoImage(file = 'src/UI/ImageBackground.png')
    left_img_label.config(image = left_img_bg)
    left_img_label.image = left_img_bg
    imageInput = None
    update_status('')
    result_label.config(text = '')

def start_video():
    if pathdataset is None:
        messagebox.showerror("Error", "Please choose dataset first")
        return
    entry_image.delete(0, END)
    check_entry()

    global video_capture, image, imageInput, processing_video, processing

    startstop_button.config(command = stop_video, image = stopvideo_img)
    t1.join()
    update_status('Starting')
    video_capture.start()
    processing_video = True
    start_time = time.time()

    while processing_video:
        ret, frame = video_capture.get_image()
        if not ret:
            break
        resized_image = resize(frame)
        countdown = math.ceil(3 - (time.time() - start_time))
        if countdown:
            update_status('Capturing')
            cv2.putText(resized_image, str(countdown),
                        (125, 155), cv2.FONT_HERSHEY_SIMPLEX, 2, (275, 275, 275), 2)
        else:
            camera_cache_path = 'src/Database/cameraCache.jpg'
            if os.path.exists(camera_cache_path):
                os.remove(camera_cache_path)
            cv2.imwrite(camera_cache_path, resized_image)
            imageInput = readImage(camera_cache_path)

        frame = Image.fromarray(resized_image)
        image = ImageTk.PhotoImage(frame)
        left_img_label.configure(image=image)
        left_img_label.image = image

        if not countdown:
            processing = True
            threading.Thread(target = stopwatch, daemon = True).start()
            update_status('Processing')
            start()
            start_time = time.time()

    video_capture.stop()

def start():
    global processing, t1, pathdataset, imageInput, eigenvector, saved_pathdataset, saved_totalImage, db_updated
    
    t1.join()

    t1 = threading.Thread(target=update_dataset, daemon=True)
    t1.start()
    t1.join()

    update_status('Processing')

    closest_image_path, distance = getNewEigenface(imageInput, pathdataset, eigenvector)

    print('Result:', closest_image_path)
    print('Distance:', distance, '\n')
    
    processing = False

    if (closest_image_path == None):
        result_label.config(text = 'Tidak ada gambar yang cocok')
        right_img_bg = PhotoImage(file = 'src/UI/ImageBackground.png')
        right_img_label.config(image = right_img_bg)
        right_img_label.image = right_img_bg
    else:
        result_label.config(text = os.path.basename(closest_image_path))
        image = cv2.imread(closest_image_path)
        resized_image = resize(image)
        image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        right_img_label.configure(image = image)
        right_img_label.image = image

    update_status('Done')

def close():
    global processing_video
    processing_video = False
    window.destroy()
    sys.exit()

window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()