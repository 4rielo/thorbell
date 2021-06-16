import requests
import time
import json

import ADS1115

class TIMER:
    def __init__(self):
        self.flujoEntrada=float()
        self.flujoSalida=float()
        self.presionEntrada=float()
        self.presionSalida=float()

        self.status=dict()

        self.localhost = "http://localhost:8085"

        try:
            self.status = json.loads(requests.get(f"{self.localhost}/status").text)

        self.mediciones = { 'flujoEntrada' : self.flujoEntrada , 
                        'flujoSalida' : self.flujoSalida , 
                        'presionEntrada' : self.presionEntrada , 
                        'presionSalida' : self.presionSalida
                        }
        
        self.lectura = 0

    def timer10ms(self):
        sec1=0 
        ads1 = 0x48
        ads2 = 0x49

        ADS1115_FS_4096 = 1
        ADS1115_FS_2048 = 2
        ADS1115_FS_1024 = 3
        ADS1115_FS_512 = 4

        acumTmp_flujoEntrada = 0
        acumRv_flujoEntrada = 0

        acumTmp_flujoSalida = 0
        acumRv_flujoSalida = 0

        acumPresion_Entrada = 0
        acumPresion_Salida = 0

        contadorMediciones = 0

        while(True):

            sec1 += 1
        
            #Mido temperatura y Rv de flujo de entrada, y acumulo para sacar medición promedio
            if(not self.lectura):
                ADC_reading=ADS1115.ReadADC(ads1,5,ADS1115_FS_4096)     #intenta leer
                while(ADC_reading == "ERROR"):                      #si devuelve ERROR (puerto I2C ocupado)
                    time.sleep(0.001)                               #espera 3 ms
                    ADC_reading=ADS1115.ReadADC(ads1,5,ADS1115_FS_4096) #e intenta nuevamente
                acumTmp_flujoEntrada += ADC_reading
                self.lectura += 1
            elif(self.lectura == 1):
                ADC_reading=ADS1115.ReadADC(ads1,4,ADS1115_FS_4096)
                while(ADC_reading == "ERROR"):
                    time.sleep(0.001)
                    ADC_reading=ADS1115.ReadADC(ads1,4,ADS1115_FS_4096)
                acumRv_flujoEntrada += ADC_reading
                self.lectura += 1
            elif(self.lectura==2):
                #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
                ADC_reading=ADS1115.ReadADC(ads1,7,ADS1115_FS_4096)
                while(ADC_reading == "ERROR"):
                    time.sleep(0.001)
                    ADC_reading=ADS1115.ReadADC(ads1,7,ADS1115_FS_4096)
                acumTmp_flujoSalida += ADC_reading
                self.lectura += 1
            elif(self.lectura==3):
                ADC_reading=ADS1115.ReadADC(ads1,6,ADS1115_FS_4096)
                while(ADC_reading == "ERROR"):
                    time.sleep(0.001)
                    ADC_reading=ADS1115.ReadADC(ads1,6,ADS1115_FS_4096)
                acumRv_flujoSalida += ADC_reading
                self.lectura += 1
            elif(self.lectura==4):
                ADC_reading=ADS1115.ReadADC(ads2,4,ADS1115_FS_512)
                while(ADC_reading == "ERROR"):
                    time.sleep(0.001)
                    ADC_reading=ADS1115.ReadADC(ads2,4,ADS1115_FS_512)
                acumPresion_Entrada += ADC_reading
                self.lectura += 1
            elif(self.lectura==5):
                ADC_reading=ADS1115.ReadADC(ads2,5,ADS1115_FS_512) 
                while(ADC_reading == "ERROR"):
                    time.sleep(0.001)
                    ADC_reading=ADS1115.ReadADC(ads2,5,ADS1115_FS_512) 
                acumPresion_Salida += ADC_reading #"""
                self.lectura=0
                contadorMediciones +=1          #incremento la cantidad de mediciones
            
            
            """#bloque de números RANDOM para probar el código en la PC
            acumTmp_flujoEntrada += random.randint(1000,2096)
            acumRv_flujoEntrada += random.randint(2000,3096)

            #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
            acumTmp_flujoSalida += 100#random.randint(00,500)
            acumRv_flujoSalida += random.randint(2000,2500)

            acumPresion_Entrada += random.randint(1000,2096)
            acumPresion_Salida += random.randint(2000,2596) #"""

            if(contadorMediciones>9):        #10 mediciones para calcular el promedio (contador de 0 a 9)

                """Cálculo de flujo de Entrada"""
                rvEntrada = acumRv_flujoEntrada/10.0          #promedio de 10 mediciones
                tmpEntrada = acumTmp_flujoEntrada/10.0        #promedio de 10 mediciones
                
                #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
                velCeroEntrada = -0.0006 * tmpEntrada * tmpEntrada / 1024.0 + 1.0727 * tmpEntrada/32.0 + 8.172
                rvEntrada /= 32.0
                velCeroEntrada = (rvEntrada - velCeroEntrada) * 0.01739
                if(velCeroEntrada < 0):
                    velCeroEntrada = 0.0
                
                self.flujoEntrada = pow(velCeroEntrada,2.7265) * 160.934

                """Cálculo de flujo de Salida"""
                rvSalida = acumRv_flujoSalida/10.0          #promedio de 10 mediciones
                tmpSalida = acumTmp_flujoSalida/10.0        #promedio de 10 mediciones
                
                #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
                velCeroSalida = -0.0006 * tmpSalida * tmpSalida / 1024.0 + 1.0727 * tmpSalida/32.0 + 8.172
                rvSalida /= 32.0
                velCeroSalida = (rvSalida - velCeroSalida) * 0.01739
                if(velCeroSalida < 0):
                    velCeroSalida = 0.0
                
                self.flujoSalida = pow(velCeroSalida,2.7265) * 160.934

                """Cálculo de presion de flujo de entrada """
                self.presionEntrada = acumPresion_Entrada/10

                """Cálculo de presion de flujo de salida """
                self.presionSalida = acumPresion_Salida/10

                """Recopilo todas las mediciones en un dict"""
                self.mediciones = { 'flujoEntrada' : self.flujoEntrada , 
                    'flujoSalida' : self.flujoSalida , 
                    'presionEntrada' : self.presionEntrada , 
                    'presionSalida' : self.presionSalida
                    }
                #y lo envío al servidor, para que la pantalla y app web tengan un nuevo valor
                print(f"ADC: {self.mediciones}")
                try:
                    postData = requests.(f"{self.localhost}/adc" , params = self.mediciones)
                
                """ Reinicio contadores y acumuladores a cero"""
                acumTmp_flujoEntrada=0
                acumRv_flujoEntrada=0

                acumTmp_flujoSalida=0
                acumRv_flujoSalida=0

                acumPresion_Entrada = 0
                acumPresion_Salida = 0

                contadorMediciones=0

                try:
                    self.status = json.loads(app.request("/status", method = 'GET').data)

            if(sec1>100):       #Pasó 1 segundo
                sec1=0
                if(self.status.get('UV_Light')):
                    print("Turn on that damn light!!!")


            time.sleep(0.01)

timer = TIMER()
timer.timer10ms()