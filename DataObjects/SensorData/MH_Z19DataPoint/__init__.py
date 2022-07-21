import time

class MH_Z19DataPoint:
    TimeStamp: tuple
    CO2: int

    def __init__(self, CO2: int):
        self.CO2 = CO2
        self.TimeStamp = time.localtime()
