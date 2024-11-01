class Win_prop:
    resolution = (600, 600)
    title = 'N-Back Visual Program'

class Number_prop:
    font = ('Arial', 24)
    after_login_font = ('Arial', 80)
    rely = 0.4
    show_wait = 500 # ms
    sleep_wait = 2000 # ms
    
class But_prop:
    font = ('Arial', 14)
    text = 'Check',
    width = 15, 
    height = 3,
    bg = "#87CEEB",
    activebackground='yellow',
    activeforeground='black',
    relief = "ridge", 
    borderwidth = 4,
    rely = 0.7
    
class Message_prop:
    font=("Arial", 24)
    rely = 0.85

class Time:
    countdown_time = 10 * 60 # seconds 
    font=("Helvetica", 12, 'bold')