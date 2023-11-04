from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


FONT_IN = ("Courier", 15, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_sym + password_num
    shuffle(password_list)
    password = "".join(password_list)      # This makes a string that holds the password
    password_input.insert(END, password)
    pyperclip.copy(password)        # This automatically copies the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_input.get()
    email = email_input.get()
    p_word = password_input.get()
    if web == "" or email == "" or p_word == "":       # If there's empty fields, it won't let you continue
        messagebox.showerror(title="ERROR", message="You left a field empty")

    else:
        is_okay = messagebox.askokcancel(title=web, message=f"Details entered:\nUsername: {email}\n"
                                                            f"Password: {p_word}\nSAVE THESE DETAILS?")
        if is_okay == TRUE:
            with open("Password_Storage.txt", "a+") as store_password:
                store_password.write(f"Site: {web} | Email/Username: {email} | Password: {p_word} \n")
            website_input.delete(0, END)    # This clears the website and password fields
            password_input.delete(0, END)   # So it's ready to use again

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

lock = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# All the Labels
website_label = Label(text="Website:", font=FONT_IN)        # The 'sticky=' sticks the widgets to the East/West borders
website_label.grid(row=1, column=0, sticky=E)
password_label = Label(text="Password:", font=FONT_IN)
password_label.grid(row=3, column=0, sticky=E)
email_label = Label(text="Email/Username:", font=FONT_IN)
email_label.grid(row=2, column=0, sticky=E)

# All the Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
website_input.focus()   # This focuses the cursor into the input field

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky=EW)
email_input.insert(0, "uadam253@gmail.com")     # Index is the location where it auto-writes the email

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)

# All the Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky=EW)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
