from pyA20.gpio import gpio             #Para PWM por software en PA6 (pin 7)    
from pyA20.gpio import port
from orangepwm import *

class PUERTA:
    def __init__(self):
        self.estado = None

    def subirPuerta_init(self):
        gpio.init()
        gpio.setcfg(port.PA9,gpio.output)
        gpio.setcfg(port.PA10,gpio,output)

        #PWM por software, con librería orangepwm, y pyA20
        pwm = OrangePwm(100, port.PA8)          #100Hz en PA6
        pwm.start(0)
        pwm.changeDutyCycle(0)

        gpio.output(port.PA9, gpio.HIGH)
        gpio.output(port.PA10, gpio.LOW)
        
        doorTimeout = 70            #70 * 0.15 = 10.5 segundos de timeout.

        #Rampa de a sceleración
        for x in range(100):
            pwm.changeDutyCycle(x)
            time.sleep(0.010)

        #lee el estado de la puerta, hasta llegar a la posición deseada
        puerta = MCP.estadoPuerta()
        while(puerta != "arriba"):
            time.sleep(0.15)
            puerta = MCP.estadoPuerta()
            doorTimeout -= 1                    #decrementa el timeout. Si llega a 0 y no llegó la puerta, informa del error
            if(not doorTimeout):
                break
            if(self.estado != "subir"):
                break
            else:
                self.estado = None
        
        if(not doorTimeout):                    #Aquí informa del error por timeout con un POST al microservicio
            pass
            
        pwm.stop()
        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.LOW)

    def subirPuerta_cont(self):
        self.estado = "subir"

    def bajarPuerta_init(self):
        gpio.init()
        gpio.setcfg(port.PA9,gpio.output)
        gpio.setcfg(port.PA10,gpio,output)

        #PWM por software, con librería orangepwm, y pyA20
        pwm = OrangePwm(100, port.PA8)          #100Hz en PA6
        pwm.start(0)
        pwm.changeDutyCycle(0)

        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.HIGH)
        
        doorTimeout = 70            #70 * 0.15 = 10.5 segundos de timeout.

        #Rampa de a sceleración
        for x in range(100):
            pwm.changeDutyCycle(x)
            time.sleep(0.010)

        #lee el estado de la puerta, hasta llegar a la posición deseada
        puerta = MCP.estadoPuerta()
        while(puerta != "abajo"):
            time.sleep(0.15)
            puerta = MCP.estadoPuerta()
            doorTimeout -= 1                    #decrementa el timeout. Si llega a 0 y no llegó la puerta, informa del error
            if(not doorTimeout):
                break
            if(self.estado != "bajar"):
                break
            else:
                self.estado = None
        
        if(not doorTimeout):                    #Aquí informa del error por timeout con un POST al microservicio
            pass
            
        pwm.stop()
        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.LOW)

    def bajarPuerta_cont(self):
        self.estado = "bajar"

    def abrirPuerta():
        gpio.init()
        gpio.setcfg(port.PA9,gpio.output)
        gpio.setcfg(port.PA10,gpio,output)

        #PWM por software, con librería orangepwm, y pyA20
        pwm = OrangePwm(100, port.PA8)          #100Hz en PA6
        pwm.start(0)
        pwm.changeDutyCycle(0)

        gpio.output(port.PA9, gpio.HIGH)
        gpio.output(port.PA10, gpio.LOW)
        
        doorTimeout = 70            #70 * 0.15 = 10.5 segundos de timeout.

        #Rampa de a sceleración
        for x in range(100):
            pwm.changeDutyCycle(x)
            time.sleep(0.010)

        #lee el estado de la puerta, hasta llegar a la posición deseada
        puerta = MCP.estadoPuerta()
        while(puerta != "arriba"):
            time.sleep(0.15)
            puerta = MCP.estadoPuerta()
            doorTimeout -= 1                    #decrementa el timeout. Si llega a 0 y no llegó la puerta, informa del error
            if(not doorTimeout):
                break
        
        if(not doorTimeout):                    #Aquí informa del error por timeout con un POST al microservicio
            pass
            
        pwm.stop()
        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.LOW)

    def cerrarPuerta():
        gpio.init()
        gpio.setcfg(port.PA9,gpio.output)
        gpio.setcfg(port.PA10,gpio,output)

        #PWM por software, con librería orangepwm, y pyA20
        pwm = OrangePwm(100, port.PA8)          #100Hz en PA6
        pwm.start(0)
        pwm.changeDutyCycle(0)

        gpio.output(port.PA9, gpio.LOW)                 
        gpio.output(port.PA10, gpio.HIGH)
        
        doorTimeout = 70            #70 * 0.15 = 10.5 segundos de timeout.

        #Rampa de a sceleración
        for x in range(100):
            pwm.changeDutyCycle(x)
            time.sleep(0.010)

        #lee el estado de la puerta, hasta llegar a la posición deseada
        puerta = MCP.estadoPuerta()
        while(puerta != "abajo"):
            time.sleep(0.15)
            puerta = MCP.estadoPuerta()
            doorTimeout -= 1                    #decrementa el timeout. Si llega a 0 y no llegó la puerta, informa del error
            if(not doorTimeout):
                break
        
        if(not doorTimeout):                    #Aquí informa del error por timeout con un POST al microservicio
            pass    

        pwm.stop()
        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.LOW)

    def puertaPosicionCorrecta():
        gpio.init()
        gpio.setcfg(port.PA9,gpio.output)
        gpio.setcfg(port.PA10,gpio,output)

        #PWM por software, con librería orangepwm, y pyA20
        pwm = OrangePwm(100, port.PA8)          #100Hz en PA6
        pwm.start(0)
        pwm.changeDutyCycle(0)

        puerta = MCP.estadoPuerta()             #consulta la posición actual de la puerta
        while(puerta == "ERROR"):               
            time.sleep(0.002)
            puerta = MCP.estadoPuerta()
        
        if(puerta == "arriba"):                 #Si la puerta se encuentra arriba
            gpio.output(port.PA9, gpio.LOW)                 
            gpio.output(port.PA10, gpio.HIGH)
        elif(puerta == "abajo"):                #si la puerta se encuentra abajo
            gpio.output(port.PA9, gpio.HIGH)                 
            gpio.output(port.PA10, gpio.LOW)
        elif(puerta == "correcta"):
            return "Correcta"
        else:
            return "NoDoorFound"

        doorTimeout = 70            #70 * 0.15 = 10.5 segundos de timeout.

        #Rampa de a sceleración
        for x in range(100):
            pwm.changeDutyCycle(x)
            time.sleep(0.010)

        #lee el estado de la puerta, hasta llegar a la posición deseada
        puerta = MCP.estadoPuerta()
        while(puerta != "correcta"):
            time.sleep(0.15)
            puerta = MCP.estadoPuerta()
            doorTimeout -= 1                    #decrementa el timeout. Si llega a 0 y no llegó la puerta, informa del error
            if(not doorTimeout):
                break
        
        if(not doorTimeout):                    #Aquí informa del error por timeout con un POST al microservicio
            pass    

        pwm.stop()
        gpio.output(port.PA9, gpio.LOW)
        gpio.output(port.PA10, gpio.LOW)

        gpio.setcfg(port.PA8,gpio.output)
        gpio.output(port.PA8, gpio.LOW)                 #deshabilita el enable, para que no 
