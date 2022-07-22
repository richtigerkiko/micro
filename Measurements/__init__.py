from DataObjects.SensorData import MH_Z19DataPoint, SensorData
from LEDs import InternalLED
from Sensors import Sensor_DHT22

class SensorMeasurement:
    dht22: Sensor_DHT22
    
    def __init__(self, dht22: Sensor_DHT22):
        self.dht22 = dht22

    def GetSensorData(self) -> SensorData:
        led = InternalLED()
        led.LEDOn()
        # get dht22 data
        dht22measurement = self.dht22.getDHT22DataPoint()

        # # get mh_z19 data
        mhz_19 = MH_Z19DataPoint(0)
        # led.LEDOff()
        return SensorData(dht22measurement, mhz_19)
        
