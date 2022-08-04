import time
from DataObjects.SensorData import DHT22DataPoint, MH_Z19DataPoint
from machine import Pin, UART
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
    
class Sensor_MHZ19C:
    
    def __init__(self, tx_pin: int, rx_pin: int):
        self.uart = UART(0, baudrate=9600, bits=8, stop=1, tx=Pin(tx_pin), rx=Pin(rx_pin))
        
    def measure(self):
        for i in range(2):
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep_ms(100)  # in seconds

            # read and validate the data
            global buf 
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break

        if buf != None:
            co2 = buf[2] * 256 + buf[3]
            return [co2]
        
        else:
            return [0]

    # check data returned by the sensor
    def is_valid(self, buf):
        if buf is None or buf[0] != 0xFF or buf[1] != 0x86:
            return False
        i = 1
        checksum = 0x00
        while i < 8:
            checksum += buf[i] % 256
            i += 1
        checksum = ~checksum & 0xFF
        checksum += 1
        return checksum == buf[8]
    
    def getMH_Z19DataPoint(self) -> MH_Z19DataPoint:
        co2 = self.measure()
        return MH_Z19DataPoint(CO2=co2[0])