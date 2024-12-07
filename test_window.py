import tkinter as tk
from tkinter import messagebox
from config import *
from process import *
import random
from datetime import datetime

class Test_Window:
    def __init__(self):
        self.force_quit = False
        self.new_number_lock = False
        self.countdown_time = Time.countdown_time
        self.n_mode = Mode.n_back_mode
        self.latencies_at_time = list()
        self.data = list()
        self.latencies = list()
        self.catch = dict()
        self.__set_widgets()
    
    def __set_widgets(self):
        
        self.root = tk.Tk()
        self.root.title('N-Back Visual Program')
        self.root.geometry('600x600')
        self.root.configure(background=Color.green)
        
        self.time_frame = tk.Frame(
            master=self.root,
            background=Color.green,
        )
        
        self.timer_label = tk.Label(
            master=self.time_frame,
            text=f'Time: ',
            font=("Helvetica", 12, 'bold'),
            background=Color.green,
        )

        
        self.entry_minutes = tk.Entry(
            master=self.time_frame,
            width=5,
            font=("Helvetica", 16),
        )
        self.entry_minutes.insert(0, '5')
        self.entry_minutes.config(state='readonly')
        
        self.colon_label = tk.Label(
            master=self.time_frame, 
            text=":", 
            font=("Helvetica", 16),
            background=Color.green,
        )
        
        self.entry_seconds = tk.Entry(
            master=self.time_frame,
            width=5,
            font=("Helvetica", 16),
        )
        self.entry_seconds.insert(0, '00')
        self.entry_seconds.config(state='readonly')
        
        self.mode_frame = tk.Frame(
            master=self.root,
            background=Color.green,
        )
        
        self.mode_label = tk.Label(
            master=self.mode_frame,
            font=("Helvetica", 12, 'bold'),
            text='Mode:',
            background=Color.green,
        )
        
        self.mode_entry = tk.Entry(
            master=self.mode_frame,
            width=11,
            font=("Helvetica", 16),
        )
        self.mode_entry.insert(0, str(Mode.n_back_mode))
        self.mode_entry.config(state='readonly')
        
        self.name_frame = tk.Frame(
            master=self.root,
            background=Color.green,
        )
        
        self.prompt_label = tk.Label(
            master=self.name_frame, 
            text="Name", 
            font=("Helvetica", 12),
            background=Color.green,
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
            background=Color.green,
        )
        
        self.number_label = tk.Label(
            master=self.test_frame, 
            text="Waiting to submit",
            font=('Arial', 24),
            state='disabled',
            pady=60,
            background=Color.green,
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
            state='disabled',
            background=Color.green,
        )

        self.timer_label.pack(side='left')
        self.prompt_label.pack(side="left")
        self.entry_minutes.pack(side='left')
        self.colon_label.pack(side='left')
        self.entry_seconds.pack(side='left')
        self.time_frame.place(relx=0.2, rely=0.13, anchor='center')
        
        self.mode_label.pack(side='left')
        self.mode_entry.pack(side='left')
        self.mode_frame.place(relx=0.2, rely=0.18, anchor='center')
        
        self.prompt_label.pack(fill='x', side='top')
        self.name_entry.pack(fill='x')
        self.submit_button.pack(pady=10) 
        self.name_frame.place(relx=0.7, rely=0.15, anchor='center')
        
        self.number_label.pack(side='top')
        self.check_button.pack()
        self.message_label.pack()
        self.test_frame.place(relx=0.5, rely=0.6, anchor='center')
        
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
    
    def generate_3back_sequence(self):
        total_numbers = 92  # Total length of the sequence
        numbers_per_group = 18  # Numbers in each group
        required_3backs_per_group = 4  # Required 3-back occurrences per group
        range_of_numbers = 10  # Range of numbers (0 to 9)
        
        sequence = []
        
        for _ in range(total_numbers // numbers_per_group):
            group_numbers = []
            three_back_indices = random.sample(range(numbers_per_group - 3), required_3backs_per_group)
            current_group_3backs = 0
            
            for i in range(numbers_per_group):
                if i >= 3 and current_group_3backs < required_3backs_per_group and i - 3 in three_back_indices:
                    group_numbers.append(group_numbers[i - 3])
                    current_group_3backs += 1
                else:
                    new_number = random.randint(0, range_of_numbers - 1)
                    while i >= 3 and new_number == group_numbers[i - 3]:
                        new_number = random.randint(0, range_of_numbers - 1)
                    group_numbers.append(new_number)
            
            sequence.extend(group_numbers)
        
        return sequence

    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.force_quit = True
            self.close_Test_Window()
    
    def run(self):
        self.root.mainloop()

    def start_counting(self):
        for widget in self.name_frame.winfo_children():
            widget.pack_forget()
        for widget in self.mode_frame.winfo_children():
            widget.pack_forget()
        for widget in self.time_frame.winfo_children():
            widget.pack_forget()
        self.name_frame.pack_forget()
        self.mode_frame.pack_forget()
        self.time_frame.pack_forget()
        self.number_label.config(font=('Arial', 90))
        self.root.geometry('500x500')
        self.test_frame.config(pady=80)
        self.test_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.timer_label.config(font=('Arial', 16))
        self.data = self.generate_3back_sequence()
        print(self.data)
        self.data_index = 0
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
            for widget in self.mode_frame.winfo_children():
                widget.config(state='disabled')
            for widget in self.test_frame.winfo_children():
                widget.config(state='normal')
            self.number_label.config(text='Ready?')
            self.countdown_time = self.m * 60 + self.s - 1
            self.n_mode = int(self.mode_entry.get())
            self.time_left = self.countdown_time 
            self.number_label.after(1000, self.start_counting)
            self.root.bind('<space>', self.take_action)

    
    def generate_and_set(self):
        random_number = self.data[self.data_index]
        self.data_index += 1
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
        if (len(self.data) < self.n_mode + 1):
            self.message_label.config(text= 'lack of data for test n-back')
        else:
            index = len(self.data) - self.n_mode - 1
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
            self.result = check_all_n_back(self.name, self.data, self.catch, self.time_left, self.n_mode)
            self.number_label.config(font=('Arial', 24))
            self.number_label.config(text='Thank You!')
            self.number_label.after(800, self.close_Test_Window)
    
    def close_Test_Window(self):
        self.root.destroy()

def main():
    t = Test_Window()
    t.run()

if __name__ == '__main__':
    main()
    