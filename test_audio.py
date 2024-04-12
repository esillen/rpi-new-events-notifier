from time import sleep
import os
import pygame
from common import AUDIO_CLIPS


pygame.mixer.init(buffer=1024)
pygame.mixer.music.set_volume(1.0)


def play_audio(clip):
    filepath = os.path.join(os.path.dirname(__file__), 'clips', clip)
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

for clip in AUDIO_CLIPS:
    print(clip)
    play_audio(clip)
    sleep(7)
print()