#!/usr/bin/python

# This program will blink an LED when you press a button.
# The LED defaults to *OFF* !!!

# At some point, add control using the run variable within the
# while loop.  Until then, CTRL-C to exit.  (24 Feb 15)

import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(17, GPIO.HIGH)  # Turn off LED

run = 0

while run == 0:
    if(GPIO.input(18)) == GPIO.LOW:
        GPIO.output(17, GPIO.LOW)   # Turn on LED
        time.sleep(0.01)
    elif(GPIO.input(18)) == GPIO.HIGH:
        GPIO.output(17, GPIO.HIGH)  # Turn off LED
        time.sleep(0.01)
    else:
        time.sleep(0.01)

GPIO.cleanup([17, 18])   # clean the channels
exit(0)
