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


pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

NOTIFICATION_TIME_SECONDS = 15
POLL_TIME_SECONDS = 10
PIN = 24
URL = 'http://mysite.com/event_endpoint'
if 'RPI_EVENT_URL' in os.environ:
    URL = os.environ['RPI_EVENT_URL']
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)

lastHash = ""


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

while True:
    try:
        response = requests.get(URL)
        hash = response.text
        if hash != lastHash:
            print("new hash!")
            print(hash)
            if (lastHash != ""):
                notify()
            lastHash = hash
    except:
        pass
    sleep(POLL_TIME_SECONDS)
GPIO.output(PIN, GPIO.HIGH)
