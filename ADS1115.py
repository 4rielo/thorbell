from pyA20 import i2c

if __name__ == "__init__":
    
    #ADC address and gain settings ("constants")
    global ads1
    global ads2
    global ADS1115_FS_4096
    global ADS1115_FS_2048
    global ADS1115_FS_1024
    global ADS1115_FS_512

    ads1 = 0x48              #Address for the I2C ADC, when ADD0 is connected to GND
    ads2 = 0x49

    ADS1115_FS_4096 = 1
    ADS1115_FS_2048 = 2
    ADS1115_FS_1024 = 3
    ADS1115_FS_512 = 4

def ReadADC(Address, channel, ref):

    config = 0b1000000111000011
    config |= (channel<<12)
    config |= (ref<<9)

    lectura = 0
    aux = 0x80

    configH = (config>>8)
    configL = config & 0x00FF

    try:
        i2c.init("/dev/i2c-0") 

        i2c.open(Address)           #Open ADC I2C
        i2c.write([0x01, configH, configL])         #Write to Adddress 1 (config register) 
        i2c.close()


        while(lectura != aux):

            i2c.open(Address)
            high = i2c.read(2)
            i2c.close()

            lectura = high[0] & aux

        i2c.open(Address)
        i2c.write([0x00])
        i2c.close()

        i2c.open(Address)
        read = i2c.read(2)
        i2c.close()

        value=(read[0]<<8)+read[1]
    except:         #port busy or something
        value = "ERROR" 
    return value