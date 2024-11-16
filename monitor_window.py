import tkinter as tk
from tkinter import messagebox
import json
from config import key_headers

class Monitor_Window:
    
    def __init__(self):
        with open('database.json', 'r') as json_file:
            self.raw_data = json.load(json_file)
        self.__set_widgets()
        
    def __set_widgets(self):
        
        self.root = tk.Tk()
        self.root.title('The result')
        self.root.geometry('400x400')

        # Create the frame and center it within the root window
        self.frame = tk.Frame(
            master=self.root
        )
        self.frame.pack(expand=True)  # This will center the frame

        # Row 0: name
        self.name_label = tk.Label(
            master=self.frame,
            text='name:', 
            font=('Arial', 14, 'bold')
        )
        self.name_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
        )

        # Row 1: data
        self.data_label = tk.Label(
            master=self.frame, 
            text='data:', 
            font=('Arial', 14, 'bold')
        )
        self.data_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 2: latencies
        self.latencies_label = tk.Label(
            master=self.frame, 
            text='latencies:', 
            font=('Arial', 14, 'bold')
        )
        self.latencies_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 3: correct
        self.correct_label = tk.Label(
            master=self.frame, 
            text='correct:', 
            font=('Arial', 14, 'bold')
        )
        self.correct_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14),
            state='readonly'
        )

        # Row 4: incorrect
        self.incorrect_label = tk.Label(
            master=self.frame, 
            text='incorrect:', 
            font=('Arial', 14, 'bold')
        )
        self.incorrect_entry = tk.Entry(
            self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 5: uncatched
        self.uncatched_label = tk.Label(
            self.frame, 
            text='uncatched:', 
            font=('Arial', 14, 'bold')
        )
        self.uncatched_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 6: other
        self.other_label = tk.Label(
            master=self.frame, 
            text='other:', 
            font=('Arial', 14, 'bold')
        )
        self.other_entry = tk.Entry(
            master=self.frame, 
            font=('Arial', 14), 
            state='readonly'
        )

        # Row 7: search button spanning two columns
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
        self.data_label.grid(row=1, column=0, sticky='e')
        self.data_entry.grid(row=1, column=1, padx=10)
        self.latencies_label.grid(row=2, column=0, sticky='e')
        self.latencies_entry.grid(row=2, column=1, padx=10)
        self.correct_label.grid(row=3, column=0, sticky='e')
        self.correct_entry.grid(row=3, column=1, padx=10)
        self.incorrect_label.grid(row=4, column=0, sticky='e')
        self.incorrect_entry.grid(row=4, column=1, padx=10)
        self.uncatched_label.grid(row=5, column=0, sticky='e')
        self.uncatched_entry.grid(row=5, column=1, padx=10)
        self.other_label.grid(row=6, column=0, sticky='e')
        self.other_entry.grid(row=6, column=1, padx=10)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=20)
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
        widgets = [ 
            self.data_entry, 
            self.latencies_entry, 
            self.correct_entry, 
            self.incorrect_entry, 
            self.uncatched_entry, 
            self.other_entry
        ]
        not_found = True
        for item in self.raw_data:
            if not not_found:
                break
            if self.name_entry.get() == item.get('name'):
                not_found = False
                for widget, name in zip(widgets, key_headers[1:]):
                    self.set_and_set(widget, item.get(name))
                
        if not_found:
            messagebox.showinfo('Search Failed', message=f'There is not information about {self.name_entry.get()}')
    
    def run(self):
        self.root.mainloop()
    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.close_Monitor_Window()

    def close_Monitor_Window(self):
        self.root.destroy()
        
