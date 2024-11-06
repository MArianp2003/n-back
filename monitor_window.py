import tkinter as tk
import json
import os

class Monitor_Window:
    
    def __init__(self):
        with open('database.json', 'r') as json_file:
            self.raw_data = json.load(json_file)
        self.__set_widgets()
        
    def __set_widgets(self):
        
        self.root = tk.Tk()
        self.root.title('The result')
        self.root.geometry('320x320')
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True)
        
        self.name_label = tk.Label(
            master=self.frame,
            padx=10,
            font=('Arial', 14, 'bold'),
            text=''
        )
        
        self.name_text = tk.Entry(
            master=self.frame,
            width=20,
            font=('Arial', 18)
            
        )
 
        
        # for i, (key, value) in enumerate(self.raw_data.items()):

        #     key_label = tk.Label(self.frame, text=f"{key.capitalize()}:", font=('Arial', 14, 'bold'))
        #     key_label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

        #     value_entry = tk.Label(self.frame, width=10, font=('Arial', 14), bg='white', fg='black')
        #     value_entry.grid(row=i, column=1, padx=10, pady=5)
        #     value_entry.config(text=str(value))
        #     value_entry.config(state='normal')
        
        os.remove('result.json')

    def run(self):
        self.root.mainloop()
        
        
def main():
    m = Monitor_Window()
    

if __name__ == '__main__':
    main()