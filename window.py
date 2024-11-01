import tkinter as tk
from tkinter import messagebox
from config import *

import random

class Window:
    def __init__(self):
        self.data = list()
        self.set_widgets()
        self.run()
    
    def set_widgets(self):
        self.root = tk.Tk()
        self.root.title(Win_prop.title)
        self.width_window, self.height_window = Win_prop.resolution
        self.reso = f'{str(self.width_window)}x{str(self.height_window)}'
        self.root.geometry(self.reso)

        self.input_frame = tk.Frame(self.root)
        prompt_label = tk.Label(
            self.input_frame, 
            text="Name:", 
            font=("Helvetica", 12)
        )
        
        self.name_entry = tk.Entry(
            self.input_frame, 
            font=("Helvetica", 12), 
            width=20
        )

        self.submit_button = tk.Button(
            self.root, 
            text="Submit", 
            font=("Helvetica", 12), 
            command=self.login,
            width=25,
            bg='#71F5BC'
        )

        self.countdown_time = Time.countdown_time
        self.timer_label = tk.Label(
            self.root,
            text=f'Time left: 10:00',
            font=Time.font,
            state='disabled'
        )
        
        self.number_label = tk.Label(
            self.root, 
            text="Waiting to submit",
            font=Number_prop.font,
            state='disabled'
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
            activebackground=But_prop.activebackground,
            activeforeground=But_prop.activeforeground,
            command=self.Click_Button,
            state='disabled'
        )
        
        self.message_label = tk.Label(
            self.root,
            text="", 
            font=Message_prop.font,
            state='disabled'
        )

        self.number_label.place(relx=0.5, rely=Number_prop.rely, anchor='center')
        self.check_button.place(relx=0.5, rely=But_prop.rely, anchor='center')
        self.message_label.place(relx=0.5, rely=Message_prop.rely, anchor="center")
        self.timer_label.place(relx=0.05, rely=0.08)
        self.input_frame.place(relx=0.8, rely=0.1, anchor='center')
        self.submit_button.place(relx=0.8, rely=0.15, anchor='center')
        prompt_label.pack(side="left")
        self.name_entry.pack(side="left")
        self.root.bind('<space>', self.take_action)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
    
    def start_counting(self):
        self.number_label.config(font=Number_prop.after_login_font)
        self.update_timer()
        self.start_show_number()

    def login(self):
        if not self.name_entry.get():
            messagebox.showerror('ERROR!', message='Name can not be empty')
        else:
            self.timer_label.config(state='normal')
            self.number_label.config(state='normal')
            self.number_label.config(text='Ready?')
            self.check_button.config(state='normal')
            self.message_label.config(state='normal')
            self.number_label.after(1000, self.start_counting)
        
    
    def generate_and_set(self):
        random_number = random.randint(0, 9)
        self.data.append(random_number)
        return random_number
    
    def start_show_number(self):
        random_number = self.generate_and_set()
        self.number_label.config(text=str(random_number))
        self.root.after(Number_prop.show_wait, lambda: self.number_label.config(text=''))
        self.number_label.after(Number_prop.sleep_wait, self.start_show_number)
     
    def run(self):
        self.root.mainloop()
    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.root.destroy()
    
    def take_action(self, event):
        original_color = self.check_button.cget('bg')
        self.check_button.config(bg='yellow')
        self.check_button.after(100, lambda: self.check_button.config(bg=original_color))    
        self.message_label.config(text= self.data)
        # self.message_label.after(500, lambda: self.message_label.config(text=''))

    def Click_Button(self):
        self.take_action(event=None)
        
    def update_timer(self):
        minutes = self.countdown_time // 60
        seconds = self.countdown_time % 60
        self.timer_label.config(text=f"Time left: {minutes:02}:{seconds:02}")
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.root.destroy()
    
    