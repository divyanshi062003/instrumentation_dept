import tkinter as tk
from tkinter import*
from tkinter import ttk
import customtkinter
from PIL import ImageTk, Image
import mysql.connector
window= Tk()
window.geometry("655x333")
window.title("Inventory/Stock Control")


#update the list
def update(data):
    my_list.delete(0,END)
    for item in data:
        my_list.insert(END,item)

def fillout(event):
    selected_index = my_list.curselection()
    if selected_index:
        selected_option = my_list.get(selected_index)
        open_new_page(selected_option)

def check(event):
    search_text = my_entry.get().lower()
    my_list.delete(0, tk.END)
    for instrument in instruments:
        if search_text in instrument.lower():
            my_list.insert(tk.END, instrument)

#function to open new page
def open_new_page(selected_option):
    new_window = tk.Toplevel(window)
    new_window.title("RECORD")

    #################
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@123",
        database="instrumentation"
    )
    cursor = conn.cursor()
    query = f"SELECT * FROM RECORD WHERE Name = '{selected_option}'"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()

    # Display records
    if records:
        tree = ttk.Treeview(new_window, columns=("S_No", "Company_Name", "Modes", "VCS_Code","Avail_Qty", "Size", "Requirement", "Location", "Received_Date", "Issued_Date", "Range", "Name"), show="headings")
        tree.pack(padx=20, pady=20, fill="both", expand=True)

        # Define column headings
        tree.heading("#1", text="S_No")
        tree.heading("#2", text="Company_Name")
        tree.heading("#3", text="Modes")
        tree.heading("#4", text="VCS_Code")
        tree.heading("#5", text="Avail_Qty")
        tree.heading("#6", text="Size")
        tree.heading("#7", text="Requirement")
        tree.heading("#8", text="Location")
        tree.heading("#9", text="Received_Date")
        tree.heading("#10", text="Issued_Date")
        tree.heading("#11", text= "Range")
        tree.heading("#12", text="Name")

        tree.column("#1", width=20)
        tree.column("#2", width=20)
        tree.column("#3", width=20)
        tree.column("#4", width=20)
        tree.column("#5", width=20)
        tree.column("#6", width=20)
        tree.column("#7", width=20)
        tree.column("#8", width=20)
        tree.column("#9", width=20)
        tree.column("#10", width=20)
        tree.column("#11", width=20)
        tree.column("#12", width=20)

        # Populate the Treeview with records
        for record in records:
            tree.insert("", tk.END, values=record)

    save_button = tk.Button(new_window, text="Save")
    save_button.pack(pady=10)
    
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)


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


my_label=Label(window,text="Search Bar",font=("Helvetica",14),fg="grey")
my_label.pack(pady=20)
my_entry=Entry(window,font=("Helvetica",20))
my_entry.pack()
my_list=Listbox(window,width=50)
my_list.pack(pady=40)
instruments=["rod","plate","battery","actuator","transmitter","battery 1"]
update(instruments)
my_list.bind("<<ListboxSelect>>",fillout)

#create a binding on the entry box
my_entry.bind("<KeyRelease>", check)



# Start the application
window.mainloop()
