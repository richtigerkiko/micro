import time

class DHT22DataPoint:
    PinNumber: int
    TimeStamp: tuple
    Temperature: float
    Humidity: float

    def __init__(self, PinNumber: int, Temperature: float, Humidity: float):
        self.PinNumber = PinNumber
        self.TimeStamp = time.localtime()
        self.Humidity = Humidity
        self.Temperature = Temperature
