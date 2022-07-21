import time

from DataObjects.SensorData.DHT22DataPoint import DHT22DataPoint
from DataObjects.SensorData.MH_Z19DataPoint import MH_Z19DataPoint

class SensorData:
    dht22: DHT22DataPoint
    mh_z19: MH_Z19DataPoint
    
    def __init__(self, dht22: DHT22DataPoint, mh_z19: MH_Z19DataPoint):
        self.dht22 = dht22
        self.mh_z19 = mh_z19
        
    