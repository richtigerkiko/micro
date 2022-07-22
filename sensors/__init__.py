from LEDs import InternalLED
from mhz19b.mhz19b import mhz19b
from DataObjects.SensorData import DHT22DataPoint, MH_Z19DataPoint
from machine import Pin
from dht import DHT22

class Sensor_DHT22:
    
    dhtSensor:DHT22
    
    def __init__(self, dataPin:Pin) -> None:
        try:
            self.dhtSensor = DHT22(dataPin)
        except:
            print("cant connect to sensor")
        
    def getDHT22DataPoint(self) -> DHT22DataPoint:
        self.dhtSensor.measure()
        temp = self.dhtSensor.temperature()
        humid = self.dhtSensor.humidity()
        return DHT22DataPoint(temp, humid)