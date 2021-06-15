"""***********************************************************************
Rutinas para acceder al RTC DS3231, conectado al I2C-0 de la orangePi

#TODO: agregar acción en caso de error de lectura/escritura
"""
from pyA20 import i2c
import datetime

class DS3231:
    def __init__(self):
        self.address = 0x68

    def read(self, register):
        try:
            i2c.init("/dev/i2c-0")
            i2c.open(self.address)
            i2c.write([register])         #Write to Adddress 1 (config register) 
            i2c.close()

            i2c.open(self.address)
            response = i2c.read(1)
            i2c.close()
        except:
            response = "ERROR"

        return response

    def write(self, register, byte):
        try:
            i2c.init("/dev/i2c-0")
            i2c.open(self.address)
            i2c.write([register, byte])         #Write to Adddress 1 (config register) 
            i2c.close()
            return "OK"
        except:
            return "ERROR"

    def writeTimeString(self, hourString):
        #convierte la hora en objeto datetime
        currentTime=datetime.time.fromisoformat(hourString)

        #Extrae los segundos, y lo formatea para el RTC DS3231
        highByte = int(currentTime.second / 10)
        secondsByte = highByte << 4
        lowByte = currentTime.second % 10
        secondsByte += lowByte
        response = self.write(0,secondsByte)

        #Extrae los minutos, y lo formatea para el RTC DS3231
        highByte = int(currentTime.minute / 10)
        minuteByte = highByte << 4
        lowByte = currentTime.minute % 10
        minuteByte += lowByte
        response2 = self.write(1,minuteByte)

        #Extrae la hora, y lo formatea para el RTC DS3231
        highByte = int(currentTime.hour / 10)
        hourByte = highByte << 4
        lowByte = currentTime.hour % 10
        hourByte += lowByte
        response3 = self.write(2,hourByte)

        if(response != response2 != response 3)
            response = "ERROR"

        return response

    def writeDateString(self, dateString):
        #Convierte la fecha en objeto datetime
        currentDate=datetime.datetime.fromisoformat(dateString)

        #Extrae el día, y lo formatea para el RTC DS3231
        highByte = int(currentDate.day / 10)
        dayByte = highByte << 4
        lowByte = currentDate.day % 10
        dayByte += lowByte
        response = self.write(4,dayByte)

        #Extrae el mes, y lo formatea para el RTC DS3231
        highByte = int(currentDate.month / 10)
        monthByte = highByte << 4
        lowByte = currentDate.month % 10
        monthByte += lowByte
        response2 = self.write(5,monthByte)

        #Extrae el año, y lo formatea para el RTC DS3231 (rango de 2000 a 2099)
        year = currentDate.year %100
        highByte = int(year / 10)
        yearByte = highByte << 4
        lowByte = year % 10
        yearByte += lowByte
        response3 = self.write(6,yearByte)

        if(response != response2 != response 3)
            response = "ERROR"

        return response

    def readTimeString(self):
        readSeconds = self.read(0)
        if(readSeconds != "ERROR"):
            highByte = readSeconds & 0xF0 
            highByte = highByte >> 4
            seconds = highByte * 10
            lowByte = readSeconds & 0x0F
            seconds += lowByte
        else: 
            return "ERROR"
        
        readMinutes = self.read(1)
        if(readMinutes != "ERROR"):
            highByte = readMinutes & 0xF0 
            highByte = highByte >> 4
            minutes = highByte * 10
            lowByte = readMinutes & 0x0F
            minutes += lowByte
        else: 
            return "ERROR"

        readHour = self.read(2)
        if(readHour != "ERROR"):
            highByte = readHour & 0xF0 
            highByte = highByte >> 4
            hour = highByte * 10
            lowByte = readHour & 0x0F
            hour += lowByte
        else: 
            return "ERROR"

        time = datetime.time(hour=hour,minute=minutes,second=seconds)
        timeString = f"{time:%H:%M:%S}"
        return timeString
        
    def readDateString(self):
        readDay = self.read(4)
        if(readDay != "ERROR"):
            highByte = readDay & 0xF0 
            highByte = highByte >> 4
            day = highByte * 10
            lowByte = readDay & 0x0F
            day += lowByte
        else: 
            return "ERROR"
        
        readMonth = self.read(5)
        if(readMonth != "ERROR"):
            highByte = readMonth & 0xF0 
            highByte = highByte >> 4
            month = highByte * 10
            lowByte = readMonth & 0x0F
            month += lowByte
        else: 
            return "ERROR"

        readYear = self.read(6)
        if(readYear != "ERROR"):
            highByte = readYear & 0xF0 
            highByte = highByte >> 4
            year = highByte * 10
            lowByte = readYear & 0x0F
            year += lowByte
            year += 2000
        else: 
            return "ERROR"

        date = datetime.date(day=day,month=month,year=year)
        dateString = f"{date:%Y-%m-%d}"
        return dateString