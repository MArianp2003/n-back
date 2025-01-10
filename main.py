from test_window import Test_Window
from monitor_window import Monitor_Window
from login_window import Login_window
from config import MonitorMode

if __name__ == '__main__':

    match MonitorMode.run_mode:
        case 'test':
            #login window opens
            lw = Login_window()
            lw.run()
    
            if not lw.mquit:
                #after login window gets the data and starts the task
                tw = Test_Window(lw.name, lw.frequency, lw.condition, lw.countdown_time, lw.n_mode, lw.time_left, lw.mp3_file, lw.debug)
                tw.run()

        case 'monitor':
            m = Monitor_Window()
            m.run()
