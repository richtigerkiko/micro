from DataObjects.SensorData import MH_Z19DataPoint, SensorData
from LEDs import InternalLED
from Sensors import Sensor_DHT22, Sensor_MHZ19C

class SensorMeasurement:
    dht22: Sensor_DHT22
    mhz19c: Sensor_MHZ19C
    
    def __init__(self, dht22: Sensor_DHT22, mhz19c:Sensor_MHZ19C):
        self.dht22 = dht22
        self.mhz19c = mhz19c

    def GetSensorData(self) -> SensorData:
        led = InternalLED()
        led.LEDOn()
        # get dht22 data
        dht22measurement = self.dht22.getDHT22DataPoint()

        # # get mh_z19 data
        mhz_19 = self.mhz19c.getMH_Z19DataPoint()
        led.LEDOff()
        return SensorData(dht22measurement, mhz_19)
        
