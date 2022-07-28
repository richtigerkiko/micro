from machine import Pin, I2C
import urtc

clock = urtc.DS3231(I2C(0, sda=Pin(0), scl=Pin(1)))

print(clock.datetime()[0])
