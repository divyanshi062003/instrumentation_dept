import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter.tix import Tree
import customtkinter
from PIL import ImageTk, Image
import mysql.connector
import datetime
from tkinter import messagebox, filedialog
import pandas as pd
from tkinter import END
import tkinter.font as font
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


window= Tk()
#window.geometry("925x500+300+200")
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()
#window.geometry("%dx%d" % (width, height+70))
window.geometry("{}x{}+0+0". format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Inventory/Stock Control")
global tree

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

def update_label():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    l2a.config(text=formatted_datetime)
    # Schedule the function to run again after 1000 milliseconds (1 second)
    window.after(1000, update_label)


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

        def viewrec():
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql@123",
            database="instrumentation")
            cursor = conn.cursor()
            query2=f"select* from record;"
            cursor.execute(query2)
            allrecord=cursor.fetchall()
            cursor.close()
            conn.close()
            if allrecord:
                tree2 = ttk.Treeview(new_window, columns=("S_No", "Company_Name", "Modes", "VCS_Code","Avail_Qty", "Size", "Requirement", "Location", "Received_Date", "Issued_Date", "Range", "Name"), show="headings")
                tree2.pack(padx=20, pady=20, fill="both", expand=True)

                # Define column headings
                tree2.heading("#1", text="S_No")
                tree2.heading("#2", text="Company_Name")
                tree2.heading("#3", text="Modes")
                tree2.heading("#4", text="VCS_Code")
                tree2.heading("#5", text="Avail_Qty")
                tree2.heading("#6", text="Size")
                tree2.heading("#7", text="Requirement")
                tree2.heading("#8", text="Location")
                tree2.heading("#9", text="Received_Date")
                tree2.heading("#10", text="Issued_Date")
                tree2.heading("#11", text= "Range")
                tree2.heading("#12", text="Name")

                tree2.column("#1", width=20)
                tree2.column("#2", width=20)
                tree2.column("#3", width=20)
                tree2.column("#4", width=20)
                tree2.column("#5", width=20)
                tree2.column("#6", width=20)
                tree2.column("#7", width=20)
                tree2.column("#8", width=20)
                tree2.column("#9", width=20)
                tree2.column("#10", width=20)
                tree2.column("#11", width=20)
                tree2.column("#12", width=20)

                # Populate the Treeview with records
                for record in allrecord:
                    tree2.insert("", tk.END, values=record)
                def fun1():
                    if tree2:
                        tree2.destroy()
                def fun2():
                    closerec_button.destroy()

                closerec_button = tk.Button(new_window, text="Close Full Record", command=lambda: [fun1(), fun2()])
                closerec_button.pack(pady=20)
                
                
        def upload_excel():
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mysql@123",
            database="instrumentation")
            cursor = conn.cursor()
            file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx;.xls")])
            if file_path:
                try:
                    cursor.execute("SELECT * FROM record")
                    existing_records = [str(row[0]) for row in cursor.fetchall()]
                    df = pd.read_excel(file_path)

                    # Check if the number of columns in the DataFrame matches the expected number
                    expected_columns = ["S_No", "Company_Name", "Modes", "VCS_Code", "Avail_Qty", "Size", "Requirement",
                                "Location", "Received_Date", "Issued_Date", "Range", "Name"]
                    if len(df.columns) != len(expected_columns):
                        messagebox.showerror("Error", "Column count in the Excel file does not match the expected count. Choose the correct file to upload.")
                        return
                    length = len(df)

                    # Iterate through the DataFrame and insert data into the table
                    for i in range(length):
                        # Convert each record to a tuple
                        rec = tuple(df.loc[i].fillna('null'))
                        print("Record fetch successfull",rec[0:11])
                        if str(rec[0]) in existing_records:
                            messagebox.showerror(f"Record with ID {rec[0]} already exists in the database.")
                            return
                        else:
                            # Create SQL INSERT statement
                            sqlSentence = f"INSERT INTO record VALUES {rec};"
                    
                            # Replace 'nan', 'None', 'none' with 'null'
                            sqlSentence = sqlSentence.replace("'nan'", 'null').replace("'None'", 'null').replace("'none'", 'null')

                            # Execute the SQL statement
                            cursor.execute(sqlSentence)
                        
                    conn.commit()

                except Exception as e:
                        messagebox.showerror("Error", f"Failed to read/insert Excel data: {str(e)}")
                finally:
                        cursor.close()
                        conn.close()

        
    
    fr1= Frame(new_window, borderwidth=6, width=500, bg="LightSkyBlue2")
    fr1.pack(side=RIGHT, fill="y")
    update_button = tk.Button(fr1, text="Update by Uploading Excel File", command=upload_excel)
    update_button.pack(pady=30)

    viewrec_button = tk.Button(fr1, text="View Record of all instruments", command=viewrec)
    viewrec_button.pack(pady=20)

    save_button = tk.Button(fr1, text="Save")
    save_button.pack(pady=10)
    
    close_button = tk.Button(fr1, text="Close", command=new_window.destroy)
    close_button.pack(pady=10)


    


myFont = font.Font(size=30)    
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

f2=Frame(window, borderwidth=5, bg="blue" ,relief=SUNKEN)
f2.pack(side=tk.BOTTOM, fill="both")
l2a=Label(f2, text="")
l2a.pack(side=LEFT, padx=5, pady=5)
#l2b=Label(f2)
#l2b.pack(side=RIGHT, padx=5, pady=10)

f2=Frame(window, borderwidth=6 )
f2.pack(side=TOP, fill="x")
img = ImageTk.PhotoImage(Image.open("coke-ovenpng.png"))
label = Label(f2, image = img)
label.pack(side=LEFT)
img3 = ImageTk.PhotoImage(Image.open("BSP.jpg"))
label3= Label(f2, image = img3)
label3.pack(side=LEFT)
img2 = ImageTk.PhotoImage(Image.open("coke-ovenpng.png"))
label2= Label(f2, image = img2)
label2.pack(side=LEFT)


my_label=Label(window,text="Search Instrument",font=("Helvetica",14),fg="grey")
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


update_label()

# Start the application
window.mainloop()
