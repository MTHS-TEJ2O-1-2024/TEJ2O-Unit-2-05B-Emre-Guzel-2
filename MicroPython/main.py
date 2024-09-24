"""
Created by: Emre Guzel 
Created on: Sep 24 2024
This module is a Micro:bit MicroPython measures the temperature of Kelvin   
"""

from microbit import *

display.clear()

display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature = temperature() + round(273.15)
        display.scroll("The temperature is: " + str(temperature) + "K")
