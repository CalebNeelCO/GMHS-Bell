import datetime
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
time.sleep(2)
GPIO.output(18,GPIO.LOW)

dict1 = {
1: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"},
2: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"},
3: {9:"20", 10:"05", 11:"30", 12:"05", 1:"30"},
4: {9:"20", 10:"45", 11:"25", 12:"45", 2:"10", 3:"00"},
5: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"}}

# I WAS ABLE TO GET THE LIGHT TO FLASH FOR THREE SECONDS AND TURN OFF
# BY IMPORTING TIME IN THE ACTUAL FUNCTION BUT I COULDN'T FIGURE OUT THE BUZZER


c = True
while c:
    time = datetime.datetime.now()
    day = time.weekday() + 1
    hour = time.hour
    mini = time.minute
    import time
    for i in dict1[day]:
        if(hour == i):
            if(mini == int(dict1[day][i])):
                print("test")
                GPIO.output(18,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(18,GPIO.LOW)
                time.sleep(60)
