from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- SAVE API-DATA ------------------------------- #
def save():
    api_name = api_name_entry.get()
    endpoint = endpoint_entry.get()
    api_id = api_id_entry.get()
    api_key = api_key_entry.get()
    token = token_entry.get()

    new_data = {
        api_name: {
            "endpoint": endpoint,
            "api_id": api_id,
            "api_key": api_key,
            "token": token,
        }
    }

    if len(api_name) == 0 or len(endpoint) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("C:/Users/iwand/OneDrive/api_key.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("C:/Users/iwand/OneDrive/api_key.json", "w") as data_file:
                # Create file and saving the first data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("C:/Users/iwand/OneDrive/api_key.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            api_name_entry.delete(0, END)
            endpoint_entry.delete(0, END)
            api_id_entry.delete(0, END)
            api_key_entry.delete(0, END)
            token_entry.delete(0, END)


# ------------------------- FIND API-DATA ----------------------------- #
def find():
    api_name = api_name_entry.get()
    try:
        with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No datafile found!")
    else:
        if api_name in data:
            endpoint = data[api_name]["endpoint"]
            api_id = data[api_name]["api_id"]
            api_key = data[api_name]["api_key"]
            token = data[api_name]["token"]
            messagebox.showinfo(title=api_name, message=f"Endpoint: {endpoint}\nAPI ID: {api_id}\nAPI key: {api_key}\nToken: {token}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("API Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

# Labels
api_name_label = Label(text="API naam:", justify=LEFT).grid(sticky=W, row=1, column=0)
endpoint_label = Label(text="Endpoint:", justify=LEFT).grid(sticky=W, row=2, column=0)
api_id_label = Label(text="API ID:", justify=LEFT).grid(sticky=W, row=3, column=0)
api_key_label = Label(text="API key:", justify=LEFT).grid(sticky=W, row=4, column=0)
api_token_label = Label(text="Token:", justify=LEFT).grid(sticky=W, row=5, column=0)

# Entries
api_name_entry = Entry(width=35, justify=LEFT)
api_name_entry.grid(sticky=W, row=1, column=1)
endpoint_entry = Entry(width=60, justify=LEFT)
endpoint_entry.grid(sticky=W, row=2, column=1, columnspan=2)
api_id_entry = Entry(width=60, justify=LEFT)
api_id_entry.grid(sticky=W, row=3, column=1, columnspan=2)
api_key_entry = Entry(width=60, justify=LEFT)
api_key_entry.grid(sticky=W, row=4, column=1, columnspan=2)
token_entry = Entry(width=60, justify=LEFT)
token_entry.grid(sticky=W, row=5, column=1, columnspan=2)

# Buttons
search_button = Button(text="Zoeken", width=18, justify=RIGHT, command=find)
search_button.grid(sticky=W, row=1, column=2)
add_button = Button(text="Toevoegen", width=18, justify=LEFT, command=save)
add_button.grid(sticky=W, row=6, column=1)

window.mainloop()
