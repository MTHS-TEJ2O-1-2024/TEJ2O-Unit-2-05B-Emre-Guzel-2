"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *

while True:
    if button_a.is_pressed():
        temperature = temperature()
        display.scroll("The temperature is " + str(temperature) + "C")
