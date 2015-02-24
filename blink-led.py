#!/usr/bin/python

# This program will blink an LED at an interval for a set number of times. 
# The LED defaults to *OFF* !!!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)

count = 0
countmax = 10
interval = 0.5

while count < countmax:
    GPIO.output(17,GPIO.HIGH)  # LED off
    time.sleep(interval)
    GPIO.output(17,GPIO.LOW)   # LED on
    time.sleep(interval)
    count = count + 1

GPIO.cleanup(17)   # clean the channel
exit(0)
