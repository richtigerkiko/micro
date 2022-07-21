from mhz19b.mhz19b import mhz19b
from DataObjects.SensorData import DHT22DataPoint, MH_Z19DataPoint, SensorData
from machine import Pin
from dht import DHT22


def measureDHT22(pinNumber: int) -> DHT22DataPoint:
    print("Getting DHT22 Read...")
    try:
        dataPin = Pin(pinNumber, Pin.IN, Pin.PULL_UP)
        dhtSensor = DHT22(dataPin)
        dhtSensor.measure()

        temp = dhtSensor.temperature()
        humid = dhtSensor.humidity()
    except:
        print("Error gettng DHT22 Data")
        temp = 0
        humid = 0
    finally:
        return DHT22DataPoint(pinNumber, temp, humid)


def measure_mh_z19b(rx_pin: int, tx_pin: int) -> MH_Z19DataPoint:
    print("Getting mhz19 read...")
    try:
        SensorCO2 = mhz19b(rx_pin, tx_pin)  # rx_pin= 16 and tx_pin= 17
        reading = int(sum(SensorCO2.measure()))
    except:
        print("Error getting MH_Z19 Data")
        reading = 0
    finally:
        return MH_Z19DataPoint(reading)


def GetSensorData() -> SensorData:
    print("getting Sensor Data...")
    # get dht22 data
    dht22 = measureDHT22(21)

    # get mh_z19 data
    mhz_19 = measure_mh_z19b(27, 26)

    return SensorData(dht22, mhz_19)
