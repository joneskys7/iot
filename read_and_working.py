while True:
    import json
    import urllib.request
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(3,GPIO.OUT)
    url = "http://mycampus365.com/farmvilla/select.php"
    x = urllib.request.urlopen(url)
    raw_data = x.read()
    encoding = x.info().get_content_charset('utf8')  # JSON default
    #print(raw_data)   #this is data in string format
    data = json.loads(raw_data.decode(encoding))
    print(data)
    if data==0:
        print("Off")
        GPIO.output(3,0)
        time.sleep(1)
    elif data==1:
        print("on")
        GPIO.output(3,1)
        time.sleep(1)
    elif data==2:
        print("2 ON")
        GPIO.output(3,0)
        time.sleep(1)
    elif data==3:
        print("2 OFF")
        GPIO.output(3,0)
        time.sleep(1)
GPIO.cleanup()
