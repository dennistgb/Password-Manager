from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
        , 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_enter.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    password_file = open("passwords.txt", "a")
    web_info = website_enter.get()
    user_info = user_enter.get()
    pass_info = pass_enter.get()
    if len(user_info) == 0 or len(pass_info) == 0:
        messagebox.showinfo(title="you idiot", message="you forgor you dumb dumb")
    else:
        isok = messagebox.askokcancel(title=web_info, message=f"These are the details entered: \nEmail: {user_info} "
                                                          f"\nPassword: {pass_info}\nIs it ok to save?")
        if isok:
            password_file.write(f"\n{web_info}|{user_info}|{pass_info}")
            website_enter.delete(0, END)
            pass_enter.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", fg="black")
website_label.grid(row=1, column=0)
website_enter = Entry(width=45)
website_enter.grid(row=1, column=1, columnspan=2, pady=5)

user_label = Label(text="Email/Username:", fg="black")
user_label.grid(row=2, column=0)
user_enter = Entry(width=45)
user_enter.grid(row=2, column=1, columnspan=2, pady=5)
user_enter.insert(0, "dennistgb579@gmail.com")

pass_label = Label(text="Password:", fg="black")
pass_label.grid(row=3, column=0)
pass_enter = Entry(width=30)
pass_enter.grid(row=3, column=1, pady=5)
pass_generate = Button(text="Generate Password", width=14, command=pass_gen)
pass_generate.grid(row=3, column=2, padx=0)

add_button = Button(text="Add", width=40, command=add_pass)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
