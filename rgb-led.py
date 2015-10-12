#!/usr/bin/python

# This program will blink a single RGB LED different colors 10 times, then exit.
# The LED defaults to *OFF* !!!

# 17 = red
# 18 = green
# 27 = blue


import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17, 18, 27], GPIO.OUT)

# Turn LED off
GPIO.output([17, 18, 27], GPIO.LOW)

# Set up interval to blink
interval = 0.5
count = 0

# Blink red, green, blue, white
while count <= 10:
    GPIO.output(17, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(27, GPIO.LOW)
    GPIO.output([17, 18, 27], GPIO.HIGH)
    time.sleep(interval)
    GPIO.output([17, 18, 27], GPIO.LOW)
    count = count + 1

# Finish
GPIO.output([17, 18, 27], GPIO.LOW)
GPIO.cleanup([17, 18, 27])   # clean the channels
exit(0)
