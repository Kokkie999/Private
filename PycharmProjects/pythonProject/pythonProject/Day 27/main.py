from tkinter import *

# Create window
window = Tk()
window.title("My First GUI-program")
window.minsize(width=500, height=300)

# Create label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Create buttons
def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack()

# Create entry
input = Entry(width=15)
input.pack()

window.mainloop()
