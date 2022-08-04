from machine import Pin, I2C
import Clock

clock = Clock.DS3231(sdaPin=Pin(0), sclPin=Pin(1))

clock.setTime(dateTime=Clock.DateTimeObj(2922,8,1,0,21,32,0,0))
