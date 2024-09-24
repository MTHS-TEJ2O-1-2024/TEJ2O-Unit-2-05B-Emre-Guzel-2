"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython measures the temperature of Kelvin   
"""

from microbit import *

display.clear()

display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature = temperature() + round(273.15)
        display.scroll("The temperature is: " + str(temperature) + "K")
