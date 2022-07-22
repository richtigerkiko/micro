from mhz19b.mhz19b import mhz19b
from machine import UART, Pin

uart = UART(1, baudrate=9600, bits=8, parity=0, stop=1, rx=Pin(4) ,tx=Pin(3))

ppin=Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)