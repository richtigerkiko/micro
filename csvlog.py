import machine
import utime
import os

from Clock import DateTimeObj
from DataObjects.SensorData import SensorData

LogFileName = "log.csv"

Max_File_Size = 50000



def WriteLine(passed):
    log = open(LogFileName,"a") #open in append - creates if not existing, will append if it exists
    log.write(passed)
    log.close()
    
    
def WriteSensorLog(timeStamp:DateTimeObj, sensorData:SensorData):
    print("logging...")
    timeString = f"{timeStamp.year}{timeStamp.month:02d}{timeStamp.day:02d} {timeStamp.hour:02d}:{timeStamp.minute:02d}:{timeStamp.second:02d}"
    csvString = f"\"{timeString}\",\"{sensorData.dht22.Temperature}\",\"{sensorData.dht22.Humidity}\"\n"
    WriteLine(csvString)
