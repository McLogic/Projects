from tkinter import *
import tkinter as tk
import random
import pyperclip
from PIL import Image


def password_gen():
    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = uppercaseLetters.lower()
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    uppercase, lowercase, number, symbol = True, True, True, True

    all = ""

    if uppercase:
        all += uppercaseLetters
    if lowercase:
        all += lowercaseLetters
    if number:
        all += numbers
    if symbol:
        all += symbols

    length = 16

    global password
    password = "".join(random.sample(all, length))

    result_box.configure(state="normal")
    result_box.delete(0, tk.END)
    result_box.insert(tk.END, password)
    result_box.configure(state="readonly")

def save_password():
    specified_app = app_box.get()
    saved_passwords = open("generated_passwords", "a")
    saved_passwords.write(specified_app + ": " + password + "\n")
    saved_passwords.close()

def app_prompt(self):
    app_box.delete(0, tk.END)

def safe_locked(self):
    password_safe.delete(1.0, tk.END)

def open_safe():
    global safe_open
    safe_open = open("generated_passwords", "r+")
    password_safe.insert(1.0, safe_open.read())
    password_safe.bind("<FocusOut>", safe_locked)
    safe_open.close()

def copy_password():
    pyperclip.copy(password)



root = tk.Tk()

root.geometry("400x500")
root.title("Password Generator")
root.configure(background="slategray")

bg = PhotoImage(file="safeimage.png")
bglabel = tk.Label(root, image=bg)
bglabel.place(x=-1.5, y=0)


label = tk.Label(root, text="Password Generator", background="lavender", highlightbackground="darkgrey", highlightthickness=2, font=('Times New Roman', 28))
label.place(x=47, y=70)

result_box = tk.Entry(root, width=26, font=('Times New Roman', 12))
result_box.place(x=95, y=150)

app_box = tk.Entry(root, width=26, font=('Times New Roman', 12))
app_box.place(x=95, y=180)
app_box.insert(0, "Specify App...")
app_box.bind("<FocusIn>", app_prompt)

password_safe = tk.Text(root, height=5, width=26, font=('Times New Roman', 12))
password_safe.place(x=95, y=220)
password_safe.insert(1.0, "SAFE LOCKED")
password_safe.bind("<FocusIn>", safe_locked)

buttonframe = tk.Frame(root)
buttonframe.configure(background="slategrey")
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

password_gen_button = tk.Button(buttonframe, text="Generate Password", font=('Times New Roman', 12),command=password_gen)
password_gen_button.grid(row=0, column=0, sticky=tk.E+tk.W)

save_password_button = tk.Button(buttonframe, text="Save Password", font=('Times New Roman', 12),command=save_password)
save_password_button.grid(row=1, column=0, sticky=tk.E+tk.W)

open_safe_button = tk.Button(buttonframe, text="Open Safe", font=('Times New Roman', 12), command=open_safe)
open_safe_button.grid(row=2, column=0, sticky=tk.E+tk.W)

copy_password_button = tk.Button(buttonframe, text="Copy Password", font=('Times New Roman', 12), command=copy_password)
copy_password_button.grid(row=3, column=0, sticky=tk.E+tk.W)

buttonframe.place(x=135, y=340)

root.mainloop()
