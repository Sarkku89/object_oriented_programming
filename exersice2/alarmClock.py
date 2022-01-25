"""Code the alarm clock, use objects.
This is also supposed to be a simple task, so do not makeit unnecessarily complicated. 
Alarm can simply be a text output on screen. 
No sounds are needed (can be added if you wish).
If this is too difficult, code a timer instead.
"""
import time
import tkinter


class AlarmClock:
    def __init__(self, main_window):
        self.main_window = main_window
        self.clock_label = tkinter.Label(self.main_window, font = ('arial', 80), bg = 'black', fg='red')
        self.display_time()

    def display_time(self):
        self.time_now = time.strftime('%H:%M:%S')
        self.clock_label = self.time_now
        self.main_window.after(200, self.display_time)

main_window = tkinter.Tk()
my_alarm_clock = AlarmClock(main_window)
main_window.mainloop()