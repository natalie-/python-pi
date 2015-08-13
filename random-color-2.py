#!/usr/bin/python

# This program will change a single RGB LED to random colors over time,
# resulting in a "breathing" effect.  The LED defaults to *OFF* !!!


from time import sleep
from random import randrange

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print(
        "Error importing RPi.GPIO!  This is probably because you need superuser\
        privileges.  You can achieve this by using 'sudo' to run your script.")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17, 18, 27], GPIO.OUT)
GPIO.output([17, 18, 27], GPIO.LOW)

redPin = GPIO.PWM(17, 100)
greenPin = GPIO.PWM(18, 100)
bluePin = GPIO.PWM(27, 100)

redPin.start(0)
greenPin.start(0)
bluePin.start(0)

# Functions


def new():
    ''' Generate new random color '''
    new.redValue = randrange(0, 100, 1)
    new.greenValue = randrange(0, 100, 1)
    new.blueValue = randrange(0, 100, 1)


def old():
    ''' Cycles old and new colors '''
    old.redValue = new.redValue
    old.greenValue = new.greenValue
    old.blueValue = new.blueValue


def fade():
    ''' Fade new and old color together '''
    duration = 2
    steps = 100
    count = 0
    while count < steps:
        redNext = old.redValue + \
            (((new.redValue - old.redValue) / steps) * count)
        greenNext = old.greenValue + \
            (((new.greenValue - old.greenValue) / steps) * count)
        blueNext = old.blueValue + \
            (((new.blueValue - old.blueValue) / steps) * count)
        redPin.ChangeDutyCycle(redNext)
        greenPin.ChangeDutyCycle(greenNext)
        bluePin.ChangeDutyCycle(blueNext)
        sleep(duration / steps)
        count = count + 1
    sleep(1)


def zero():
    ''' Initialize the old colors as zero '''
    old.redValue = 0
    old.greenValue = 0
    old.blueValue = 0


def main():
    zero()
    while True:
        try:
            new()
            fade()
            old()
            # print(new.redValue, new.greenValue, new.blueValue)
            # prints colors to terminal for debugging if needed
        except (KeyboardInterrupt):
            print ("Keyboard Interrupt, exiting.")
            GPIO.output([17, 18, 27], GPIO.LOW)
            GPIO.cleanup([17, 18, 27])   # clean the channels
            exit(0)

# Run the program
main()
