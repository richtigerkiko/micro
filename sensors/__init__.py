from DataObjects.SensorData import SensorData 
from measuredht22 import measureDHT22
from Sensors.measuremhz19b import measure_mh_z19b


def GetSensorData() -> SensorData:
    print("getting Sensor Data...")
    # get dht22 data
    dht22 = measureDHT22(21)
    
    # get mh_z19 data
    mhz_19 = measure_mh_z19b(27,26)
    
    return SensorData(dht22,mhz_19)