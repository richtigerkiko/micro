import time
from dataclasses import dataclass

@dataclass
class dht22Measurement:
    PinNumber: int
    TimeStamp: tuple
    Temperature: float
    Humidity: float

    def __init__(self, PinNumber: int, Temperature: float, Humidity: float):
        self.PinNumber = PinNumber
        self.TimeStamp = time.localtime()
        self.Humidity = Humidity
        self.Temperature = Temperature
    
