# IMAGAE-_SLIDESHOW_PROJECT
PYTHON PROJECT 
import tkinter as tk
from PIL import Image, ImageTk
from itertools import cycle
import time 
# 1. Initialize the Main Window
root = tk.Tk()
root.title("Image Slideshow App")
root.geometry("600x500")

# 2. Define Image Paths
#put your Image paths
image_paths = [
              r"C:\Users\\Desktop\newphotos\Screenshot 2026-05-24 195902.png",
              r"C:\Users\\Attachments\Desktop\newphotos\Screenshot 2026-05-24 200454.png",
              r"C:\Users\\Attachments\Desktop\newphotos\Screenshot 2026-05-24 202058.png",
              r"C:\Users\\Attachments\Desktop\newphotos\2026-06-04 at 10.36.42 PM.jpeg"
              ]

# 3. Process and Load Images using PIL
photo_images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize((500, 400), Image.Resampling.LANCZOS)
    photo_images.append(ImageTk.PhotoImage(img))

# 4. Create an Iterator for Cyclic Playback
slideshow = cycle(photo_images)

# 5. Create a Label Widget to Display Images
image_label = tk.Label(root)
image_label.pack(pady=10)

# 6. Define Functions to Control the Slideshow
def update_image():
    next_image = next(slideshow)
    image_label.config(image=next_image)
    image_label.image = next_image

def start_slideshow():
    update_image()
    # Automatically switch images every 3000 milliseconds (3 seconds)
    root.after(5000, start_slideshow)

# 7. Add a Button to Start the Slideshow
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack(pady=10)

# 8. Start the Tkinter Event Loop
root.mainloop()
