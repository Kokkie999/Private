from tkinter import *

font = ("Arial", 11)


def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.6093, 2)
    label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

input_miles = Entry(width=7, font=font)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles", font=font)
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to", font=font)
label_equal.grid(column=0, row=1)

label_km = Label(text="Km", font=font)
label_km.grid(column=2, row=1)

label_result = Label(text=0, font=font)
label_result .grid(column=1, row=1)


button_calculate = Button(text="Calculate", command=miles_to_km, font=font)
button_calculate.grid(column=1, row=3)

window.mainloop()