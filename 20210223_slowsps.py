# 20210223 - Slow Scissors Paper Stone
# In this code, it checks for gestures but it does not count "mini-shakes".

from microbit import *
import random

scissors = Image("99099:99099:00900:09090:90009")

while True:
    if accelerometer.was_gesture("shake"):
        hand=str(random.randint(1,3))
        if hand == "1":
            display.show(Image.SQUARE)
        elif hand=="2":
            display.show(Image.SQUARE_SMALL)
        else:
            display.show(scissors)
