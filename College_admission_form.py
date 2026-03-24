import tkinter as tk
from tkinter import messagebox

def on_submit():
    name = name_entry.get()
    dob = dob_entry.get()
    email = email_entry.get()
    branch = branch_var.get()
    responce = responce_entry.get()
    
    selected_games = []
    if cricket_var.get():
        selected_games.append("Cricket")
    if football_var.get():
        selected_games.append("Football")
    if badminton_var.get():
        selected_games.append("Badminton")
    
    if not name:
        messagebox.showwarning("Input Error", "Please enter a student name.")
        return
    
    # Update the output section
    output_text = f"Your name is {name}.\n"
    output_text += f"Your date of birth is {dob}.\n"
    output_text += f"E-mail: {email_entry.get()}\n"
    output_text += f"{name} is from {branch} Department.\n"
    output_text += f"Your response:  {responce}\n"

    if selected_games:
        games_str = " and ".join(selected_games)
        output_text += f"{name} is from {branch} Department and enjoy playing {games_str}."
    else:
        output_text += f"{name} is from {branch} Department."
        
    output_label.config(text=output_text)

root = tk.Tk()
root.title("Student Admission Form")
root.geometry("600x600")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)
tk.label1 = tk.Label(main_frame, text="Student Information Form", font=("Arial", 16, "bold"))

tk.Label(main_frame, text="Enter Student Name:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
name_entry = tk.Entry(main_frame, width=30)
name_entry.grid(row=0, column=1, sticky="w", padx=10)

tk.Label(main_frame, text="Enter Date of Birth (YYYY-MM-DD):", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
dob_entry= tk.Entry(main_frame, width=30)
dob_entry.grid(row=1, column=1, sticky="w", padx=10)

tk.Label(main_frame, text="Enter E-mail:", font=("Arial", 10, "bold")).grid(row=1, column=2, sticky="w", pady=10)
email_entry = tk.Entry(main_frame, width=30)
email_entry.grid(row=1, column=3, sticky="w", padx=10)

tk.Label(main_frame, text="Select Your Branch:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=10)
branch_var = tk.StringVar(value="Ai & Ds")
tk.Radiobutton(main_frame, text="Ai & Ds", variable=branch_var, value="Ai & Ds").grid(row=2, column=1, sticky="w", padx=10)
tk.Radiobutton(main_frame, text="Computer Engineering", variable=branch_var, value="Computer Engineering").grid(row=2, column=2, sticky="w", padx=10)
tk.Radiobutton(main_frame, text="Information Technology", variable=branch_var, value="Information Technology").grid(row=2, column=3, sticky="w")

tk.Label(main_frame, text="Select Favorite Games:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=10)
cricket_var = tk.BooleanVar()
football_var = tk.BooleanVar()
badminton_var = tk.BooleanVar()

tk.Checkbutton(main_frame, text="Cricket", variable=cricket_var).grid(row=3, column=1, sticky="w", padx=10)
tk.Checkbutton(main_frame, text="Football", variable=football_var).grid(row=3, column=2, sticky="w")
tk.Checkbutton(main_frame, text="Badminton", variable=badminton_var).grid(row=3, column=3, sticky="w")

tk.Label(main_frame, text="Enter your response:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=10)
responce_entry = tk.Entry(main_frame, width=50)
responce_entry.grid(row=4, column=1, columnspan=3, sticky="w", padx=10)

submit_btn = tk.Button(main_frame, text="Submit", command=on_submit, width=10)
submit_btn.grid(row=5, column=1, pady=20)


tk.Label(main_frame, text="OUTPUT:", font=("Arial", 10, "bold", "underline"), fg="blue").grid(row=6, column=0, sticky="w", pady=(10, 5))
output_label = tk.Label(main_frame, text="", justify="left", font=("Arial", 10))
output_label.grid(row=7, column=0, columnspan=4, sticky="w")


root.mainloop()



    