from machine import Timer, Pin
import time
import Clock
from Display import LCDDisplay
from Measurements import SensorMeasurement
from Sensors import Sensor_DHT22
from csvlog import WriteSensorLog

timer = Timer()

try:
    print("Initiating peripheral devices")
    display = LCDDisplay(sdaPin=Pin(0), sclPin=Pin(1))
    dht22Sensor = Sensor_DHT22(Pin(2))
    clock = Clock.DS3231(sdaPin=Pin(0), sclPin=Pin(1))

    
except:
    print("no display")
    
    

def timerTick(timer):
    # # Run function to grab sensor data
    try:
        # get current time
        currentTime = clock.getTime()
        sensorMeasure = SensorMeasurement(dht22Sensor)
        sensorData = sensorMeasure.GetSensorData()
        if currentTime.second % 10 == 0:
            WriteSensorLog(currentTime, sensorData)
        display.DisplayTempAndHumidity(sensorData)
        display.DisplayTime(currentTime)
        time.sleep_ms(200)
    except:
        display.DisplayNoData()
    # time.sleep_ms(200)
    
    # # # Run actions depending on data
    # # print("Running sensor driven actions")
    # # time.sleep_ms(200)
    
    # # # Run display function to display sensor data on OLED

    
timer.init(mode=Timer.PERIODIC, callback=timerTick, period=1000)


