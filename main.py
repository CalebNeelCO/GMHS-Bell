import datetime
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)

T = 5 #Time Before Bell

dict1 = {
1: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"},
2: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"},
3: {9:"20", 10:"05", 11:"30", 12:"05", 1:"30"},
4: {9:"20", 10:"45", 11:"25", 12:"45", 2:"10", 3:"00"},
5: {8:"50", 9:"45", 10:"45", 11:"40", 12:"20", 1:"10", 2:"05", 3:"00"}}

while True:
    GPIO.output(18,GPIO.HIGH)
    time = datetime.datetime.now()
    day = time.weekday() + 1
    hour = time.hour
    mini = time.minute
    import time
    for i in dict1[day]:
        if(hour == i):
            if(mini == int(dict1[day][i])-T):
                GPIO.output(18,GPIO.HIGH)
                time.sleep(3)
                GPIO.output(18,GPIO.LOW)
                time.sleep(60)
