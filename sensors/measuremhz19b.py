from dataObjects.sensordata import mhz19Measurement
from statistics import median

from mhz19b.mhz19b import mhz19b

def measure_mh_z19b(rx_pin:int, tx_pin:int) -> mhz19Measurement:
    print("Getting mhz19 read...")
    SensorCO2 = mhz19b(rx_pin, tx_pin) # rx_pin= 16 and tx_pin= 17
    readinList= [] 
    for x in range(1, 5): # We take 5 measurements 
        # we add the list of 1 member and convert it to "int" number 
        readinList.append(int(sum(SensorCO2.measure())))
    
    medianCo2Value = median(readinList) # reduce noise
    return mhz19Measurement(medianCo2Value)
