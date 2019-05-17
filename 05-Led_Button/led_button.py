# name: led_button.py
#
# Este programa acende um led quando um botão é primido. O circutito do botão é independente do circuito do LED.

import RPi.GPIO as GPIO

ledPin    = 11
buttonPin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    if GPIO.input(buttonPin) == GPIO.LOW:
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

GPIO.output(ledPin, GPIO.LOW)
GPIO.setup(ledPin, GPIO.LOW)
