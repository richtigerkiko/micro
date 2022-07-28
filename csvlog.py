import machine
import utime
import os

from Clock import DateTimeObj
from DataObjects.SensorData import SensorData

LogFileName = "log.csv"

Max_File_Size = 50000


def isFileToBig() -> bool: # returns filesize in bytes
    try:
        logFile = open(LogFileName, "r")
        logFile.seek(0, 2)
        size = logFile.tell()
        logFile.close()
        return Max_File_Size <= size
    except:
        print("no file")
        return False # if error then file doesnt exist so its not too big
    
def WriteDataLine(passed):
    if isFileToBig() == False:
        log = open(LogFileName,"a") #open in append - creates if not existing, will append if it exists
        log.write(passed)
        log.flush()
        log.close()
    else:
        print("cant log, file too big")
    
    
def WriteSensorLog(timeStamp:DateTimeObj, sensorData:SensorData):
    timeString = f"{timeStamp.year}{timeStamp.month:02d}{timeStamp.day:02d} {timeStamp.hour:02d}:{timeStamp.minute:02d}:{timeStamp.second:02d}"
    csvString = f"\"{timeString}\",\"{sensorData.dht22.Temperature}\",\"{sensorData.dht22.Humidity}\"\n"
    WriteDataLine(csvString)
