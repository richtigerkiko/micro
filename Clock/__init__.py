from machine import Pin, I2C
import urtc

# weekday: 0 = monday


class DateTimeObj:
    year: int
    month: int
    day: int
    weekday: int
    hour: int
    minute: int
    second: int
    millisecond: int

    def __init__(self, year: int = 2022, month: int = 1, day: int = 1, weekday: int = 1, hour: int = 0, minute: int = 0, second: int = 0, millisecond: int = 0) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond


class DS3231:
    clock = urtc.DS3231

    def __init__(self, sdaPin: Pin, sclPin: Pin) -> None:
        self.clock = urtc.DS3231(I2C(0, sda=sdaPin, scl=sclPin))

    def getTime(self) -> DateTimeObj:
        timetupl = self.clock.datetime()
        if timetupl is not None:
            timeObj = DateTimeObj(timetupl[0], timetupl[1], timetupl[2], timetupl[3], timetupl[4], timetupl[5], timetupl[6], timetupl[7])
        else:
            timeObj = DateTimeObj()
        return timeObj
    
    def setTime(self, dateTime:DateTimeObj) -> None:
        # "DateTimeTuple", ["year", "month", "day", "weekday", "hour", "minute", "second", "millisecond"]
        self.clock.datetime(urtc.datetime_tuple(dateTime.year, dateTime.month, dateTime.day, dateTime.weekday, dateTime.hour, dateTime.minute))


