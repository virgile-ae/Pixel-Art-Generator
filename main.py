from PIL import Image
import tkinter as tk
from tkinter import filedialog

input_file_path = ""
input_quality = 1

img = 0

output = 0
output_path = ""

def pixelize():
    (imageW, imageH) = img.size
    quality = input_quality/100
    width, height = int(imageW * quality), int(imageH * quality)
    global output
    output = img.resize((width, height), Image.BILINEAR).resize((imageW, imageH), Image.BOX)

def input_photo():
    global input_file_path
    input_file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Images", "*.png *.jpg *.gif *.jpeg *.bmp"), ("All files", "*.*")))
    global img
    img = Image.open(input_file_path)

def save_image():
    pixelize()
    global output_path
    output_path = filedialog.askdirectory(initialdir="/", title="Select a folder")
    output.save(f"{output_path}/pixel_art.{img.format.lower()}", img.format)

def show_state():
    pixelize()
    output.show()

def set_quality(newq):
    global input_quality
    input_quality = int(newq)

# INIT
win = tk.Tk()
win.title("Pixel Art Generator")

# WRAPPER
frame = tk.Frame(win)
frame.pack(padx=20, pady=20)

# RESOLUTION PICKER
scale = tk.Scale(frame, from_=1, to=100, orient=tk.HORIZONTAL, command=set_quality, length=400, label="Quality of image")

# FILE PICKER
button_explore = tk.Button(frame, text="Choose image", command=input_photo)

# DIRECTORY PICKER
dir_explore = tk.Button(frame, text="Save pixel art", command=save_image)

# PREVIEW
preview = tk.Button(frame, text="Preview", command=show_state)

# INSTRUCTIONS
instruct= tk.Label(frame, text="Hello!\nThis is a pixel art generator that I made because I didn't want to do revision.\nTo use it, choose a photo that you want to pixelize, adjust the quality of the pixel art using the preview if you need to and then save your image.")

instruct.pack()
scale.pack()
button_explore.pack(ipadx=10, ipady=10, pady=5)
preview.pack(ipadx=10, ipady=10, pady=5)
dir_explore.pack(ipadx=10, ipady=10, pady=5)

frame.mainloop()