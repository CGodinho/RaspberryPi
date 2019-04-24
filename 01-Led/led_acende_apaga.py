# este programa foi comcebido para acender e apagar um led infinitamente
# acende o led durante 10 seg e apaga seguidamente durante 5 seg
# 

import RPi.GPIO as GPIO
import time

ledPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    GPIO.output(ledPin, GPIO.HIGH)
    print("Acender")
    time.sleep(10)
    print("Apagar")
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(5)

GPIO.cleanup()
