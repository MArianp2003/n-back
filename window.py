import tkinter as tk
from config import *
import random

class Window:
    def __init__(self):
        self.set_widgets()
        self.root.bind('<space>', self.press_space)
        self.generate_random_number()
        self.run()
        
    def set_widgets(self):
        self.root = tk.Tk()
        self.root.title(Win_prop.title)
        self.width_window, self.height_window = Win_prop.resolution
        self.reso = f'{str(self.width_window)}x{str(self.height_window)}'
        self.root.geometry(self.reso)
        
        self.number_label = tk.Label(
            self.root, 
            text="",
            font=Label_prop.font
        )
        
        self.check_button = tk.Button(
            self.root,
            text=But_prop.text,
            font=But_prop.font,
            width=But_prop.width, 
            height=But_prop.height,
            bg=But_prop.bg,
            relief=But_prop.relief, 
            borderwidth=But_prop.borderwidth,
            command=None #TODO
        )
        
        self.message_label = tk.Label(
            self.root,
            text="", 
            font=Message_prop.font
        )

        self.number_label.place(relx=0.5, rely=Label_prop.rely, anchor='center')
        self.check_button.place(relx=0.5, rely=But_prop.rely, anchor='center')
        self.message_label.place(relx=0.5, rely=Message_prop.rely, anchor="center")
            
        
    def on_button_click(self):
        print("hello the message")  # Print the message


    def generate_random_number(self):
        random_number = random.randint(0, 9)
        self.number_label.config(text=str(random_number))
        self.root.after(250, self.generate_random_number)
    
    def press_space(self, event):
        # Change the button's background color to indicate it was pressed
        original_color = self.check_button.cget("bg")  # Get the original color
        self.check_button.config(bg="yellow")  # Change to a blinking color
        self.on_button_click()  # Call the button click function
        
        self.message_label.config(text="you hit the press key")  # Set the label text
        
        # Clear the label after 500ms
        self.root.after(500, self.clear_label)

        self.root.after(200, lambda: self.check_button.config(bg=original_color))  # Revert color after 200ms
    
    def clear_label(self):
        self.message_label.config(text="")  # Clear the label text
        
    def run(self):
        self.root.mainloop()