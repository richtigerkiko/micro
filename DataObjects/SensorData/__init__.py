import time

class DHT22DataPoint:
    TimeStamp: tuple
    Temperature: float
    Humidity: float

    def __init__(self, Temperature: float, Humidity: float):
        self.TimeStamp = time.localtime()
        self.Humidity = Humidity
        self.Temperature = Temperature

class MH_Z19DataPoint:
    TimeStamp: tuple
    CO2: int

    def __init__(self, CO2: int):
        self.CO2 = CO2
        self.TimeStamp = time.localtime()

class SensorData:
    dht22: DHT22DataPoint
    mh_z19: MH_Z19DataPoint
    
    def __init__(self, dht22: DHT22DataPoint, mh_z19: MH_Z19DataPoint):
        self.dht22 = dht22
        self.mh_z19 = mh_z19
        
