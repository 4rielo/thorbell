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
import os

#Módulos de manejo de puertos de I/O e I2C
#import ADS1115
import MCP23017
from DS3231 import DS3231
from MCP23017 import MCP23017
from puerta import PUERTA
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
LED.start_pwm()

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
urls = ('/','root', 
        '/status', 'Status',
        '/adc','ADC', 
        '/language','language',
        '/reboot','reboot'
        )

#Dirección de la carpeta, donde se encuentra el archivo ejecutado
path = __file__.replace("/statusServer.py","")
if(not path):
    path = "."

#Dirección de la ubicación del archivo "status.dat"
statusFile= f"{path}/CSB_MercurioR1/status.dat"

#Dirección de la ubicación del directorio de idiomas
languagePath = f"{path}/CSB_MercurioR1/idioma"

#intenta abrir el archivo "status.dat"
try:                 
    print("Trying to open status file")
    f=open(statusFile)              #Busca el archivo statusFile, si existe, lo abre
    status = json.load(f)             #y carga el último estado guardado
    f.close()                       #(cierra el archivo, no lo necesita por ahora)
    print("Status File found, reading initial status")
except:                             #Si no econtró el arvchivoa
    uv_timer=datetime.time.min.__str__()
    now = format(datetime.datetime.now(),"%Y/%m/%d %H:%M")
    status = {                        #genera un status inicial
        "Idioma": "es-AR", 
        
        "LED_Light": False, 
        "LEDPWM": 100, 
        
        "UV_Light": False, 
        "UV_TimerEnable": False,
        "UV_Timer": uv_timer, 
        
        "UVLEDPWM": 100, 
        
        "UV_Calendar": False, 
        "UV_Calendar_init": now, 
        "UV_Calendar_end": now, 

        "Rutina_Calendar": False,
        "Rutina_Calendar_init": now, 
        "Rutina_Calendar_end": now, 

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

#reads current language
try:                 
    print("Trying to open language file")
    f=open(f"{languagePath}/{status['Idioma']}.dat")              #Busca el archivo statusFile, si existe, lo abre
    idioma = json.load(f)             #y carga el último estado guardado
    f.close()                       #(cierra el archivo, no lo necesita por ahora)
    print("Language File found, reading initial status")
except:                             #Si no econtró el arvchivo
    language = {
        "separador_de_PantallaPrincipal": "*********************",
        "luminariaLED" : "Luminaria\nLED",
        "luminariaUV" : "Luminaria\nUV",
        "rutina" : "Rutina",
        "puerta" : "Control de puerta",
        "separador_de_PantallaInfo": "*********************",
        "postVenta" : "Servicio Post Venta",
        "separador_de_Pantalla_LuminariaLED": "*********************",
        "LEDTittle" : "Luminaria LED",
        "separador_de_Pantalla_LuminariaUV": "*********************",
        "UVTittle" : "Luminaria UV",
        "separador_de_Pantalla_Configuracion": "*********************",
        "configTittle" : "Configuración",
        "separador_de_Pantalla_Advertencia": "*********************",
        "warningTittle" : "Advertencia" ,
        "puerta_abierta" : "Puerta Abierta",
        "filtro_saturado" : "Filtro Saturado",
        "filtro_roto" : "Filtro Roto",
        "filtro_proximo_a_saturarse" : "Filtro próximo a saturarse",
        "ventilador_roto" : "Ventilador Roto",
        "separador_de_Pantalla_LogIn": "*********************",
        "loginTittle" : "Login",
        "separador_de_Pantalla_LuminariaLED": "*********************",
        "clockTittle": "Configuración de Fecha y Hora",
        "horaActual" : "Hora Actual",
        "fechaActual" : "Fecha Actual",
        "separador_de_Pantalla_Calendario": "*********************",
        "calendarTittle" : "Calendario",
        "calendarUV" : "Calendario de UV",
        "calendarRutina" : "Calendario de Rutina",
        "calendarInit" : "Inicio",
        "calendarEnd": "Apagado",
        "separador_de_Pantalla_ControlDePuerta": "*********************",
        "puertaTittle": "Posición de la puerta"
    }
    status.update({'Idioma' : 'es-AR'})
    with open(f"{languagePath}/{status['Idioma']}.dat", "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
        json.dump(language,f)
    print("Language file not found. Creates initial (default) language file")

#TODO: Aquí se obtiene el tiempo del reloj SPI, y se revisa si hay conexión a 
# internet. 

#################################################################################
app = web.application(urls,globals())       #Creates server, and passes it global variables

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
                    time.sleep(0.002)                           #Espera un muy breve instante a que se desocupe
                    timeRTC = RTC.readTimeString()              #Y vuelve a consultar la hora

                dateRTC = RTC.readDateString()
                while(dateRTC == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.002)                           #Espera un muy breve instante a que se desocupe
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
                    posTrabajoPuerta = threading.Thread(target= controlPuerta.puertaPosicionCorrecta) 
                    posTrabajoPuerta.start()
                    pass
                elif(input[x] == "abrir"):
                    abrirPuerta = threading.Thread(target= controlPuerta.abrirPuerta) 
                    abrirPuerta.start()
                    pass
                elif(input[x] == "cerrar"):
                    cerrarPuerta = threading.Thread(target= controlPuerta.cerrarPuerta) 
                    cerrarPuerta.start()
                    pass

        #Finalmente, devuelve el valor de la variable status que se modificó
        return json.dumps({x: status.get(x) for x in input.keys()})

class language:
    def __init__(self):
        global status

    def GET(self):                      #requests language
        input=web.input()
        if(input):                      #There's a specific language request. Wants to know available languages
            #for x in input.keys():                
            availableLanguages = os.listdir(languagePath)
            return json.dumps(availableLanguages)
        
        try:                        #By default, grabs current language
            print("Trying to open status file")
            f=open(f"{languagePath}/{status['Idioma']}.dat")              #Busca el archivo statusFile, si existe, lo abre
            idioma = json.load(f)             #y carga el último estado guardado
            f.close()                       #(cierra el archivo, no lo necesita por ahora)
            print("Language File found, reading initial status")
        except:                             #Si no econtró el arvchivo
            idioma = {
                "separador_de_PantallaPrincipal": "*********************",
                "luminariaLED" : "Luminaria\nLED",
                "luminariaUV" : "Luminaria\nUV",
                "rutina" : "Rutina",
                "puerta" : "Control de puerta",
                "separador_de_PantallaInfo": "*********************",
                "postVenta" : "Servicio Post Venta",
                "separador_de_Pantalla_LuminariaLED": "*********************",
                "LEDTittle" : "Luminaria LED",
                "separador_de_Pantalla_LuminariaUV": "*********************",
                "UVTittle" : "Luminaria UV",
                "separador_de_Pantalla_Configuracion": "*********************",
                "configTittle" : "Configuración",
                "separador_de_Pantalla_Advertencia": "*********************",
                "warningTittle" : "Advertencia" ,
                "puerta_abierta" : "Puerta Abierta",
                "filtro_saturado" : "Filtro Saturado",
                "filtro_roto" : "Filtro Roto",
                "filtro_proximo_a_saturarse" : "Filtro próximo a saturarse",
                "ventilador_roto" : "Ventilador Roto",
                "separador_de_Pantalla_LogIn": "*********************",
                "loginTittle" : "Login",
                "separador_de_Pantalla_LuminariaLED": "*********************",
                "clockTittle": "Configuración de Fecha y Hora",
                "horaActual" : "Hora Actual",
                "fechaActual" : "Fecha Actual",
                "separador_de_Pantalla_Calendario": "*********************",
                "calendarTittle" : "Calendario",
                "calendarUV" : "Calendario de UV",
                "calendarRutina" : "Calendario de Rutina",
                "calendarInit" : "Inicio",
                "calendarEnd": "Apagado",
                "separador_de_Pantalla_ControlDePuerta": "*********************",
                "puertaTittle": "Posición de la puerta"
            }
            status.update({'Idioma' : 'es-AR'})
            with open(f"{languagePath}/{status['Idioma']}.dat", "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
                json.dump(idioma,f)
            print("Language file not found. Creates initial (default) language file")
        
        return json.dumps(idioma)       #finally, returns a json object-like string containing language info
    

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

if __name__ == "__main__":
    #loopTimer = TIMER()
    #clock = threading.Thread(target=loopTimer.timer10ms,daemon=True)
    #clock.start()

    app.run()
