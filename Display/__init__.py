from machine import Pin, I2C
import ssd1306


SDA = 1
SCL = 2

i2c = I2C(1, sda=Pin(4), scl=Pin(5))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

display("Hello World")