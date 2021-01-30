from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI-program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Buttons
button1 = Button(text="Click me", command=button_clicked)
# button.pack()
button1.grid(column=1, row=1)

button2 = Button(text="Click me also", command=button_clicked)
# button.pack()
button2.grid(column=2, row=0)

# Entry
input = Entry(width=15)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


window.mainloop()
