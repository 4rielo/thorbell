#Fprincipal.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

#import fbUpload
import time
import threading
from datetime import datetime, date
#from CSB_MercurioR1.Pprincipal import Ui_form
#from CSB_MercurioR1.Fconfig import ConfigWindow

from Pprincipal import Ui_form
from Fconfig import ConfigWindow

#import config
#import Fluminaria_led
#loader = QUiLoader()

counter = 0
lightPercent = 50
lightOnOff = True


class MainWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)

        self.setWindowTitle("THORBELL")

        #handler=lightHandler()

        #Create all sub-windows, to call on them when different buttons are clicked.
        #self.ConfigWindow = config.ConfigWindow()
        #self.LuminariaLED_Window = Fluminaria_led.WluminariaLED()
        self.configWindow = ConfigWindow()

        self.horizontalSlider.valueChanged.connect(self.Dial)
        self.horizontalSlider_2.valueChanged.connect(self.Dial2)

        self.config_Btn.clicked.connect(self.Config)

        #self.luz_Btn.setAutoRepeat(True)
        #self.luz_Btn.setAutoRepeatDelay(1000)

        #print(callable(luz.start))
        self.luz_Btn.pressed.connect(self.pressHandler)#handler.LuminariaLED_pressed)
        #self.luz_Btn.clicked.connect(handler.LuminariaLED_released)
        #self.upArrow.setText("Upload Reading")

        # icon = QtGui.QIcon("animal-penguin.png") self.centralWidget.#

        # self.button.setIcon(icon)

        #self.upArrow.clicked.connect(self.Upload)
        #self.pushButton.clicked.connect(self.Decrease)
        #self.pushButton_2.clicked.connect(self.Config)

        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        global lightOnOff
        if(lightOnOff):
            self.luz_Btn.setChecked=True
        else:
            self.luz_Btn.setChecked=False
        # self.setCentralWidget(self.button)
        #self.setFocus
        #self.show()
        currentTime=datetime.now().strftime("%H:%M:%S")
        self.hora.setText(currentTime)
        today=date.today().strftime("%d/%m/%Y")
        self.fecha.setText(today)
        self.firstKey=False

        self.ms100=0
        clock = threading.Thread(target=self.timer100ms,daemon=True)
        clock.start()

    def timer100ms(self):
        while(True):
            self.ms100 += 1
            if(self.ms100>10):
                self.ms100=0
                currentTime=datetime.now().strftime("%H:%M:%S")
                self.hora.setText(currentTime)
                today=date.today().strftime("%d/%m/%Y")
                self.fecha.setText(today)
            time.sleep(0.1)

    """Cuando presiono el botón de luminaria, comienza un thread que cuenta el tiempo que se sostiene presionado
    utilizando la función "LuminariaLED_pressed """
    def pressHandler(self):
        self.luz=threading.Thread(target=self.LuminariaLED_pressed,daemon=True)
        self.luz.start()
        
    """Con intervalos de 0.1 seg., cuenta 25 veces, chequeando el estado del botón de luz. Si en algun momento 
    se dejó de presionar, se interrumpe la cuenta, borrando el flag "firstKey", lo que resulta en que no se
    abra la ventana de configuración de la intensidad de luz. """
    def LuminariaLED_pressed(self):
        self.counter=0
        #self.luz_Btn.released.connect(self.LuminariaLED_released)
        print("Light Pressed")    
        self.firstKey = True
        #time.sleep(5)
        for n in range(25):
            if(not self.luz_Btn.isDown):
                self.firstKey=False
            if(not self.firstKey):
                break
            time.sleep(0.1)

        if(self.luz_Btn.isDown() and self.firstKey):
            print("Open config menu")
            #self.LuminariaLED_Window.show()
            self.firstKey=False
        else:
            print("No light menu because: Btn:" + str(self.luz_Btn.isDown()))
            print("Key is: " + str(self.firstKey))

    def LuminariaLED_released(self):
        self.counter+=1
        self.firstKey=False
        print("Light released: " + str(self.counter))

    def Upload(self):
        #fbUpload.upload()
        self.counter += 1
        self.label.setText(str(counter))

    def Decrease(self):
        self.counter -= 1
        self.label.setText(str(counter))

    def Config(self):
        self.configWindow.show()
        pass

    def Dial(self):
        slider= self.horizontalSlider.value()
        self.label_2.setText(str(slider) + " %")
        stopValue= (slider)/100
    #       print("Slider value= " + str(stopValue))
        gradient = stopValue-0.05
        if(gradient < 0):
            gradient = 0
            stopValue = 0.05
        if(stopValue>1):
            stopValue=1
        if(gradient>1):
            gradient=1
                
        if(stopValue < 0.15 or stopValue > 0.85 ):
            color= (255, 0, 0, 145)
        elif(stopValue < 0.4 or stopValue > 0.6):
            color=(255,197,0,145)
        else:
            color=(51, 255, 151, 145)
        style=u"QFrame{\n"
        style += "	\n"
        style += "	border-radius: 138px;\n"
        style += "   background-image: url();\n"
        style += "	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:" 
        style += str(stopValue) + " rgba(255, 255, 255, 0), stop:" + str(gradient) + " rgba" + str(color) + ");\n"
        style += "}"
    #        print(style)
        self.Bar.setStyleSheet(style)

    def Dial2(self):
        slider= self.horizontalSlider_2.value()
        self.label_3.setText(str(slider) + " %")
        stopValue= (slider)/100
#        print("Slider value= " + str(stopValue))
        gradient = stopValue-0.05
        if(gradient < 0):
            gradient = 0
            stopValue = 0.05
        if(stopValue>1):
            stopValue=1
        if(gradient>1):
            gradient=1
            
        if(stopValue < 0.15 or stopValue > 0.85 ):
            color=(255, 0, 0, 145)
        elif(stopValue < 0.4 or stopValue > 0.6):
            color=(255,197,0,145)
        else:
            color=(51, 255, 151, 145)

        style=u"QFrame{\n"
        style += "	\n"
        style += "	border-radius: 138px;\n"
        style += "   background-image: url();\n"
        style += "	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:" 
        style += str(stopValue) + " rgba(255, 255, 255, 0), stop:" + str(gradient) + " rgba" + str(color) + ");\n"
        style += "}"
        self.Bar_2.setStyleSheet(style)

