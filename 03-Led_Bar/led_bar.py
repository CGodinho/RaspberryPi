# name: led_bar_random.py
#
# Este programa acende os led bars sequencialmente.
# Uma vez todas as posições acessas, são apagados na ordem contrária.

import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

GPIO.setmode(GPIO.BOARD)

for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin, GPIO.HIGH)

while True:
    for pin in ledPins:
        GPIO.setup(pin, GPIO.LOW)
        time.sleep(1)
        GPIO.setup(pin, GPIO.HIGH)
        time.sleep(0.2)
        
    for pin in ledPins[9:0:-1]:
        GPIO.setup(pin, GPIO.LOW)
        time.sleep(1)
        GPIO.setup(pin, GPIO.HIGH)
        time.sleep(0.2)
        

for pin in ledPins:
    GPIO.setup(pin, GPIO.HIGH)

GPIO.cleanup()
