from time import sleep
from sseclient import SSEClient
import requests
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

NOTIFICATION_TIME_SECONDS = 15
POLL_TIME_SECONDS = 10
PIN = 24
URL = 'http://mysite.com/event_endpoint'
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

lastHash = ""

def notify():
    print("new message received!")
    GPIO.output(PIN, GPIO.LOW)
    sleep(NOTIFICATION_TIME_SECONDS)
    GPIO.output(PIN, GPIO.HIGH)

while True:
    try:
        response = requests.get(URL)
        hash = response.text
        if hash != lastHash:
            print("new hash!")
            lastHash = hash
    except:
        pass
    sleep(POLL_TIME_SECONDS)
