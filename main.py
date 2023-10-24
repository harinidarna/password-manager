from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# to get copied onto clipboard directly
# import pyperclip
# pyperclip.copy(text)
# ---------------------------- SEARCH WEBSITE ----------------------------- #
def search_website():
    website_name = website_entry.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website_name in data:
            details = data[website_name]
            messagebox.showinfo(title=website_name, message=f"Email: {details['Email']}\n"
                                                            f"password: {details['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists.")





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    res = ''.join(password_list)
    password_entry.insert(0, res)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_file():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="fields required", message="Please fill all the fields.")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, sticky='W')

email_username_entry = Entry(width=52)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky='W')

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, sticky='W')

# buttons
search = Button(text="search", bg="white", width=14, command=search_website)
search.grid(row=1, column=2)

generate_password = Button(text="Generate Password", bg="white", command=generate_password)
generate_password.grid(row=3, column=2, sticky='W')

add = Button(text="Add", bg="white", width=43, command=add_to_file)
add.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()
