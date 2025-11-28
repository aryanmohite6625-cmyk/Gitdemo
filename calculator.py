import tkinter
from tkinter import *
from tkinter import ttk

window =Tk()
window.title("Calculator")

lable_1=ttk.Label(window,text="CALCULATOR")
lable_1.pack(side="top")
window.geometry("500x500")

e=Entry(width=56,borderwidth=5)
e.place(x=0,y=0)

def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+ str(num))


b=ttk.Button(text="1",width=12,command=lambda :click(1))
b.place(x=10,y=60)

b=ttk.Button(text="2",width=12,command=lambda :click(2))
b.place(x=80,y=60)

b=ttk.Button(text="3",width=12,command=lambda :click(3))
b.place(x=170,y=60)

b=ttk.Button(text="4",width=12,command=lambda :click(4))
b.place(x=10,y=120)

b=ttk.Button(text="5",width=12,command=lambda :click(5))
b.place(x=80,y=120)

b=ttk.Button(text="6",width=12,command=lambda :click(6))
b.place(x=170,y=120)

b=ttk.Button(text="7",width=12,command=lambda :click(7))
b.place(x=10,y=180)

b=ttk.Button(text="8",width=12,command=lambda :click(8))
b.place(x=80,y=180)

b=ttk.Button(text="9",width=12,command=lambda :click(9))
b.place(x=170,y=180)

b=ttk.Button(text="0",width=12,command=lambda :click(0))
b.place(x=10,y=240)


#OPERATOR
def add():
    n1=e.get()
    global math
    math="Addition"
    global i
    i=int(n1)
    e.delete(0,END)

b=ttk.Button(text="+",width=12,command=add)
b.place(x=80,y=240)


def sub():
    n1 = e.get()
    global math
    math="Subtraction"
    global i
    i = int(n1)
    e.delete(0, END)


b=ttk.Button(text="-",width=12,command=sub)
b.place(x=170,y=240)


def mul():
    n1 = e.get()
    global i
    global math
    math="Multiplication"
    i = int(n1)
    e.delete(0, END)


b=ttk.Button(text="*",width=12,command=mul)
b.place(x=10,y=300)


def div():
    n1 = e.get()
    global math
    math="Division"
    global i
    i = int(n1)
    e.delete(0, END)


b=ttk.Button(text="/",width=12,command=div)
b.place(x=80,y=300)

def equal():
    n2=e.get()
    e.delete(0, END)
    if math =="Addition":
        e.insert(0,i+int(n2))
    elif math == "Subtraction":
        e.insert(0,i-int(n2))
    elif math == "Multiplication":
        e.insert(0,i*int(n2))
    elif math=="Division":
        e.insert(0,i/int(n2))

b=ttk.Button(text="=",width=12,command=equal)
b.place(x=170,y=300)

def clear():
    e.delete(0,END)

b=ttk.Button(text="Clear",width=12,command=clear)
b.place(x=10,y=360)

quit_button=ttk.Button(text="Quit",width=12,command=window.destroy)
quit_button.place(x=170,y=360)
mainloop()