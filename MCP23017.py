from pyA20 import i2c


class MCP23017:
    def __init__(self, address=0x24):
        self.address = address

        self.GPIOA = 0x12
        self.LATA = 0x14

        self.GPIOB = 0x13
        self.LATB = 0x15

    def write(self, register, byte):
        try:
            i2c.init("/dev/i2c-0")
            i2c.open(self.address)
            i2c.write([register, byte])         #Write to Adddress 1 (config register) 
            i2c.close()
            return "OK"
        except:
            return "ERROR"

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

    def configMCP(self):
        trisA = 0b00011111              #los 5 pines más bajos (de 0 a 4) son entradas
        pullUpA= 0b00001111             #Los 4 pines más bajos (de 0 a 3), tienen pullup activado

        trisB = 0xFF                    #de momento no se utiliza, quedan como entradas

        response = self.write(0x00,trisA)          #Configura los pines del puerto A como entrada/salida
        if(response != "OK"):
            return response

        response = self.write(0x0C,pullUpA)        #configura los pullups del puerto A
        if(response != "OK"):
            return response

        response = self.write(0x01,trisB)          #configura los pines del puerto B como entrada
        
        return response

    def encenderUV(self):               #La luminaria UV está controlada por el pin A5
        estadoActual = self.read(self.GPIOA)           #lee el estado del GPIOA
        estadoActual = estadoActual | 0x20             #enciende el bit correspondiente al A5, sin modificar el resto
        self.write(self.LATA,estadoActual)

    def apagarUV(self):                 #La luminaria UV es controlada por el pin A5
        estadoActual = self.read(self.GPIOA)            #lee el estado actual del GPIOA
        estadoActual = estadoActual & 0xDF              #pone a 0 el bit del pin A5
        self.write(self.LATA,estadoActual)


    def estadoPuerta(self):             #Lee el estado de la puerta
        posicionPuerta = self.read(self.GPIOA)      #GPIOA 1, 2 y 3 son las posiciones de arriba, abajo, y pos. común

        return posicionPuerta
        
        if(posicionPuerta != "ERROR"):
            if(posicionPuerta[0] & 0x02):
                posicionPuerta = "abajo"
            elif(posicionPuerta[0] & 0x04):
                posicionPuerta = "arriba"
            elif(posicionPuerta[0] & 0x08):
                posicionPuerta = "correcta"
            else:
                posicionPuerta = "movimiento"

        return posicionPuerta