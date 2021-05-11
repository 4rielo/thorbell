#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import main
import json
from datetime import datetime, date

from Pcalendar import Ui_form

class CalendarWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

        print("Open: " + main.texto.get("configTittle"))

        with open(main.statusFile) as f:
            status=json.load(f)                 #Carga el estado de "status"

        #Revisa si está encendido la función de calendario
        if(status.get("UV_Calendar")):
            self.onBtn.setChecked(True)
            self.offBtn.setChecked(False)
        else:
            self.onBtn.setChecked(False)
            self.offBtn.setChecked(True)
        

        calendar = f"{main.texto.get('calendarTittle')}"
        self.tittleGlow.setText(calendar)
        self.tittle.setText(calendar)

        self.inicioLbl.setText(f"{main.texto.get('calendarInit')}")
        self.endLbl.setText(f"{main.texto.get('calendarEnd')}")
        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        #Obtiene la fecha de inicio del archivo de status
        init_Status = datetime.strptime(status.get("UV_Calendar_init"), "%Y/%m/%d %H:%M")
        init_Day = date(init_Status.year,init_Status.month,init_Status.day)
        end_Status = datetime.strptime(status.get("UV_Calendar_end"), "%Y/%m/%d %H:%M")
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

        self.onBtn.clicked.connect(self.UVCalendarON)
        self.offBtn.clicked.connect(self.UVCalendarOFF)

        self.initDateEdit.dateChanged.connect(self.updateInitDate)
        self.initTimeEdit.timeChanged.connect(self.updateInitDate)

        self.endDateEdit.dateChanged.connect(self.updateEndDate)
        self.endTimeEdit.timeChanged.connect(self.updateEndDate)

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def UVCalendarON(self):
        if(self.onBtn.isChecked()):
            self.onBtn.setChecked(True)
            self.offBtn.setChecked(False)
            with open(main.statusFile) as f:
                status=json.load(f)                 #Carga el estado de "status"
            status.update({"UV_Calendar": True})
            with open(main.statusFile,"w") as f:
                json.dump(status, f)                 #Carga el estado de "status"
        else:
            self.onBtn.setChecked(True)

    def UVCalendarOFF(self):
        if(self.offBtn.isChecked()):
            self.onBtn.setChecked(False)
            self.offBtn.setChecked(True)
            with open(main.statusFile) as f:
                status=json.load(f)                 #Carga el estado de "status"
            status.update({"UV_Calendar": False})
            with open(main.statusFile,"w") as f:
                json.dump(status, f)                 #Carga el estado de "status"
        else:
            self.offBtn.setChecked(True)

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
            init_Status = datetime(initDate.year(),initDate.month(),initDate.day(),initHour.hour(),initHour.minute())
            print(format(init_Status,"%Y/%m/%d %H:%M"))
            with open(main.statusFile) as f:
                status=json.load(f)                 #Carga el estado de "status"
            status.update({"UV_Calendar_init": format(init_Status,"%Y/%m/%d %H:%M")})
            with open(main.statusFile,"w") as f:
                json.dump(status, f)                 #Carga el estado de "status"

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
            print(format(end_Status,"%Y/%m/%d %H:%M"))
            with open(main.statusFile) as f:
                status=json.load(f)                 #Carga el estado de "status"
            status.update({"UV_Calendar_end": format(end_Status,"%Y/%m/%d %H:%M")})
            with open(main.statusFile,"w") as f:
                json.dump(status, f)                 #Carga el estado de "status"