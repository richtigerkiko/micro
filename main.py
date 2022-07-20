from machine import Timer
import time
import sensors

timer = Timer()

def timerTick(timer):
    # Run function to grab sensor data
    print("Grabbing sensor data")
    time.sleep_ms(200)
    
    # Run actions depending on data
    print("Running sensor driven actions")
    time.sleep_ms(200)
    
    # Run display function to display sensor data on OLED
    print("running display function")
    time.sleep_ms(200)
    
timer.init(period=1000, callback=timerTick)
