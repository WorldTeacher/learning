import tkinter as tk
from tkinter import *
import PyPDF2
import glob
from PIL import Image, ImageTk
#setting variables
imagefile=r"J:\GitHub\learning\Python\python gui scripts\testing\img.png"
root = tk.Tk()
canvas= tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
#load logo
logo=Image.open(imagefile)
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.grid(column=1, row=0)

#instruction 
instruction=tk.Label(root, text="select the pdf file you want to extract the content from")
instruction.grid(columnspan=3, row=1)

#browse button
browse_text=tk.StringVar()
browse_button=tk.Button(root, textvariable="browse text", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse Text")
browse_button.grid(column=1, row=2)
#gui
root.mainloop()

