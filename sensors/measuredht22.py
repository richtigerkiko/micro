from machine import Pin
from DataObjects.SensorData.DHT22DataPoint import DHT22DataPoint
from dht import DHT22 # type: ignore

def measureDHT22(pinNumber:int) -> DHT22DataPoint: 
    print("Getting DHT22 Read...")
    dataPin = Pin(pinNumber, Pin.IN, Pin.PULL_UP)
    dhtSensor = DHT22(dataPin)
    dhtSensor.measure()
    
    temp = dhtSensor.temperature()
    humid = dhtSensor.humidity()
    
    return DHT22DataPoint(pinNumber, temp, humid)
