# name: led_bar_random.py
#
# Este programa acende e apaga aleatoriamente uma posição no Led Bar.

import RPi.GPIO as GPIO
import time
import random

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

GPIO.setmode(GPIO.BOARD)

for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin, GPIO.HIGH)

while True:

    ledPosition = random.randint(0, 9)
    ledStatus   = random.randint(0, 1)
    
    if (ledStatus == 0):
        GPIO.setup(ledPins[ledPosition], GPIO.LOW)
    else:
        GPIO.setup(ledPins[ledPosition], GPIO.HIGH)  
    time.sleep(0.1)

GPIO.cleanup()
