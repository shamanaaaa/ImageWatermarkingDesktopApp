from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import convert

gui = Tk()
gui.geometry("500x400")
gui.title("WATERMARK IMAGES")


def getFolderPath():
    folder_selected = filedialog.askdirectory()
    folderPath.set(folder_selected)


def get_images():
    images = filedialog.askopenfilenames()
    for item in images:
        all_images.append(item)


def run():
    watermark_count = int(e1.get())
    watermark_size = int(e2.get())
    for image in all_images:
        convert.image_converter(image, folderPath.get(), watermark_count, watermark_size)


folderPath = StringVar()
all_images = []
a = Label(gui, text="Destination folder")
a.grid(row=1, column=0)
E = Entry(gui, textvariable=folderPath)
E.grid(row=1, column=1)
browse_button = ttk.Button(gui, text="Browse", command=getFolderPath)
browse_button.grid(row=1, column=2)
s = Label(gui, text="Select photos")
s.grid(row=0, column=0)
select_photos = ttk.Button(gui, text="Browse", command=get_images)
select_photos.grid(row=0, column=2)
ttk.Label(gui, text="Watermark count").grid(row=3)
ttk.Label(gui, text="Watermark size").grid(row=4)
e1 = ttk.Entry(gui)
e1.insert(END, '4')
e2 = ttk.Entry(gui)
e2.insert(END, '40')
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)
run_btn = ttk.Button(gui, text="RUN", command=run)
run_btn.grid(row=5, column=1)
gui.mainloop()
