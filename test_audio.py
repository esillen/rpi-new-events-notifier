from time import sleep
import os
import pygame
from common import AUDIO_CLIPS


pygame.mixer.init(buffer=1024)
pygame.mixer.music.set_volume(1.0)
voice = pygame.mixer.Channel(0)


def play_audio(clip):
    filepath = os.path.join(os.path.dirname(__file__), 'clips', clip)
    sound = pygame.mixer.Sound(filepath)
    voice.play(sound)

for clip in AUDIO_CLIPS:
    print(clip)
    play_audio(clip)
    while voice.get_busy():
        pass
print("done")