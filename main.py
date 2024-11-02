from window import Window
from monitor_result import Monitor_Window

def main():
    w = Window()
    w.run()
    if not w.forcequit:
        monitor = Monitor_Window()
        monitor.run()
    
if __name__ == '__main__':
    main()