# name: led_semaforo.py
#
# Este programa foi simula um semáforo, usando 3 leds

import RPi.GPIO as GPIO
import time

ledPinRed    = 11
ledPinYellow = 29
ledPinGreen  = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPinRed,    GPIO.OUT)
GPIO.setup(ledPinYellow, GPIO.OUT)
GPIO.setup(ledPinGreen,  GPIO.OUT)

while True:
    print("Vermelho")
    GPIO.output(ledPinRed,    GPIO.HIGH)
    GPIO.output(ledPinYellow, GPIO.LOW)
    GPIO.output(ledPinGreen,  GPIO.LOW)
    time.sleep(5)

    print("Verde")
    GPIO.output(ledPinRed,    GPIO.LOW)
    GPIO.output(ledPinGreen,  GPIO.HIGH)
    time.sleep(5)
    
    print("Amarelo")
    GPIO.output(ledPinYellow, GPIO.HIGH)
    GPIO.output(ledPinGreen,  GPIO.LOW)
    time.sleep(2)

GPIO.cleanup()
