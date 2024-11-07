import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.withdraw()  # Hide the main window

if messagebox.askyesno("Confirmation", "Are you sure you want to clear database?"):
    with open('database.json', 'w') as json_file:
        json_file.write(json.dumps([], indent=4))
        
    with open('database.csv', 'w') as csv_file:
        csv_file.write('')

root.destroy()