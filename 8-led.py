#!/usr/bin/python

# This program will blink LEDs left to right.

# At some point, add control using the run variable within the while loop.
# Until then, CTRL-C to exit.  (24 Feb 15)

import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17, 18, 27, 22, 23, 24, 25, 4], GPIO.OUT)

# Turn all LEDs off
GPIO.output([17, 18, 27, 22, 23, 24, 25, 4], GPIO.HIGH)

# Set run conditions (maybe use this for control later)
count = 0
interval = 0.5
countmax = 1

# Blink left to right
while count < countmax:
    GPIO.output(17, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(27, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(25, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)

# Finish
GPIO.cleanup([17, 18, 27, 22, 23, 24, 25, 4])   # clean the channels
exit(0)
