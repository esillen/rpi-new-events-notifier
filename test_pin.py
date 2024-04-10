from time import sleep
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

BLINK_TIME_SECONDS = 2
PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:  
    while True: 
        print("on") 
        GPIO.output(PIN, GPIO.LOW) 
        sleep(BLINK_TIME_SECONDS)
        print("off")
        GPIO.output(PIN, GPIO.HIGH)
        sleep(BLINK_TIME_SECONDS)
  
except KeyboardInterrupt:
    GPIO.cleanup()
