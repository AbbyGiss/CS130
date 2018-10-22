###########################################################################################
# Name: Abby Gissendanner
# Date: 10-20-18
# Description: Makes the LED blink
###########################################################################################
import RPi.GPIO as GPIO
from time import sleep

led = 17
button = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    if (GPIO.input(button) == GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)
    else:
        GPIO.output(led, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        sleep(0.5)