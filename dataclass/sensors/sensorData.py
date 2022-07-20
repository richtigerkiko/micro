import time
from dataclasses import dataclass

from dataclass.sensors.dht22.dht22Measurement import dht22Measurement

@dataclass
class sensorData:
    dht22: dht22Measurement

    def __init__(self, PinNumber: int, Temperature: float, Humidity: float):
        self.PinNumber = PinNumber
        self.TimeStamp = time.localtime()
        self.Humidity = Humidity
        self.Temperature = Temperature
    
