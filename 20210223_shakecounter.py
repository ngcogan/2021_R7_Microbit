# 20210223 - Shake Counter
# Everytime the Microbit is shaked, it will add one to the count and show the count

from microbit import *

count = 0
display.clear()
# Checking for a shake
while True:
    if accelerometer.was_gesture("shake"):
        count += 1
        display.scroll(count)
