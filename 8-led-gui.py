#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This program will turn the LEDs on or off with a checkbox in a GUI
# Requires wxPython Phoenix (using Python 3) and RPi.GPIO

# Import all the things
import tkinter as tk

try:
    import pygubu
except ImportError:
    print("Error importing pygubu.  Available at https://github.com/alejandroautalan/pygubu")

# use wiringpi instead!

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.")

# Set up RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17,18,27,22,23,24,25,4],GPIO.OUT)

# Turn all LEDs off
GPIO.output([17,18,27,22,23,24,25,4],GPIO.HIGH)

class Application:
    def __init__(self, master):
        self.master = master

        self.builder = builder = pygubu.Builder()
        builder.add_from_file('led.ui')
        self.mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

    def onQuitButtonClick(self):
        """Quit button callback"""
        GPIO.cleanup([17,18,27,22,23,24,25,4])   # clean the channels
        self.master.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()



# # Blink left to right
# while count < countmax:
#     GPIO.output(17,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(17,GPIO.HIGH)
#     GPIO.output(18,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(18,GPIO.HIGH)
#     GPIO.output(27,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(27,GPIO.HIGH)
#     GPIO.output(22,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(22,GPIO.HIGH)
#     GPIO.output(23,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(23,GPIO.HIGH)
#     GPIO.output(24,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(24,GPIO.HIGH)
#     GPIO.output(25,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(25,GPIO.HIGH)
#     GPIO.output(4,GPIO.LOW)
#     time.sleep(interval)
#     GPIO.output(4,GPIO.HIGH)
