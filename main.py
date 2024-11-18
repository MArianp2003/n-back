from test_window import Test_Window
from monitor_window import Monitor_Window
from config import MonitorMode
def main():
    match MonitorMode.run_mode:
        case 'test':
            w = Test_Window()
            w.run()
        case 'monitor':
            m = Monitor_Window()
            m.run()
    
if __name__ == '__main__':
    main()