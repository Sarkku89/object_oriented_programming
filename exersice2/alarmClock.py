#File name: alarmClock.py
#Author: Sarianna Junnila
#Description: Super simple alarm clock with objects.

import time

# Initializing the alarm time and current time

class AlarmClock:
    def __init__(self):
        self.alarm_hours = int(input("Give the hours for alarm (HH): "))
        self.alarm_minutes = int(input("Give the minutes for alarm (MM): "))
        self.time_now = time.strftime('%H:%M')

# Slicing the current time string and comparing it to the alarm time every 1 second

    def alarm(self):
        while True:
            time.sleep(1)
            #self.time_now = time.strftime('%H:%M')
            self.hours = int(self.time_now[0:2])
            self.minutes = int(self.time_now[3:5])
            print (time.strftime('%H:%M:%S') )
            if self.hours == self.alarm_hours:
                if self.minutes == self.alarm_minutes:
                    print ("Time to wake up!")
                    break

# Main function 
                  
def main():
    my_alarm = AlarmClock()
    my_alarm.alarm()
    

main()
    