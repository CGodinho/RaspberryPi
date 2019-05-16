import RPi.GPIO as GPIO
import time
import math

buzzerPin = 11
buttonPin = 12

    
global portBuzzer


def alertor():
    portBuzzer.start(50)
    for x in range(0, 361):
        sinVal = math.sin(x * (math.pi / 180.0))
        toneVal = 2000 + sinVal * 500
        portBuzzer.ChangeFrequency(toneVal)
        time.sleep(0.001)

def stopAlertor():
    portBuzzer.stop()
    

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzerPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
portBuzzer = GPIO.PWM(buzzerPin, 1)
portBuzzer.start(0)

while True:
    if GPIO.input(buttonPin) == GPIO.LOW:
        alertor()
    else:
        stopAlertor()


GPIO.output(buzzerPin, GPIO.LOW)
GPIO.cleanup()





