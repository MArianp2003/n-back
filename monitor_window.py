import tkinter as tk
from tkinter import messagebox
from config import *
import json
import os


class Monitor_Window:
    
    def __init__(self):
        self.file_exist = os.path.exists(DataBase.json_file) 
        if not self.file_exist:
            messagebox.showinfo(title='NO DATABASE FILE', message="There is no database json file in this directory, after this info, window will be close.")
        else:
            with open(DataBase.json_file, 'r') as json_file:
                self.raw_data = json.load(json_file)
            self.__set_widgets()
        
    def __set_widgets(self):
        
        self.root = tk.Tk()
        self.root.title('The result')
        self.root.geometry('600x400')

        # Create the frame and center it within the root window
        self.frame = tk.Frame(
            master=self.root
        )
        self.frame.pack(expand=True)  # This will center the frame

        # Row 0: name
        self.name_label = tk.Label(
            master=self.frame,
            text='Name:', 
            font=('Arial', 14, 'bold')
        )
        self.name_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
        )

        # Row 1: hit
        self.hit_label = tk.Label(
            master=self.frame, 
            text='Hit:', 
            font=('Arial', 14, 'bold')
        )
        self.hit_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14),
            state='readonly'
        )

        # Row 2: false_alarm
        self.false_alarm_label = tk.Label(
            master=self.frame, 
            text='false_alarm:', 
            font=('Arial', 14, 'bold')
        )
        self.false_alarm_entry = tk.Entry(
            self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 3: miss
        self.miss_label = tk.Label(
            self.frame, 
            text='miss:', 
            font=('Arial', 14, 'bold')
        )
        self.miss_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 4: correct_rejection
        self.correct_rejection_label = tk.Label(
            master=self.frame, 
            text='correct_rejection:', 
            font=('Arial', 14, 'bold')
        )
        self.correct_rejection_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 5: at_times
        self.at_times_label = tk.Label(
            master=self.frame,
            text='At times:',
            font=('Arial', 14, 'bold'),
        )
        self.at_times_entry = tk.Entry(
            master=self.frame,
            font=('Arial', 14),
            state='readonly',
        )
        
        # Row 6: latencies
        self.latencies_label = tk.Label(
            master=self.frame, 
            text='Latencies:', 
            font=('Arial', 14, 'bold')
        )
        self.latencies_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )
        
        # Row 7: time duration
        self.time_duration_label = tk.Label(
            master=self.frame,
            text='Time_duration:',
            font=('Arial', 14, 'bold'),
        )
        self.time_duration_entry = tk.Entry(
            master=self.frame,
            font=('Arial', 14),
            state='readonly',
        )

        # Row 8: mode
        self.mode_label = tk.Label(
            master=self.frame,
            text='Mode:',
            font=('Arial', 14, 'bold'),
        )
        self.mode_entry = tk.Entry(
            master=self.frame,
            font=('Arial', 14),
            state='readonly',
        )

        # Row 9: search button spanning two columns
        self.search_button = tk.Button(
            master=self.frame, 
            text="Search", 
            font=("Helvetica", 12), 
            width=25, 
            bg='#71F5BC',
            command=self.search
        )

        self.name_label.grid(row=0, column=0, sticky='e')
        self.name_entry.grid(row=0, column=1, padx=10)
        self.hit_label.grid(row=1, column=0, sticky='e')
        self.hit_entry.grid(row=1, column=1, padx=10)
        self.false_alarm_label.grid(row=2, column=0, sticky='e')
        self.false_alarm_entry.grid(row=2, column=1, padx=10)
        self.miss_label.grid(row=3, column=0, sticky='e')
        self.miss_entry.grid(row=3, column=1, padx=10)
        self.correct_rejection_label.grid(row=4, column=0, sticky='e')
        self.correct_rejection_entry.grid(row=4, column=1, padx=10)
        self.at_times_label.grid(row=5, column=0, sticky='e')
        self.at_times_entry.grid(row=5, column=1, padx=10)
        self.latencies_label.grid(row=6, column=0, sticky='e')
        self.latencies_entry.grid(row=6, column=1, padx=10)
        self.time_duration_label.grid(row=7, column=0, sticky='e')
        self.time_duration_entry.grid(row=7, column=1, padx=10)
        self.mode_label.grid(row=8, column=0, sticky='e')
        self.mode_entry.grid(row=8, column=1, padx=10)
        self.search_button.grid(row=9, column=0, columnspan=2, pady=10)
        
        self.root.bind('<Return>', func=self.search_key)
        self.root.protocol('WM_DELETE_WINDOW', func=self.on_closing)
        
    def set_and_set(self, widget, d):
        widget.config(state='normal')
        widget.delete(0, tk.END)
        widget.insert(0, d)
        widget.config(state='readonly')
        
    def search_key(self, event):
        self.search()
        
    def search(self):
        not_found = True
        for item in self.raw_data:
            if not not_found:
                break
            if self.name_entry.get() == item.get('name'):
                not_found = False
                self.set_and_set(self.hit_entry, item.get('hit'))
                self.set_and_set(self.false_alarm_entry, item.get('false_alarm'))
                self.set_and_set(self.miss_entry, item.get('miss'))
                self.set_and_set(self.correct_rejection_entry, item.get('correct_rejection'))
                all_times = list()
                all_latencies = list()
                for value in item.get('hit_catched').values():
                    seq, time, latency = value
                    all_times.append(time)
                    all_latencies.append(str(latency))
                all_times_in_str = ', '.join(all_times)
                all_latencies_in_str = ', '.join(all_latencies)
                self.set_and_set(self.at_times_entry, all_times_in_str or 'None')
                self.set_and_set(self.latencies_entry, all_latencies_in_str or 'None')
                self.set_and_set(self.time_duration_entry, item.get('time_duration'))
                self.set_and_set(self.mode_entry, item.get('mode'))
                max_len = len(all_times_in_str)
                self.set_width_all_entries(max_len)
                
                
        if not_found:
            messagebox.showinfo('Search Failed', message=f'There is not information about {self.name_entry.get()}')
    
    def run(self):
        self.root.mainloop()
    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.close_Monitor_Window()

    def close_Monitor_Window(self):
        self.root.destroy()
        
    def set_width_all_entries(self, l):
        l = max(10, l)
        self.name_entry.config(width=l)
        self.hit_entry.config(width=l)
        self.false_alarm_entry.config(width=l)
        self.miss_entry.config(width=l)
        self.correct_rejection_entry.config(width=l)
        self.at_times_entry.config(width=l)
        self.latencies_entry.config(width=l)
        self.time_duration_entry.config(width=l)
        self.mode_entry.config(width=l)
        

if __name__ == '__main__':
    m = Monitor_Window()
    if m.file_exist:
        m.run()
