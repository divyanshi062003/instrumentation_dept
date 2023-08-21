import tkinter as tk
from tkinter import*
import customtkinter
from PIL import ImageTk, Image
import mysql.connector
window= Tk()
window.geometry("655x333")
window.title("Inventory/Stock Control")



f0= Frame(window, borderwidth=6, bg="grey", relief=SUNKEN)
f0.pack(side=TOP, fill="x")

l0=Label(f0, text="Inventory/Stock Control", font="helvetica 16")
l0.pack(padx=10, pady=10)

f1= Frame(window, borderwidth=6, bg="blue", relief=SUNKEN)
f1.pack(side=TOP, fill="x")
l1a=Label(f1, text="Department - Instrumentation")
l1a.pack(side=LEFT, padx=5, pady=5)
l1b=Label(f1, text="Section - CO & CCO")
l1b.pack(side=RIGHT, padx=5, pady=5)

f2=Frame(window, borderwidth=6 )
f2.pack(side=TOP, fill="x")
img = ImageTk.PhotoImage(Image.open("coke-oven2png.png"))
label = Label(f2, image = img)
label.pack(side=LEFT)
img3 = ImageTk.PhotoImage(Image.open("BSP.jpg"))
label3= Label(f2, image = img3)
label3.pack(side=LEFT)
img2 = ImageTk.PhotoImage(Image.open("coke-ovenpng.png"))
label2= Label(f2, image = img2)
label2.pack(side=LEFT)




window.mainloop()