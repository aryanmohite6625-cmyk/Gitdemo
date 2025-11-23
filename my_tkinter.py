import tkinter as tk
import tkinter.font as tfont
from tkinter import Entry
from tkinter import ttk

window = tk.Tk()
window.title("My Application")
custom_font=tfont.Font(family='Times new roman', size=20, slant='italic')

label=ttk.Label(text="Hello World!",font=custom_font,padding=15)   #LABEL
label.pack()
#label["text"] = "Have a nice day"
label.config(text="My new app")

window.geometry("300x700")
def function_button():
    input_text=user_input.get()
    label.config(text=input_text)

user_input = ttk.Entry(width=40)        #ENTRY
user_input.pack()
print(user_input.get())


button=ttk.Button(text="Click", command=function_button)       #BUTTON
button.pack()
quit_button=ttk.Button(text="Quit", command=window.destroy)
quit_button.pack(pady=10)


sep=ttk.Separator(orient="horizontal")     #SEPERATOR
sep.pack(fill="x")

text=tk.Text(height=5, width=25)
text.pack(pady=10)
text.focus_set()



text.insert("1.0","Enter your comment:")
def text_function():
    textdata=text.get("1.0","end")
    print(textdata)

text_button=ttk.Button(text="Get text", command=text_function)
text_button.pack()




'''text["state"]="disabled"

def enable_text():
    text["state"]="normal"


enable_button=ttk.Button(text="Enable the textbox", command=enable_text)
enable_button.pack()'''

check_option=tk.BooleanVar()    #CHECKBUTTON

def check_task():
    print(check_option.get())

check_button=ttk.Checkbutton(text="Agree with the terms and conditions",variable=check_option,command=check_task)
check_button.pack()

radio_value=tk.StringVar()      #RADIOBUTTON
def get_radio_value():
    print(radio_value.get())


option_1 = ttk.Radiobutton(text="Male",variable=radio_value,value="Male",command=get_radio_value)
option_2 = ttk.Radiobutton(text="Female",variable=radio_value,value="Female",command=get_radio_value)
option_1.pack()
option_2.pack()

#COMBOBOX
selected_country=tk.StringVar()
def display_country(event):
    msg=f"Selected country is {selected_country.get()}"
    country_label= ttk.Label(text=msg, font=custom_font, padding=15)
    country_label.pack()
    #print(f"Selected country: {selected_country.get()}")
countries=ttk.Combobox(textvariable=selected_country,values=("Australia","Canada","India","Sweden","US","UK"))
countries["state"]="readonly"
countries.pack()

countries.bind("<<ComboboxSelected>>",display_country)

#LISTBOX
food_items=("Pizza","Burger","Garlic bread","Nachos","Salad")
fav_food=tk.StringVar(value=food_items)
food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food_list.pack()

def get_fav_food(event):
    food_indices=food_list.curselection()
    for i in food_indices:
        print(food_list.get(i))

food_list.bind("<<ListboxSelect>>",get_fav_food)

#SPINBOX
counter=tk.IntVar(value=10)

def grt_spinbox_value():
    print(f"Current value is {spin_box.get()}")

spin_box=ttk.Spinbox(values=tuple(range(5,105,5)),textvariable=counter,wrap=True,command=grt_spinbox_value)
spin_box.pack()
print(f"The teh initial value is {spin_box.get()}")

window.mainloop()

