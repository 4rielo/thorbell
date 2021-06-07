#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import requests
import json
from datetime import datetime, date

import main
from Pcalendar import Ui_form

class CalendarWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(CalendarWindow, self).__init__() 
        self.setupUi(self)
        self.setWindowTitle("CONFIG")
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        try:
            #Obtiene el "status" general
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            pass

        #Revisa si está encendido la función de calendario (Por defecto, inicia en UV Calendar)
        if(self.status.get("UV_Calendar")):
            self.onOffBtn.setChecked(True)
            self.onOffBtn.setText("On")
        else:
            self.onOffBtn.setChecked(False)
            self.onOffBtn.setText("Off")
        
        
        #Título de la pantalla de calendario
        calendar = f"{main.texto.get('calendarTittle')}"
        self.tittleGlow.setText(calendar)
        self.tittle.setText(calendar)

        #Sub-Título de la pantalla de calendario - Inicializa en Calendario UV
        calendar = f"{main.texto.get('calendarUV')}"
        self.subTittleGlow.setText(calendar)
        self.subTittle.setText(calendar)

        #Etiquetas de inicio y fin
        self.inicioLbl.setText(f"{main.texto.get('calendarInit')}")
        self.endLbl.setText(f"{main.texto.get('calendarEnd')}")
        
        #Inicia en modo de calendario de UV
        self.uvBtn.setChecked(True)
        self.rutinaBtn.setChecked(False)
        self.uvBtn.clicked.connect(self.toggleRutinaUV)
        self.rutinaBtn.clicked.connect(self.toggleRutinaUV2)

        #Obtiene la fecha de inicio del archivo de status
        self.changeDisplay("UV")

        #*****************Asignación de funciones según botones
        #botón de salir
        self.return_Btn.clicked.connect(self.goBack)

        #Botones de fecha y hora de inicio
        self.initDatePlusBtn.clicked.connect(self.increaseInitDate)
        self.initDatePlusBtn.setAutoRepeat(True)
        self.initDatePlusBtn.setAutoRepeatDelay(500)
        self.initDatePlusBtn.setAutoRepeatInterval(100)

        self.initDateMinusBtn.clicked.connect(self.decreaseInitDate)
        self.initDateMinusBtn.setAutoRepeat(True)
        self.initDateMinusBtn.setAutoRepeatDelay(500)
        self.initDateMinusBtn.setAutoRepeatInterval(100)

        self.initTimePlusBtn.clicked.connect(self.increaseInitTime)
        self.initTimePlusBtn.setAutoRepeat(True)
        self.initTimePlusBtn.setAutoRepeatDelay(500)
        self.initTimePlusBtn.setAutoRepeatInterval(100)
        
        self.initTimeMinusBtn.clicked.connect(self.decreaseInitTime)
        self.initTimeMinusBtn.setAutoRepeat(True)
        self.initTimeMinusBtn.setAutoRepeatDelay(500)
        self.initTimeMinusBtn.setAutoRepeatInterval(100)

        #Botones de fecha y hora de fin
        self.endDatePlusBtn.clicked.connect(self.increaseEndDate)
        self.endDatePlusBtn.setAutoRepeat(True)
        self.endDatePlusBtn.setAutoRepeatDelay(500)
        self.endDatePlusBtn.setAutoRepeatInterval(100)

        self.endDateMinusBtn.clicked.connect(self.decreaseEndDate)
        self.endDateMinusBtn.setAutoRepeat(True)
        self.endDateMinusBtn.setAutoRepeatDelay(500)
        self.endDateMinusBtn.setAutoRepeatInterval(100)

        self.endTimePlusBtn.clicked.connect(self.increaseEndTime)
        self.endTimePlusBtn.setAutoRepeat(True)
        self.endTimePlusBtn.setAutoRepeatDelay(500)
        self.endTimePlusBtn.setAutoRepeatInterval(100)

        self.endTimeMinusBtn.clicked.connect(self.decreaseEndTime)
        self.endTimeMinusBtn.setAutoRepeat(True)
        self.endTimeMinusBtn.setAutoRepeatDelay(500)
        self.endTimeMinusBtn.setAutoRepeatInterval(100)


        #Botones de encendido y apagado
        self.onOffBtn.clicked.connect(self.CalendarOnOff)

        #Modificación de fechas y hora de inicio y fin - Actualización del valor
        self.initDateEdit.dateChanged.connect(self.updateInitDate)
        self.initTimeEdit.timeChanged.connect(self.updateInitDate)

        self.endDateEdit.dateChanged.connect(self.updateEndDate)
        self.endTimeEdit.timeChanged.connect(self.updateEndDate)

    #***************************************************************

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def changeDisplay(self, what = "UV"):
        if(what == "UV"):
            print("UV raise")
            self.uvBtn.setChecked(True)
            self.rutinaBtn.setChecked(False)

            #Pongo el título indicativo de modificación de calendario de UV
            calendar = f"{main.texto.get('calendarUV')}"
            self.subTittleGlow.setText(calendar)
            self.subTittle.setText(calendar)

            #Actualizo la información en pantalla, para coincidir con los valores almacenados de UV
            if(self.status.get("UV_Calendar")):
                self.onOffBtn.setChecked(True)
                self.onOffBtn.setText("On")
            else:
                self.onOffBtn.setChecked(False)
                self.onOffBtn.setText("Off")

            init_Status = datetime.strptime(self.status.get("UV_Calendar_init"), "%Y/%m/%d %H:%M")
            end_Status = datetime.strptime(self.status.get("UV_Calendar_end"), "%Y/%m/%d %H:%M")
        
        elif(what == "Rutina"):
            print("Rutina raise")
            self.uvBtn.setChecked(False)
            self.rutinaBtn.setChecked(True)

            #Pongo el título indicativo de modificación de calendario de Rutina
            calendar = f"{main.texto.get('calendarRutina')}"
            self.subTittleGlow.setText(calendar)
            self.subTittle.setText(calendar)

            #Actualizo la información en pantalla, para coincidir con los valores almacenados de Rutina
            if(self.status.get("Rutina_Calendar")):
                self.onOffBtn.setChecked(True)
                self.onOffBtn.setText("On")
            else:
                self.onOffBtn.setChecked(False)
                self.onOffBtn.setText("Off")
            init_Status = datetime.strptime(self.status.get("Rutina_Calendar_init"), "%Y/%m/%d %H:%M")    
            end_Status = datetime.strptime(self.status.get("Rutina_Calendar_end"), "%Y/%m/%d %H:%M")

        init_Day = date(init_Status.year,init_Status.month,init_Status.day)
        end_Day = date(end_Status.year, end_Status.month, end_Status.day)

        self.today=date.today()         #Obtiene la fecha de hoy
        #Si la fecha de hoy es más actual que la almacenada en "status.dat"
        #Se muestra la fecha y hora actual en inicio y fin
        if(self.today>end_Day):     
            todayQt = PySide2.QtCore.QDate(self.today.year, self.today.month, self.today.day)
            endDayQt = PySide2.QtCore.QDate(self.today.year, self.today.month, self.today.day)
            self.now=datetime.now()
            initHourQt = PySide2.QtCore.QTime(self.now.hour, self.now.minute)
            endHourQt = PySide2.QtCore.QTime(self.now.hour, self.now.minute)
            
        else: 
            todayQt = PySide2.QtCore.QDate(init_Status.year, init_Status.month, init_Status.day)
            endDayQt = PySide2.QtCore.QDate(end_Status.year, end_Status.month, end_Status.day)
            initHourQt = PySide2.QtCore.QTime(init_Status.hour, init_Status.minute)            
            endHourQt = PySide2.QtCore.QTime(end_Status.hour, end_Status.minute)
            
        self.initDateEdit.setDate(todayQt)
        self.endDateEdit.setDate(endDayQt)
        self.initTimeEdit.setTime(initHourQt)
        self.endTimeEdit.setTime(endHourQt)

    def toggleRutinaUV(self):
        #print("Toggle")
        if(self.uvBtn.isChecked()):
            self.changeDisplay("UV")
        else:
            self.changeDisplay("Rutina")

    def toggleRutinaUV2(self):
        #print("Toggle")
        if(self.rutinaBtn.isChecked()):
            self.changeDisplay("Rutina")
        else:
            self.changeDisplay("UV")

    def CalendarOnOff(self):
        if(self.onOffBtn.isChecked()):          #(is checked -> ON)
            self.onOffBtn.setText("On")
            if(self.uvBtn.isChecked()):             #Y guardo en localhost el encendido, de rutina o UV, según corresponda
                self.status.update({"UV_Calendar" : True })
                response = requests.post(main.localhost,params= {"UV_Calendar" : True })
            elif(self.rutinaBtn.isChecked()):
                self.status.update({"Rutina_Calendar" : True })
                respose = requests.post(main.localhost,params= {"Rutina_Calendar" : True })

        else:                                   #(is NOT checked -> OFF)
            self.onOffBtn.setText("Off")
            if(self.uvBtn.isChecked()):             #Y guardo en localhost el encendido, de rutina o UV, según corresponda
                self.status.update({"UV_Calendar" : False })
                response = requests.post(main.localhost,params= {"UV_Calendar" : False })
            elif(self.rutinaBtn.isChecked()):
                self.status.update({"Rutina_Calendar" : False })
                respose = requests.post(main.localhost,params= {"Rutina_Calendar" : False })


    def increaseInitDate(self):
        self.initDateEdit.setDate(self.initDateEdit.date().addDays(1))      #Incremento el día de inicio por uno
        
        endDate=self.endDateEdit.date()        #Día de fin
        initDate=self.initDateEdit.date()      #Día de inicio 
        
        if (endDate < initDate):                #Si incremento el día de inicio por encima del día de fin,
            self.endDateEdit.setDate(initDate)   #Incremento el día de fin para igualar el día de inicio
            #Como actualizo el día de fin, chequeo que la hora de fin no sea menor que la hora de inicio
            if(self.endTimeEdit.time()<self.initTimeEdit.time()):       
                self.endTimeEdit.setTime(self.initTimeEdit.time())      #De ser así, actualizo la hora de fin

    def decreaseInitDate(self):
        newDate=self.initDateEdit.date().addDays(-1)
        if (newDate >= self.today):         #Sólo deja decrementar hasta la fecha actual
            self.initDateEdit.setDate(newDate)

    def increaseInitTime(self):
        self.initTimeEdit.setTime(self.initTimeEdit.time().addSecs(60))
        #Si incremento la hora, y el día de fin es el mismo que el actual
        #chequeo la hora de fin, para "arrastrarla" con la hora de inicio
        #De esta forma, la hora de fin será siempre por lo menos un minuto 
        #mayor que la de inicio.
        if(self.initDateEdit.date() == self.endDateEdit.date()):
            if(self.endTimeEdit.time()<=self.initTimeEdit.time()):
                self.endTimeEdit.setTime(self.initTimeEdit.time().addSecs(60))


    def decreaseInitTime(self):
        setDate=self.initDateEdit.date()        #Día de inicio configurado
        
        self.today=date.today()                 #Día actual
        self.today = PySide2.QtCore.QDate(self.today.year, self.today.month, self.today.day)

        self.now = datetime.now()                 #Hora actual
        CurrentTimeQt = PySide2.QtCore.QTime(self.now.hour, self.now.minute)

        if(setDate == self.today):              #Si el día seteado es hoy
            newTime=self.initTimeEdit.time().addSecs(-60)
            #No permite decrementar la hora de inicio por debajo de la hora actual
            if(newTime >= CurrentTimeQt):               
                self.initTimeEdit.setTime(newTime)
        else:           #Si se está programando la alarma para otro día
            self.initTimeEdit.setTime(self.initTimeEdit.time().addSecs(-60))            #Puede ser cualquier hora

    def increaseEndDate(self):
        self.endDateEdit.setDate(self.endDateEdit.date().addDays(1))

    def decreaseEndDate(self):
        newDate=self.endDateEdit.date().addDays(-1)        #Nuevo día de fin, menos 1
        initDate=self.initDateEdit.date()                   #Día de inicio 
        #El mínimo día de fin, es el mismo día de inicio
        if (newDate >= initDate):
            self.endDateEdit.setDate(newDate)

    def increaseEndTime(self):
        #Chequeo si la fecha de inicio es la misma que la fecha de fin
        if(self.initDateEdit.date() == self.endDateEdit.date()):
            #De ser así, verifico que el tiempo de fin sea mayor al tiempo de inicio
            if(self.endTimeEdit.time()<=self.initTimeEdit.time()):
                self.endTimeEdit.setTime(self.initTimeEdit.time().addSecs(60))
            else:
                self.endTimeEdit.setTime(self.endTimeEdit.time().addSecs(60))
        else:
            self.endTimeEdit.setTime(self.endTimeEdit.time().addSecs(60))

    def decreaseEndTime(self):
        #Si las fechas de inicio y fin coinciden
        if(self.initDateEdit.date() == self.endDateEdit.date()):
            if(self.endTimeEdit.time()>self.initTimeEdit.time().addSecs(60)):       
                #Sólo decrementa mientras el tiempo final sea mayor a el inicial más un minuto
                #(es decir, el tiempo final siempre va a ser, por lo menos, 1 minuto más que el inicial)
                self.endTimeEdit.setTime(self.endTimeEdit.time().addSecs(-60))
        else:
            #Si la fecha final es distinta a la inicial (nunca puede ser menor)
            #Decrementa la hora final por un minuto
            self.endTimeEdit.setTime(self.endTimeEdit.time().addSecs(-60))

    def updateInitDate(self):
        #Antes de guardar, verifica que, si la fecha/hora de fin son menores
        #que la fecha de inicio.
        if(self.endDateEdit.date() < self.initDateEdit.date()):
            self.endDateEdit.setDate(self.initDateEdit.date())
        if(self.initDateEdit.date() == self.endDateEdit.date()):
            if(self.endTimeEdit.time()<=self.initTimeEdit.time()):
                self.endTimeEdit.setTime(self.initTimeEdit.time().addSecs(60))
        #Cuando cambia la fecha de inicio, y ninguno de los pulsadores de + y - están presionados
        #actualizo la fecha de inicio en "status.dat"
        if(not self.initDateMinusBtn.isDown() and not self.initDatePlusBtn.isDown()
            and not self.initTimeMinusBtn.isDown() and not self.initTimePlusBtn.isDown()):
            
            initDate=self.initDateEdit.date()
            initHour=self.initTimeEdit.time()
            init_Status= datetime(initDate.year(),initDate.month(),initDate.day(),initHour.hour(),initHour.minute())

            if(self.uvBtn.isChecked()):
                self.status.update({"UV_Calendar_init": format(init_Status,"%Y/%m/%d %H:%M")})
                try:
                    response = requests.post(f"{main.localhost}/status",params = {"UV_Calendar_init": format(init_Status,"%Y/%m/%d %H:%M")})
                except:
                    #TODO: handling microprocess request failure
                    pass
            elif(self.rutinaBtn.isChecked()):
                self.status.update({"Rutina_Calendar_init": format(init_Status,"%Y/%m/%d %H:%M")})
                try:
                    response = requests.post(f"{main.localhost}/status",params = {"Rutina_Calendar_init": format(init_Status,"%Y/%m/%d %H:%M")})
                except:
                    #TODO: handling microprocess request failure
                    pass

    def updateEndDate(self):
        #Antes de guardar, verifica que, si la fecha/hora de fin son menores
        #que la fecha de inicio.
        if(self.endDateEdit.date() < self.initDateEdit.date()):
            self.endDateEdit.setDate(self.initDateEdit.date())
        if(self.initDateEdit.date() == self.endDateEdit.date()):
            if(self.endTimeEdit.time()<=self.initTimeEdit.time()):
                self.endTimeEdit.setTime(self.initTimeEdit.time().addSecs(60))
        #Cuando cambia la fecha de fin, y ninguno de los pulsadores de + y - están presionados
        #actualizo la fecha de fin en "status.dat"
        #También tiene que checkear los botones de "+" del init date, porque la fecha de inicio
        #no puede ser mayor que la fecha de fin, y "arrastra" la fecha de fin cuando incrementa
        if(not self.endDateMinusBtn.isDown() and not self.endDatePlusBtn.isDown()
            and not self.endTimeMinusBtn.isDown() and not self.endTimePlusBtn.isDown()
            and not self.initDatePlusBtn.isDown()):
            endDate=self.endDateEdit.date()
            endHour=self.endTimeEdit.time()
            end_Status = datetime(endDate.year(),endDate.month(),endDate.day(),endHour.hour(),endHour.minute())

            if(self.uvBtn.isChecked()):
                self.status.update({"UV_Calendar_end": format(end_Status,"%Y/%m/%d %H:%M")})
                try:
                    response = requests.post(f"{main.localhost}/status",params = {"UV_Calendar_end": format(end_Status,"%Y/%m/%d %H:%M")})
                except:
                    #TODO: handling microprocess request failure
                    pass
            elif(self.rutinaBtn.isChecked()):
                self.status.update({"Rutina_Calendar_end": format(end_Status,"%Y/%m/%d %H:%M")})
                try:
                    response = requests.post(f"{main.localhost}/status",params = {"Rutina_Calendar_end": format(end_Status,"%Y/%m/%d %H:%M")})
                except:
                    #TODO: handling microprocess request failure
                    pass

            #print(format(end_Status,"%Y/%m/%d %H:%M"))