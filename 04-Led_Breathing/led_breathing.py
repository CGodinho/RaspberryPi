# name: leg_breathing.py

# Este programa usa modelação de frequência para controlar um led.
# A luz acende e apaga progressivamente, simulando um sinal analógico.

import RPi.GPIO as GPIO
import time
import random

ledPin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
cycle = GPIO.PWM(ledPin, 1000)
cycle.start(0)


while True:
    for dutyCycle in range(0, 101, 1):
        cycle.ChangeDutyCycle(dutyCycle)
        time.sleep(0.05)

    time.sleep(1)

    for dutyCycle in range(100, -1, -1):
        cycle.ChangeDutyCycle(dutyCycle)
        time.sleep(0.05)
    time.sleep(1)
    

cycle.stop()
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()
