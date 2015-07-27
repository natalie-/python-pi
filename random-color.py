#!/usr/bin/python

# This program will change a single RGB LED to random colors over time, resulting in a "breathing" effect.
# The LED defaults to *OFF* !!!


import time
import random

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17,18,27],GPIO.OUT)
GPIO.output([17,18,27],GPIO.LOW)
redPin = GPIO.PWM(17,100)
greenPin = GPIO.PWM(18,100)
bluePin = GPIO.PWM(27,100)

# Initialize values for LED
redValueOld = 0
greenValueOld = 0
blueValueOld = 0
redPin.start(redValueOld)
greenPin.start(greenValueOld)
bluePin.start(blueValueOld)

# Fade to random color from previous color over 2 seconds in 100 steps
duration = 2
steps = 100
count = 0
while True:
    try:
        # Get new color
        redValue = random.randrange(0,100,1)
        greenValue = random.randrange(0,100,1)
        blueValue = random.randrange(0,100,1)
        # Change color
        while count < steps:
            redNext = redValueOld + (((redValue - redValueOld) / steps) * count)
            greenNext = greenValueOld + (((greenValue - greenValueOld) / steps) * count)
            blueNext = blueValueOld + (((blueValue - blueValueOld) / steps) * count)
            redPin.ChangeDutyCycle(redNext)
            greenPin.ChangeDutyCycle(greenNext)
            bluePin.ChangeDutyCycle(blueNext)
            time.sleep(duration/steps)
            count = count + 1
        # Set current color as old color
        time.sleep(1)
        count = 0
        redValueOld = redValue
        greenValueOld = greenValue
        blueValueOld = blueValue
    except (KeyboardInterrupt, SystemExit):
        print ("Keyboard Interrupt, exiting.")
        GPIO.output([17,18,27],GPIO.LOW)
        GPIO.cleanup([17,18,27])   # clean the channels
        exit(0)
