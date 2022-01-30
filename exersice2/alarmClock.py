#File name: alarmClock.py
#Author: Sarianna Junnila
#Description: Super simple alarm clock with objects.

import time

# Initializing the alarm time and current time as attributes for the class

class AlarmClock:
    def __init__(self, alarm_hours, alarm_minutes, time_now):
        self.alarm_hours = alarm_hours
        self.alarm_minutes = alarm_minutes
        self._time_now = time_now


# Slicing the current time string and comparing it to the alarm time every 1 second

    def alarm(self):
        while True:
            time.sleep(1)
            self.time_now = time.strftime('%H:%M')
            self.hours = int(self.time_now[0:2])
            self.minutes = int(self.time_now[3:5])
            print (time.strftime('%H:%M:%S') )
            if self.hours == self.alarm_hours:
                if self.minutes == self.alarm_minutes:
                    print ("Time to wake up!")
                    snoozing = input("You want to sleep 5 minutes longer? y/n ")
                    if snoozing == "y":
                        self.alarm_minutes += 5
                        continue
                    else:                    
                        break


# Main function defines the attributes for the instance 
                  
def main():
    my_alarm = AlarmClock( 
    alarm_hours = (int(input("Give the hours for alarm (HH): "))),
    alarm_minutes = (int(input("Give the minutes for alarm (MM): "))),
    time_now = (time.strftime('%H:%M')))
    my_alarm.alarm()
    

main()
    