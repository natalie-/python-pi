#!/usr/bin/python
# -*- coding: UTF-8 -*-

# This program will turn the LEDs on or off with a checkbox in a GUI
# Tested in Python 3.4
# Requires pygubu, tkinter, and RPi.GPIO

# Import all the things
import tkinter as tk

try:
    import pygubu
except ImportError:
    print("Error importing pygubu.  Available at https://github.com/alejandroautalan/pygubu")

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.")

# Set up RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)   # Silence cleanup warnings if CTRL-C is pressed

# Set up controls
GPIO.setup([17, 18, 27, 22, 23, 24, 25, 4], GPIO.OUT)

# Turn all LEDs off
GPIO.output([17, 18, 27, 22, 23, 24, 25, 4], GPIO.HIGH)


class Application:
    def __init__(self, master):
        self.master = master

        self.builder = builder = pygubu.Builder()
        builder.add_from_file('led.ui')
        self.mainwindow = builder.get_object('mainwindow', master)

        builder.connect_callbacks(self)

    def onQuitButtonClick(self):
        """Quit button callback"""
        GPIO.cleanup([17, 18, 27, 22, 23, 24, 25, 4])   # clean the channels
        self.master.quit()

    def onLed1(self):
        """LED 1"""
        if Led1.get() == 0:
            GPIO.output(17, GPIO.LOW)
            Led1.set(1)
        else:
            GPIO.output(17, GPIO.HIGH)
            Led1.set(0)

    def onLed2(self):
        """LED 2"""
        if Led2.get() == 0:
            GPIO.output(18, GPIO.LOW)
            Led2.set(1)
        else:
            GPIO.output(18, GPIO.HIGH)
            Led2.set(0)

    def onLed3(self):
        """LED 3"""
        if Led3.get() == 0:
            GPIO.output(27, GPIO.LOW)
            Led3.set(1)
        else:
            GPIO.output(27, GPIO.HIGH)
            Led3.set(0)

    def onLed4(self):
        """LED 4"""
        if Led4.get() == 0:
            GPIO.output(22, GPIO.LOW)
            Led4.set(1)
        else:
            GPIO.output(22, GPIO.HIGH)
            Led4.set(0)

    def onLed5(self):
        """LED 5"""
        if Led5.get() == 0:
            GPIO.output(23, GPIO.LOW)
            Led5.set(1)
        else:
            GPIO.output(23, GPIO.HIGH)
            Led5.set(0)

    def onLed6(self):
        """LED 6"""
        if Led6.get() == 0:
            GPIO.output(24, GPIO.LOW)
            Led6.set(1)
        else:
            GPIO.output(24, GPIO.HIGH)
            Led6.set(0)

    def onLed7(self):
        """LED 7"""
        if Led7.get() == 0:
            GPIO.output(25, GPIO.LOW)
            Led7.set(1)
        else:
            GPIO.output(25, GPIO.HIGH)
            Led7.set(0)

    def onLed8(self):
        """LED 8"""
        if Led8.get() == 0:
            GPIO.output(4, GPIO.LOW)
            Led8.set(1)
        else:
            GPIO.output(4, GPIO.HIGH)
            Led8.set(0)

if __name__ == '__main__':
    root = tk.Tk()
    Led1 = tk.IntVar()
    Led1.set(0)
    Led2 = tk.IntVar()
    Led2.set(0)
    Led3 = tk.IntVar()
    Led3.set(0)
    Led4 = tk.IntVar()
    Led4.set(0)
    Led5 = tk.IntVar()
    Led5.set(0)
    Led6 = tk.IntVar()
    Led6.set(0)
    Led7 = tk.IntVar()
    Led7.set(0)
    Led8 = tk.IntVar()
    Led8.set(0)
    app = Application(root)
    root.mainloop()
