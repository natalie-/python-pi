#!/usr/bin/python

# This program will blink an LED at an interval for a set number of times. 
# The LED defaults to *OFF* !!!

import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

GPIO.setup(17,GPIO.OUT)

count = 0

countmax = input("How many times to blink?   ", )
countmax = int(countmax)
interval = input("How long should each blink be? (milliseconds)   ", )
interval = int(interval) / 1000

while count < countmax:
    GPIO.output(17,GPIO.HIGH)  # LED off
    time.sleep(interval)
    GPIO.output(17,GPIO.LOW)   # LED on
    time.sleep(interval)
    count = count + 1

GPIO.cleanup(17)   # clean the channel
exit(0)
