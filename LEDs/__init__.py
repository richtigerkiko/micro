from machine import Pin


class InternalLED:
    
    LED = Pin(25, Pin.OUT)
    
    def __init__(self) -> None:
        pass
        
    def ToggleLed(self) -> None:
        self.LED.toggle()
        
    def LEDOn(self) -> None:
        self.LED.on()
        
    def LEDOff(self) -> None:
        self.LED.off()
        
    def GetStatus(self) -> int:
        return self.LED.value()
    
