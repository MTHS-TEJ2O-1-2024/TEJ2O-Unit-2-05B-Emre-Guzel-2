/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Sep 24 2024
 * This program meuseures the tempurature of Kelvin 
*/

basic.clearScreen()
basic.pause(1000)
basic.showIcon(IconNames.Happy)

let temperature: number
input.onButtonPressed(Button.A, function () {
    temperature = input.temperature() + Math.round(273.15)
    basic.showString(" the temperature is:" + temperature + "K")
})