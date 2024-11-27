import tkinter as tk
from tkinter import messagebox
from config import *
from process import *
import random
from datetime import datetime
from time import sleep
class Test_Window:
    def __init__(self):
        self.force_quit = False
        self.new_number_lock = False
        self.countdown_time = Time.countdown_time
        self.latencies_at_time = list()
        self.data = list()
        self.latencies = list()
        self.catch = dict()
        self.__set_widgets()
    
    def __set_widgets(self):
        
        self.root = tk.Tk()
        self.root.title('N-Back Visual Program')
        self.root.geometry('600x600')
        
        self.time_frame = tk.Frame(
            master=self.root,
        )
        
        self.timer_label = tk.Label(
            master=self.time_frame,
            text=f'Time: ',
            font=("Helvetica", 12, 'bold'),
        )

        
        self.entry_minutes = tk.Entry(
            master=self.time_frame,
            width=5,
            font=("Helvetica", 16),
        )
        self.entry_minutes.insert(0, '5')
        
        self.colon_label = tk.Label(
            master=self.time_frame, 
            text=":", 
            font=("Helvetica", 16)
        )
        
        self.entry_seconds = tk.Entry(
            master=self.time_frame,
            width=5,
            font=("Helvetica", 16),
            textvariable='0'
        )
        self.entry_seconds.insert(0, '00')
        
        self.name_frame = tk.Frame(
            master=self.root,
        )
        
        self.prompt_label = tk.Label(
            master=self.name_frame, 
            text="Name", 
            font=("Helvetica", 12)
        )
        
        self.name_entry = tk.Entry(
            master=self.name_frame, 
            font=("Helvetica", 12), 
            width=22
        )

        self.submit_button = tk.Button(
            master=self.name_frame, 
            text="Submit", 
            font=("Helvetica", 12), 
            command=self.login,
            width=25,
            bg='#71F5BC'
        )

        self.test_frame = tk.Frame(
            master=self.root,
        )
        
        self.number_label = tk.Label(
            master=self.test_frame, 
            text="Waiting to submit",
            font=('Arial', 24),
            state='disabled',
            pady=60,
        )
        
        self.check_button = tk.Button(
            master=self.test_frame,
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
            master=self.test_frame,
            text="", 
            font=("Arial", 16),
            state='disabled'
        )

        self.timer_label.pack(side='left')
        self.prompt_label.pack(side="left")
        self.entry_minutes.pack(side='left')
        self.colon_label.pack(side='left')
        self.entry_seconds.pack(side='left')
        self.time_frame.place(relx=0.2, rely=0.15, anchor='center')

        self.prompt_label.pack(fill='x', side='top')
        self.name_entry.pack(fill='x')
        self.submit_button.pack(pady=10) 
        self.name_frame.place(relx=0.7, rely=0.15, anchor='center')
        
        self.number_label.pack(side='top')
        self.check_button.pack()
        self.message_label.pack()
        self.test_frame.place(relx=0.5, rely=0.6, anchor='center')
        
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.force_quit = True
            self.close_Test_Window()
    
    def run(self):
        self.root.mainloop()

    def start_counting(self):
        self.entry_seconds.pack_forget()
        self.entry_minutes.pack_forget()
        self.colon_label.pack_forget()
        self.number_label.config(font=('Arial', 80))
        self.timer_label.config(font=('Arial', 16))
        self.update_timer()
        self.start_show_number()

    def validate_time_entry(self):
        try:
            m = int(self.entry_minutes.get())
            s = int(self.entry_seconds.get())
        except:
            return False
        
        if m >= 0 and 0 <= s < 60 and m * 60 + s > 0:
            return True
        
        return False
        
    def login(self):
        if not self.name_entry.get() or not self.validate_time_entry():
            messagebox.showerror('ERROR!', message='Invalid name or time, check the inputs and try again.')
            
        else:
            self.name = self.name_entry.get()
            self.m = int(self.entry_minutes.get())
            self.s = int(self.entry_seconds.get())
            for widget in self.name_frame.winfo_children():
                widget.config(state='disabled')
            for widget in self.name_frame.winfo_children():
                widget.config(state='disabled')
            for widget in self.test_frame.winfo_children():
                widget.config(state='normal')
            self.number_label.config(text='Ready?')
            self.countdown_time = self.m * 60 + self.s
            self.countdown_time += 2 - (self.countdown_time) % 3
            self.time_left = self.countdown_time 
            self.number_label.after(1000, self.start_counting)
            self.root.bind('<space>', self.take_action)

    
    def generate_and_set(self):
        random_number = random.randint(0, 2)
        self.data.append(random_number)
        return random_number
    
    def start_show_number(self):
        random_number = self.generate_and_set()
        self.number_label.config(text=str(random_number))
        self.new_number_lock = False
        self.d1 = datetime.now()
        self.root.after(Number_prop.show_wait, lambda: self.number_label.config(text=''))
        self.number_label.after(Number_prop.sleep_wait, self.start_show_number)
     
    
    def take_action(self, event):
        self.d2 = datetime.now()
        original_color = self.check_button.cget('bg')
        self.check_button.config(bg='yellow')
        self.check_button.after(100, lambda: self.check_button.config(bg=original_color))    
        if (len(self.data) < Mode.n_back_mode + 1):
            self.message_label.config(text= 'lack of data for test n-back')
        else:
            index = len(self.data) - Mode.n_back_mode - 1
            if not self.new_number_lock:
                self.new_number_lock = True
                self.message_label.config(text=f'Check submitted!')
                self.seq = self.data[index:]
                self.elapsed_time = (self.d2 - self.d1).total_seconds()
                self.latencies_at_time = self.time_left - self.countdown_time
                self.catch.update({index: (
                    self.seq, 
                    f'{self.latencies_at_time // 60:02}:{self.latencies_at_time % 60:02}',
                    round(self.elapsed_time, DigitRound.digit_round)    
                )})
        self.message_label.after(1000, lambda: self.message_label.config(text=''))
            
    def Click_Button(self):
        self.take_action(event=None)
        
    def update_timer(self):
        minutes = self.countdown_time // 60
        seconds = self.countdown_time % 60
        self.timer_label.config(text=f"Time left: {minutes:02}:{seconds:02}")
        if self.countdown_time > 0:
            self.countdown_time -= 1
            self.root.after(1000, self.update_timer)
        elif not self.force_quit:
                self.result = check_all_n_back(self.name, self.data, self.catch, self.time_left)
                self.number_label.config(text='Thank You!')
                self.number_label.after(800, self.close_Test_Window)
    
    def close_Test_Window(self):
        self.root.destroy()

def main():
    t = Test_Window()
    t.run()

if __name__ == '__main__':
    main()
    