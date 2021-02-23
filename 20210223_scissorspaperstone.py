# 20210223 - Scissors Paper Stone
# This code has a minor change. Rather than using ARROW_W as the "Scissors" image, I have defined a variable called scissors, and in the variable it shows an image which looks more like a scissors.

from microbit import *
import random

scissors = Image("99099:99099:00900:09090:90009")

while True:
    gesture = accelerometer.current_gesture()
    if gesture=="shake":
        hand=str(random.randint(1,3))
        if hand == "1":
            display.show(Image.SQUARE)
        elif hand=="2":
            display.show(Image.SQUARE_SMALL)
        else:
            display.show(scissors)
