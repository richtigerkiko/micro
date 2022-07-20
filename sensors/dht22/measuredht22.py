from machine import Pin
from dht import DHT22
from dht22Measurement import dht22Measurement

def measureDHT22(pinNumber:int) -> dht22Measurement: 
    dataPin = Pin(pinNumber, Pin.IN, Pin.PULL_UP)
    dhtSensor = DHT22(dataPin)
    dhtSensor.measure()
    
    temp = dhtSensor.temperature()
    humid = dhtSensor.humidity()
    
    return dht22Measurement(pinNumber, temp, humid)
