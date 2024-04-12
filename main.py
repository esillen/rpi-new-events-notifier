from time import sleep
import os
import requests
import pygame
import random
from common import AUDIO_CLIPS
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


pygame.mixer.init(buffer=1024)
pygame.mixer.music.set_volume(1.0)

NOTIFICATION_TIME_SECONDS = 15
POLL_TIME_SECONDS = 10
PIN = 24
URL = 'http://mysite.com/event_endpoint'
URL_DEV = "http://localhost:5000/event_endpoint"
if 'RPI_EVENT_URL' in os.environ:
    URL = os.environ['RPI_EVENT_URL']
if 'RPI_EVENT_URL_DEV' in os.environ:
    URL_DEV = os.environ['RPI_EVENT_URL_DEV']
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

def play_random_audio():
    random_clip = random.choice(AUDIO_CLIPS)
    filepath = os.path.join(os.path.dirname(__file__), 'clips', random_clip)
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

def notify():
    play_random_audio()
    GPIO.output(PIN, GPIO.LOW)
    sleep(NOTIFICATION_TIME_SECONDS)
    GPIO.output(PIN, GPIO.HIGH)


# Get initial hashes
while True:
    try:
        lastHash = requests.get(URL).text
        print("hash", lastHash)
        lastHashDev = requests.get(URL_DEV).text
        print("hashDev", lastHashDev)
        break
    except:
        pass

# Just notifying that it has started and is up and hasn't run into a problem yet
print("starting")
GPIO.output(PIN, GPIO.LOW)
sleep(2)
GPIO.output(PIN, GPIO.HIGH)

while True:
    try:
        hash = requests.get(URL).text
        print("hash", lastHash)
        hashDev = requests.get(URL_DEV).text
        print("hashDev", lastHashDev)
        if hash != lastHash or hashDev != lastHashDev:
            print("new hash!")
            notify()
            lastHash = hash
            lastHashDev = hashDev
    except:
        pass
    sleep(POLL_TIME_SECONDS)
