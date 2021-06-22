#*********************************************************************
# Status server:
#               Este archivo se ejecuta al inicio, antes de comenzar
# el programa de la pantalla principal. Corre dentro de un puerto 
# interno de localhost, y mediante métodos de GET y POST, recibe y 
# devuelve el estado de las variables globales. 
#               Cuando se realiza una modificación digna de almacenar
# en el disco duro, éste es el único punto donde se realizará dicho
# proceso, reduciendo la escritura y el acceso al disco al mínimo
# posible, ya que el estado global de la mayoría de las variables
# que se necesita acceder van a estar almacenadas en memoria RAM,
# dentro de la ejecución de éste archivo.

import web
import subprocess
import requests
import time
import json
import datetime
import threading

#Módulos de manejo de puertos de I/O e I2C
import ADS1115
import MCP23017
from DS3231 import DS3231
from MCP23017 import MCP23017
import OPi.GPIO as OPiGPIO                 #Para PWM en RA5 (PWM0)

from pyA20.gpio import gpio             #Para PWM por software en PA6 (pin 7)    
from pyA20.gpio import port
from orangepwm import *

import random

#Variables "globales", que se acceden en las distintas clases que atienden
# las solicitudes
global status
global statusFile
mediciones = dict()
#  Cuando sea necesario actualizar algún estado de manera permanente, como el idioma,
# alguna fecha/hora, o advertencias, se escribirá el archivo status.dat
#  Para saber si el dato modificado debe ser almacenado en el archivo de status, 
# tengo una lista de "essentials", que se revisa cuando se recibe un POST.
#  Si el "key" de la solicitud de modificación se encuentra en la lista de "essentials"
# se almacena la modificación en el archivo "status.dat"
global essentials 
essentials = ( 
                "LEDPWM",
                "UV_Timer",
                "UV_Calendar",
                "UV_Calendar_init",
                "UV_Calendar_end",
                "Rutina_Calendar",
                "Rutina_Calendar_init",
                "Rutina_Calendar_end",
                "WARNINGS",
                "GMT"
            )

#################################################################################

#PWM0 - Configuración con librería OPi.GPIO
PWM_chip = 0
PWM_pin = 0
frequency_Hz=2000
Duty_Cycle_Percent=0
LED = OPiGPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
LED.start_pwm())

#Crea una instancia de la lectura/escritura del reloj RTC 
RTC = DS3231()

MCP = MCP23017()

controlPuerta = PUERTA()

response = MCP.configMCP()
while(response != "OK"):
    time.sleep(0.005)
    response = MCP.configMCP()
#################################################################################

#Las direcciones sobre las que recibe solicitudes de microservicios "status"
urls = ('/','root', '/status', 'Status','/adc','ADC', '/reboot','reboot')
app = web.application(urls,globals())

#Dirección de la carpeta, donde se encuentra el archivo ejecutado
path = __file__.replace("/statusServer.py","")
if(not path):
    path = "."

#Dirección de la ubicación del archivo "status.dat"
statusFile= f"{path}/CSB_MercurioR1/status.dat"

#intenta abrir el archivo "status.dat"
try:                 
    print("Trying to open status file")
    f=open(statusFile)              #Busca el archivo statusFile, si existe, lo abre
    status = json.load(f)             #y carga el último estado guardado
    f.close()                       #(cierra el archivo, no lo necesita por ahora)
    print("Status File found, reading initial status")
