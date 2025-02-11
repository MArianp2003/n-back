import tkinter as tk
from tkinter import messagebox
from config import *
from process import *
import random
from datetime import datetime
import subprocess
import sys

try:
    import pygame
except ImportError:
    print("pygame not found. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])
    import pygame  # Import again after installation
    print("pygame installed successfully.")



class Test_Window:
    def __init__(self, name, frequency, condition, countdown_time, n_mode, time_left, mp3_file, debug):
        pygame.mixer.init()
        self.name = name
        self.frequency = frequency
        self.condition = condition
        self.countdown_time = countdown_time
        self.n_mode = n_mode
        self.time_left = time_left
        self.force_quit = False
        self.mp3_file = mp3_file
        self.debug = debug
                
        self.new_number_lock = False
        self.latencies_at_time = list()
        self.data = list()
        self.latencies = list()
        self.catch = dict()
        self.index_color = 0
        self.color_list = [Color.green, Color.black]
        
        
        self.__set_widgets_on_condition(self.condition)
        
    def __set_widgets_on_condition(self, condition):
        self.root = tk.Tk()
        self.root.title('Test Program')
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.focus_force()
        self.root.update()
        # self.root.geometry('600x600')
        self.root.configure(background=Color.green)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.bind('<space>', self.take_action)

        # self.test_frame = tk.Frame(
        #     master=self.root,
        #     background=Color.green,
        #     pady=30,
        #     padx=15,
        # )
        
        self.number_label = tk.Label(
            master=self.root, 
            text="Ready?",
            font=('Arial', 200),
            pady=60,
            background=Color.green,
            foreground=Color.black,
        )
        
        self.check_button = tk.Button(
            master=self.root,
            text='Check',
            font=('Arial', 14),
            width = 25, 
            height = 5,
            bg = "#87CEEB", #light blue
            relief = "ridge", 
            borderwidth=4,
            activebackground='yellow',
            activeforeground='black',
            command=self.click_button,
        )
        
        self.message_label = tk.Label(
            master=self.root,
            text="", 
            font=("Arial", 45),
            background=Color.green,
            foreground=Color.white
        )

        match condition:
            case 1:
                self.__start_task()
            case 2:
                self.play_condition()
                self.__start_task()
            case 3 | 4:
                self.interval = int(1000 / (2 * self.frequency))
                self.root.configure(background=Color.black)
                self.play_condition()
                if self.debug == 'ON':
                    self.root.after(2 * 1000, lambda: self.flicker_30sec(self.root)) # 2 last seconds flicker and 4 seconds black screen in debug mode 
                    self.root.after(4 * 1000, self.start_condition_3)
                elif self.debug == 'OFF':
                    self.root.after(Time.black_screen - Time.flicker_in_black, lambda: self.flicker_30sec(self.root)) # 9 min and 30 seconds black
                    self.root.after(Time.black_screen, self.start_condition_3)
                
                
    def start_condition_3(self):
        if self.condition == 3:
            self.stop_condition()
        self.__start_task()
        
    def __start_task(self):
        self.number_label.place(relx=0.5, rely=0.3, anchor='center')
        self.check_button.place(relx=0.5, rely=0.8, anchor='center')
        self.message_label.place(relx=0.5, rely=0.9, anchor='center')
        
        # self.number_label.pack(side='top')
        # self.check_button.pack()
        # self.message_label.pack()
        # self.test_frame.place(relx=0.5, rely=0.6, anchor='center')
        self.number_label.after(1000, self.start_counting)


    
    def start_counting(self):
        if self.condition in [2, 4]:
            self.interval = int(1000 / (2 * self.frequency))
            self.flicker(self.root)
            self.flicker(self.number_label)
            self.flicker(self.message_label)
        self.check_button.config(state='normal')
        self.number_label.config(fg=Color.white)
        self.data = self.generate_sequence()
        self.data_index = 0
        self.update_timer()
        self.start_show_number()

    def update_timer(self):
        if self.countdown_time < self.time_left:
            self.countdown_time += 1
            self.root.after(1000, self.update_timer)
        elif not self.force_quit:
            if self.condition in [2, 4]:
                self.stop_condition()
            self.result = check_all_n_back(self.name, self.data[:self.data_index], self.catch, self.time_left, self.n_mode)
            self.number_label.config(font=('Arial', 100))
            self.number_label.config(fg=Color.black)
            self.number_label.config(text='Thank You!')
            self.number_label.after(1000, self.close_Test_Window)

    def start_show_number(self):
        if self.countdown_time < self.time_left - 1:
            random_number = self.generate_and_set()
            self.number_label.config(text=str(random_number))
            self.new_number_lock = False
            self.d1 = datetime.now()
            self.root.after(Number_prop.show_wait, lambda: self.number_label.config(text=''))
            self.number_label.after(Number_prop.sleep_wait, self.start_show_number)

    def generate_and_set(self):
        random_number = self.data[self.data_index]
        self.data_index += 1
        return random_number
        

    def generate_sequence(self):
        # Define the chunks for match positions
        positions = list(range(4, 93))  # Positions 4 to 92 inclusive
        chunk1 = positions[:18]    # 4-21 (18 positions)
        chunk2 = positions[18:36]  # 22-39
        chunk3 = positions[36:54]  # 40-57
        chunk4 = positions[54:72]  # 58-75
        chunk5 = positions[72:]    # 76-92 (17 positions)
        
        # Select 4 positions from each chunk
        match_positions = []
        for chunk in [chunk1, chunk2, chunk3, chunk4, chunk5]:
            selected = random.sample(chunk, 4)
            match_positions.extend(selected)
        
        match_positions.sort()  # Sort for ordered processing
        
        # Generate the sequence
        sequence = [None] * 93
        for i in range(93):
            if i in match_positions:
                sequence[i] = sequence[i-4]
            else:
                if i < 4:
                    sequence[i] = random.randint(0, 9)
                else:
                    prev = sequence[i-4]
                    available = [num for num in range(10) if num != prev]
                    sequence[i] = random.choice(available)
        
        # Validation checks
        assert len(sequence) == 93, "Sequence length is incorrect."
        count = sum(1 for i in range(4, 93) if sequence[i] == sequence[i-4])
        assert count == 20, f"Found {count} 4-backs instead of 20."
        return sequence
    
    # Validate the sequence
    @staticmethod
    def validate_sequence():
        sequence = Test_Window.generate_sequence()
        print("Generated Sequence:", sequence)
        print("Length:", len(sequence))
        print("4-back Count:", sum(1 for i in range(4, 93) if sequence[i] == sequence[i-4]))

    
    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Are you sure you want to quit?'):
            self.force_quit = True
            self.close_Test_Window()
    
    def take_action(self, event):
        self.d2 = datetime.now()
        original_color = self.check_button.cget('bg')
        self.check_button.config(bg='yellow')
        self.check_button.after(100, lambda: self.check_button.config(bg=original_color))    
        if self.data_index < self.n_mode + 1:
            self.message_label.config(text= 'lack of data for test n-back')
        else:
            index = self.data_index - self.n_mode - 1
            if not self.new_number_lock:
                self.new_number_lock = True
                self.message_label.config(text=f'Check submitted!')
                self.seq = self.data[index:self.data_index]
                self.elapsed_time = (self.d2 - self.d1).total_seconds()
                self.latencies_at_time = self.countdown_time
                self.catch.update({index: (
                    self.seq, 
                    f'{self.latencies_at_time // 60:02}:{self.latencies_at_time % 60:02}',
                    round(self.elapsed_time, DigitRound.digit_round)    
                )})
        self.message_label.after(1000, lambda: self.message_label.config(text=''))
        

    def flicker(self, widget):
    
        if self.countdown_time >= self.time_left:
            widget.config(bg=Color.green)
            return
        current_color = widget.cget('bg')
        next_color = self.color_list[1 - self.color_list.index(current_color)]
        widget.config(bg=next_color)
            
        # elif isinstance(widget, tk.Label):
        #     if self.countdown_time >= self.time_left:
        #         widget.config(fg=Color.black)
        #         return
        #     current_color = widget.cget('fg')
        #     next_color = self.color_list_label[1 - self.color_list_label.index(current_color)]
        #     widget.config(fg=next_color)
            
        widget.after(self.interval, lambda: self.flicker(widget))

    def flicker_30sec(self, widget, sec=0):
        if self.debug == 'ON':
            if sec >= 2 * 1000:
                widget.configure(background=Color.green)
                return
            current_color = widget.cget('bg')
            next_color = self.color_list[1 - self.color_list.index(current_color)]
            widget.config(bg=next_color)
            widget.after(self.interval, lambda: self.flicker_30sec(widget, sec + self.interval))

        elif self.debug == 'OFF':
            if sec >= Time.flicker_in_black:
                widget.configure(background=Color.green)
                return
            current_color = widget.cget('bg')
            next_color = self.color_list[1 - self.color_list.index(current_color)]
            widget.config(bg=next_color)
            widget.after(self.interval, lambda: self.flicker_30sec(widget, sec + self.interval))
            
    def play_condition(self):
        if self.mp3_file:
            try:
                pygame.mixer.music.load(self.mp3_file)
                pygame.mixer.music.play()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to play file:\n{e}")

    def stop_condition(self):
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop music:\n{e}")

    def click_button(self):
        self.take_action(event=None)

    def run(self):
        self.root.mainloop()
    
    def close_Test_Window(self):
        self.root.destroy()
    

if __name__ == '__main__':
    test = Test_Window()
    test.run()
