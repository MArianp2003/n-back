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
        self.root.title('N-Back Visual Program')
        self.width_window, self.height_window = (600, 600)
        self.reso = f'{str(self.width_window)}x{str(self.height_window)}'
        self.root.geometry(self.reso)

        self.input_frame = tk.Frame(
            master=self.root
        )
        
        self.prompt_label = tk.Label(
            master=self.input_frame, 
            text="Name:", 
            font=("Helvetica", 12)
        )
        
        self.name_entry = tk.Entry(
            master=self.input_frame, 
            font=("Helvetica", 12), 
            width=20
        )

        self.submit_button = tk.Button(
            master=self.root, 
            text="Submit", 
            font=("Helvetica", 12), 
            command=self.login,
            width=25,
            bg='#71F5BC'
        )

        self.countdown_time = Time.countdown_time
        self.timer_label = tk.Label(
            master=self.root,
            text=f'Time left: 10:00',
            font=("Helvetica", 12, 'bold'),
            state='disabled'
        )
        
        self.number_label = tk.Label(
            master=self.root, 
            text="Waiting to submit",
            font=('Arial', 24),
            state='disabled'
        )
        
        self.check_button = tk.Button(
            master=self.root,
            text='Check',
            font=('Arial', 14),
            width = 15, 
            height = 3,
            bg = "#87CEEB", #light blue
            relief = "ridge", 
            borderwidth=4,
            activebackground='yellow',
            activeforeground='black',
            command=self.Click_Button,
            state='disabled'
        )
        
        self.message_label = tk.Label(
            master=self.root,
            text="", 
            font=("Arial", 24),
            state='disabled'
        )

        self.number_label.place(relx=0.5, rely=0.4, anchor='center')
        self.check_button.place(relx=0.5, rely=0.7, anchor='center')
        self.message_label.place(relx=0.5, rely=0.85, anchor="center")
        self.timer_label.place(relx=0.05, rely=0.08)
        self.input_frame.place(relx=0.8, rely=0.1, anchor='center')
        self.submit_button.place(relx=0.8, rely=0.15, anchor='center')
        self.prompt_label.pack(side="left")
        self.name_entry.pack(side="left")
        self.root.bind('<space>', self.take_action)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
    
    def start_counting(self):
        self.number_label.config(font=('Arial', 80))
        self.update_timer()
        self.start_show_number()

    def login(self):
        if not self.name_entry.get():
            messagebox.showerror('ERROR!', message='Name can not be empty')
        else:
            self.name_entry.config(state='disabled')
            self.prompt_label.config(state='disabled')
            self.submit_button.config(state='disabled')
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
    