except:                             #Si no econtró el arvchivo
    status = {                        #genera un status inicial
        "Idioma": "es-AR", 
        
        "LED_Light": False, 
        "LEDPWM": 100, 
        
        "UV_Light": False, 
        "UV_TimerEnable": False,
        "UV_Timer": 0, 
        
        "UVLEDPWM": 100, 
        
        "UV_Calendar": False, 
        "UV_Calendar_init": format(datetime.now(),"%Y/%m/%d %H:%M"), 
        "UV_Calendar_end": format(datetime.now(),"%Y/%m/%d %H:%M"), 

        "Rutina_Calendar": False,
        "Rutina_Calendar_init": format(datetime.now(),"%Y/%m/%d %H:%M"), 
        "Rutina_Calendar_end": format(datetime.now(),"%Y/%m/%d %H:%M"), 

        "PWR": False, 

        "screenUser": "", 

        "webUsers": {
            "userA": {
                "ip": "", 
                "user": ""
            }
        }, 
        "WARNINGS": [],
        "GMT": 0
    }
    with open(statusFile, "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
        json.dump(data,f)
    print("Status file not found. Creates initial ( default) status file")

#TODO: Aquí se obtiene el tiempo del reloj SPI, y se revisa si hay conexión a 
# internet. 

#################################################################################

class root:
    def __init__(self):
        self.hello="Please go to /scan to search for available networks"

    def GET(self):
        return self.hello

class reboot:
    def GET(self):
        input = web.input()
        for x in input.keys():
            if(x == "reboot"): 
                command = "reboot"
                subprocess.run(command,shell=True)

class Status:
    #Variables globales obtenidas del archivo status.dat
    global status
    global essentials
    #####################################################
    def __init__(self):
        #GPIO.setboard(GPIO.)
        global LED
        
        pass

    def GET(self):              #Aquí defino qué variable quiero leer, ej: GET -> status?Idioma
        input = web.input()
        #print("Input:")
        #print(input)
        for x in input.keys():              #analizo la clave ("key") recibida en la solicitud
            #print("Key: " + str(x))
            if(x == "time"):                 #consulto la hora
                #TODO: currentTimeDate es el valor obtenido del RTC, NO la hora del sistema
                timeRTC = RTC.readTimeString()
                while(timeRTC == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    timeRTC = RTC.readTimeString()              #Y vuelve a consultar la hora

                dateRTC = RTC.readDateString()
                while(dateRTC == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    dateRTC = RTC.readDateString()              #Y vuelve a consultar la fecha

                currentTime = datetime.time.fromisoformat(timeRTC)       #gets datetime object
                currentDate = datetime.datetime.fromisoformat(dateRTC)
                currentTimeDate = datetime.datetime(year=currentDate.year,
                                                    month=currentDate.month,
                                                    day = currentDate.day,
                                                    hour=currentTime.hour,
                                                    minute=currentTime.minute,
                                                    second=currentTime.second)
                #print (currentTimeDate)
                return currentTimeDate
            if(x=='ADC'):
                return str(readValues())
            if x in status:                 #Y si se encuentra en la variable "status"
                #print(str({x : status.get(x)}))
                return json.dumps({x : status.get(x)})                  #Devuelvo el valor correspondiente
        else:                   #Si no especificó ningun parámetro en particular, devuelve el objeto entero
            #print(status)
            return json.dumps(status)

    def POST(self):         #Aquí defino qué variables quiero modificar, ej: GET -> status?Idioma="es-AR"
        input = web.input()
        # Todo lo recibido con POST, es un string, así que debo analizar el valor
        #de la solicitud, para ver si es un número, o un valor booleano
        for x in input.keys():              #Analizo las claves ("key") de lo solicitado
            try:                            #Primero reviso si el valor recibido es un número
                if(int(input[x])):          
                    input[x] = int(input[x])        #Es un número, lo reescribo como tal
                #print(input[x])
                #print(type(input[x]))
            except:                                 #No es un número
                print("Not a Number")               #devuelve una excepción la instrucción "int(input[x])"

            if(input[x]=="True"):                   #Si el valor de la solicitud es el texto "True"
                input[x]=True                       #sobreescribo con la variable booleana True
            elif(input[x]=="False"):                #Lo mismo si es el texto "False"
                input[x]=False                      #sobreescribo con la variable booleana False
            status.update({x:input[x]})             #y actualizo el valor en la variable "status"

            if x in essentials:         #Busca si se encuentra dentro de las variables esenciales
                with open(statusFile, "w") as st:
                    json.dump(status,st)

            if(x == "time"):                 #Modifico la hora
                newTimeDate = datetime.datetime.fromisoformat(input[x])
 
                timeRTC = datetime.time(hour = newTimeDate.hour,
                                        minute = newTimeDate.minute,
                                        second = newTimeDate.second)
                response = RTC.writeTimeString(timeRTC.strftime("%H:%M:%s"))
                while(response == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    response = RTC.writeTimeString(timeRTC.strftime("%H:%M:%s"))              #Y vuelve a intentar guardar la hora

                dateRTC = datetime.datetime(year=newTimeDate.year,
                                            month=newTimeDate.month,
                                            day = newTimeDate.day)
                response = RTC.writeDateString(dateRTC.strftime("%Y-%m-%d"))
                while(response == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    response = RTC.writeDateString(dateRTC.strftime("%Y-%m-%d"))              #Y vuelve a consultar la fecha                          

            if (x == 'LED_Light'):          #se quiere encender o apagar la luz LED
                if(input[x]):
                    LED.duty_cycle(status.get('LEDPWM'))
                else:
                    LED.duty_cycle(0)
                
            if(x == 'LEDPWM'):
                if(status.get('LED_Light')):
                    LED.duty_cycle(status.get('LEDPWM'))

            if(x == 'puerta'):
                if(input[x] == "subir_init"):
                    subirPuerta = threading.Thread(target= controlPuerta.subirPuerta_init) 
                    subirPuerta.start()
                    pass
                elif(input[x] == "subir_cont"):
                    controlPuerta.subirPuerta_cont()
                    pass
                elif(input[x] == "bajar_init"):
                    subirPuerta = threading.Thread(target= controlPuerta.bajarPuerta_init) 
                    subirPuerta.start()
                    pass
                elif(input[x] == "bajar_cont"):
                    controlPuerta.bajarPuerta_cont()
                    pass
                elif(input[x] == "trabajo"):
                    pass
                elif(input[x] == "abrir"):
                    pass
                elif(input[x] == "cerrar"):
                    pass

        #Finalmente, devuelve el valor de la variable status que se modificó
        return json.dumps({x: status.get(x) for x in input.keys()})

class ADC:
    def __init__(self):
        global mediciones

    def GET(self):
        time.sleep(0.01)

        input = web.input()             #What ADC reading was requested
        for x in input.keys():          
            pass
        #print(f"GET: {mediciones}")
        return json.dumps(mediciones)
        
    def POST(self):
        input = web.input()
        for x in input.keys():
            mediciones[x] = input[x]

        #print(f"POST: {mediciones}")
        return "Ok"

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


if __name__ == "__main__":
    #loopTimer = TIMER()
    #clock = threading.Thread(target=loopTimer.timer10ms,daemon=True)
    #clock.start()

    app.run()
