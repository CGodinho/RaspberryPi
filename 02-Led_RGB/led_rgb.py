# name: leg_rgb.py

# Este programa controla um led RGB atráves de 3 portos específicos.
# Usa a biblioteca random para gerar numeros aleatórios que vão
# corrsponder a diferentes combinações de cor.

import RPi.GPIO as GPIO
import time
import random

pinRed    = 11
pinGreen  = 12
pinBlue   = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinRed,   GPIO.OUT)
GPIO.setup(pinGreen, GPIO.OUT)
GPIO.setup(pinBlue,  GPIO.OUT)

GPIO.output(pinRed,   GPIO.HIGH)
GPIO.output(pinGreen, GPIO.HIGH)
GPIO.output(pinBlue,  GPIO.HIGH)

portRed   = GPIO.PWM(pinRed,   2000)
portGreen = GPIO.PWM(pinGreen, 2000)
portBlue  = GPIO.PWM(pinBlue,  2000)
portRed.start(0)
portGreen.start(0)
portBlue.start(0)

while True:
    redValue = random.randint(0, 100)
    greenValue = random.randint(0, 100)
    blueValue = random.randint(0, 100)  
    portRed.ChangeDutyCycle(redValue)
    portGreen.ChangeDutyCycle(greenValue)
    portBlue.ChangeDutyCycle(blueValue)
    print("(R,G,B) = (" + str(redValue) + "," + str(greenValue) +"," + str(blueValue) + ")")
    time.sleep(5)

portRed.stop()
portGreen.stop()
portBlue.stop()

GPIO.cleanup()