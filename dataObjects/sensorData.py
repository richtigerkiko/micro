import time
from dataclasses import dataclass

@dataclass
class mhz19Measurement:
    TimeStamp: tuple
    CO2: int

    def __init__(self, CO2: int):
        self.CO2 = CO2
        self.TimeStamp = time.localtime()

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
    

@dataclass
class sensorData:
    dht22: dht22Measurement
    mh_z19: mhz19Measurement
    
    def __init__(self, dht22: dht22Measurement, mh_z19: mhz19Measurement):
        self.dht22 = dht22
        self.mh_z19 = mh_z19
        
    