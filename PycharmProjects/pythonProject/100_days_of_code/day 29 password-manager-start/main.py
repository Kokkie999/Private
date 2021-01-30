from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n "
                                                          f"Email: {email} \n "
                                                          f"Password: {password} \n\n"
                                                          f"Is it ok to save?")

    if is_ok:
        with open("passwords.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "iwan.de.kok@outlook.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=15)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)





# timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 27, "bold"))



# label_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
# label_title.grid(column=1, row=0)
#

#
#
# button_start = Button(text="Start", width=7, command=start_timer)
# button_start.grid(column=0, row=3)
#
# button_reset = Button(text="Reset", width=7, command=reset_timer)
# button_reset.grid(column=3, row=3)
#
# label_check_marks = Label(fg=GREEN, bg=YELLOW)
# label_check_marks.grid(column=1, row=4)
#
window.mainloop()
