import webbrowser
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35,GPIO.IN)
GPIO.setup(37,GPIO.IN)

while True:
    if GPIO.input(35)==1:
        webbrowser.open('http://mycampus365.com/farmvilla/update.php?id=0')
        time.sleep(5)
        os.system("killall chromium-browser")
        print("id=0")
    elif GPIO.input(37)==1:
        webbrowser.open('http://mycampus365.com/farmvilla/update.php?id=1')
        time.sleep(5)
        os.system("killall chromium-browser")
        print("id=1")
    
GPIO.cleanup()
