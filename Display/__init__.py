from machine import Pin, I2C
from Clock import DateTimeObj
from DataObjects.SensorData import SensorData
import ssd1306
from urtc import DateTimeTuple

class LCDDisplay:
    
    SDA:Pin
    SCL:Pin

    i2c:I2C

    display:ssd1306.SSD1306_I2C
    
    def __init__(self, sdaPin:Pin, sclPin:Pin) -> None:
        self.SDA = sdaPin
        self.SCL = sclPin
        self.i2c = I2C(0, sda=Pin(0), scl=Pin(1))
        self.display = ssd1306.SSD1306_I2C(128, 64, self.i2c)
        
    def DisplayNoData(self) -> None:
        self.display.fill(0)
        self.display.text("No Data", 0,0)
        self.display.show()

    def DisplayTempAndHumidity(self, data:SensorData) -> None:
        self.display.fill_rect(0, 0, 128, 30, 0)
        self.display.text(f"Temp:     {data.dht22.Temperature:.1f} C", 0, 5)
        self.display.text(f"Humidity: {data.dht22.Humidity:.1f} %", 0, 15)
        # self.display.text(f"CO2:      {data.mh_z19.CO2:.1f}", 0, 50)
        self.display.hline(30, 30, 78, 1)
        self.display.show()
    
    def DisplayTime(self, time:DateTimeObj) -> None:
        self.display.fill_rect(0, 40, 128, 24, 0)
        dateString = f"{time.day:02d}.{time.month:02d}.{time.year}"
        timeString = f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}"
        self.display.text(dateString, 0, 40, 1)
        self.display.text(timeString, 0, 50, 1)
        self.display.show()
    