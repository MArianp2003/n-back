import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from config import *
import json
import csv
import os

class Login_window:
    def __init__(self):
        self.mp3_file = None
        self.mquit = False
        self.__set_widgets()
    
    def __set_widgets(self):
        self.root = tk.Tk()
        self.root.title('N-Back Visual Program')
        self.root.geometry('600x300')
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
            width=7,
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
            width=7,
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
            text="n-back Mode:",
            font=("Arial", 16),
            background=Color.green,
        )
        
        self.mode_var = tk.StringVar(value="3")
        
        self.mode_dropdown = ttk.Combobox(
            master=self.mode_frame,
            textvariable=self.mode_var, 
            values=["3", "4"], 
            state="readonly",
            width=6
        )

        self.upload_button = tk.Button(
            master=self.root, 
            font=("Helvetica", 12, 'bold'),
            text="Condition file", 
            command=self.upload_file,
            width=20
        )
        
        self.frequency_frame = tk.Frame(
            master=self.root,
            background=Color.green,
            padx=10,
        )
        
        self.frequency_label = tk.Label(
            master=self.frequency_frame, 
            text="Select Frequency:", 
            font=("Arial", 12, 'bold'),
            background=Color.green,
        )
        
        self.frequency_var = tk.StringVar(value="0")
        self.frequency_dropdown = ttk.Combobox(
            master=self.frequency_frame, 
            textvariable=self.frequency_var, 
            values=["0", "5", "6.5", "30", "40"], 
            state="readonly",
            width=4
        )
        
        self.condition_frame = tk.Frame(
            master=self.root,
            background=Color.green,
            padx=10,
        )
        
        self.condition_label = tk.Label(
            master=self.condition_frame, 
            text="Select Condition type:", 
            font=("Arial", 12, 'bold'),
            background=Color.green,
        )
        
        self.condition_var = tk.StringVar(value="1")
        
        self.condition_dropdown = ttk.Combobox(
            master=self.condition_frame, 
            textvariable=self.condition_var, 
            values=["1", "2", "3", "4"], 
            state="readonly",
            width=4
        )
        
        self.debug_mode_frame = tk.Frame(
            master=self.root,
            background=Color.green,
            padx=10,
        )

        
        self.debug_mode_label = tk.Label(
            master=self.debug_mode_frame, 
            text="Debug Mode:", 
            font=("Arial", 12, 'bold'),
            background=Color.green,
        )
        
        self.debug_mode_var = tk.StringVar(value="OFF")
        
        self.debug_mode_dropdown = ttk.Combobox(
            master=self.debug_mode_frame, 
            textvariable=self.debug_mode_var, 
            values=["OFF", "ON"], 
            state="readonly",
            width=4
        )

        
        self.name_frame = tk.Frame(
            master=self.root,
            background=Color.green,
        )
        
        self.name_label = tk.Label(
            master=self.name_frame, 
            text="Name", 
            font=("Helvetica", 12, 'bold'),
            background=Color.green,
        )
        
        self.name_entry = tk.Entry(
            master=self.name_frame, 
            font=("Helvetica", 16), 
            width=20,
        )

        self.start_test_button = tk.Button(
            master=self.root, 
            text="Start Test", 
            font=("Helvetica", 14), 
            command=self.login,
            width=20,
            bg='#71F5BC'
        )

        self.timer_label.pack(side='left')
        self.name_label.pack(side="left")
        self.entry_minutes.pack(side='left')
        self.colon_label.pack(side='left')
        self.entry_seconds.pack(side='left')
        self.time_frame.place(relx=0.2, rely=0.1, anchor='center')
        
        self.mode_label.pack(side='left')
        self.mode_dropdown.pack(side='left')
        self.mode_frame.place(relx=0.2, rely=0.27, anchor='center')
        
        self.frequency_label.pack(side='left')
        self.frequency_dropdown.pack(side='left')
        self.frequency_frame.place(relx=0.2, rely=0.45, anchor='center')
        
        self.condition_label.pack(side='left')
        self.condition_dropdown.pack(side='left')
        self.condition_frame.place(relx=0.2, rely=0.6, anchor='center')
        
        self.debug_mode_label.pack(side='left')
        self.debug_mode_dropdown.pack(side='left')
        self.debug_mode_frame.place(relx=0.2, rely=0.75, anchor='center')
        
        self.name_label.pack(side='top')
        self.name_entry.pack()
        self.name_frame.place(relx=0.7, rely=0.12, anchor='center')
        
        self.upload_button.place(relx=0.7, rely=0.3, anchor='center')
        
        self.start_test_button.place(relx=0.5, rely=0.5)
        
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.mquit = True
            self.close_login_window()

    def close_login_window(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

    def upload_file(self):        
        self.mp3_file = filedialog.askopenfilename(
            filetypes=[("MP3 Files", "*.mp3")], 
            title="Choose an MP3 file"
        )
        if self.mp3_file:
            messagebox.showinfo("File Selected", f"Selected: {self.mp3_file}")
    
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
        elif int(self.condition_var.get()) == 1 and float(self.frequency_var.get()) != 0:
            messagebox.showerror('ERROR!', message='Condition type is 1, so frequency of flicker should be 0, please try again.')            
        elif int(self.condition_var.get()) == 2 and float(self.frequency_var.get()) == 0:
            messagebox.showerror('ERROR!', message='Condition type is 2 so frequency of flicker should be 6.5 or 30, please select one and try again.')
        elif int(self.condition_var.get()) == 3 and (float(self.frequency_var.get()) != 0 or not self.mp3_file):
            messagebox.showerror('ERROR!', message='Condition type is 3 so frequency of flicker should be 0 and binaural beats file must not be empty, please select one and try again.')            
        elif int(self.condition_var.get()) == 4 and (float(self.frequency_var.get()) == 0 or not self.mp3_file):
            messagebox.showerror('ERROR!', message='Condition type is 4 so frequency of flicker should be 6.5 or 30 and binaural beats file must not be empty, please select one and try again.')            
    
        else:
            self.name = self.name_entry.get()
            self.m = int(self.entry_minutes.get())
            self.s = int(self.entry_seconds.get())
            self.frequency = float(self.frequency_var.get())
            self.condition = int(self.condition_var.get())
            self.debug = self.debug_mode_var.get()
            self.time_left = self.m * 60 + self.s - 1
            if self.debug == 'ON':
                self.time_left = 1 * 13
            self.countdown_time = 0
            self.n_mode = int(self.mode_dropdown.get())
            
            self.current_directory = os.path.dirname(os.path.abspath(__file__))
            print(self.current_directory)
            
            file_path = os.path.join(self.current_directory, DataBase.json_file)
            if not os.path.exists(file_path):
                print('json database file doesn\'t exist, creating...')
                with open(file_path, 'w') as json_file:
                    json_file.write(json.dumps([], indent=4))
                print('json database file created successfully.')
            
            file_path = os.path.join(self.current_directory, DataBase.csv_file)
            if not os.path.exists(file_path):
                print('csv database file doesn\'t exist, creating...')
                with open(file_path, 'w') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=key_headers)
                    writer.writeheader()
                print('csv database file created successfully.')
            
            self.close_login_window()
            
if __name__ == '__main__':
    l = Login_window()
    l.run()
    