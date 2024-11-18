import tkinter as tk
from tkinter import messagebox
from config import DataBase, key_headers
import json, csv


root = tk.Tk()
root.withdraw()  # Hide the main window

if messagebox.askyesno("Confirmation", "Are you sure you want to clear database?"):
    with open('database.json', 'w') as json_file:
        json_file.write(json.dumps([], indent=4))

    with open(DataBase.csv_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=key_headers)
        writer.writeheader()


root.destroy()