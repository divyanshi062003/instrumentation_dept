from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("login")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.configure(bg="#fff")
root.resizable(False,False)
img=PhotoImage(file="login.png")
Label(root,image=img,bg='white').place(x=200,y=100)
frame=Frame(root,width=700,height=1000,bg="white")
frame.place(x=700,y=120)
heading=Label(frame,text='BSP Employee Login',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',18,'bold'))
heading.place(x=50,y=5)
def signin():
    username=user.get()
    password=code.get()
    if(username=="admin" and password=="1234567890"):
        root.destroy()
        import indextest

##
def on_enter(e):
    user.delete()
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusIn>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
##
def on_enter(e):
    code.delete()
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusIn>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

Button(frame,width=6,text="Sign in",bg="#57a1f8",fg='white',border=0,command=signin).place(x=35,y=204)

root.mainloop()