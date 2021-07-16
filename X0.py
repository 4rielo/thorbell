###############################################################################
import OPi.GPIO as OPiGPIO
from pyA20.gpio import gpio             #Para PWM por software en PA6 (pin 7)    
from pyA20.gpio import port
from orangepwm import *

class x0int:
    def __init__(self):
        OPiGPIO.setmode(OPiGPIO.BOARD)
        OPiGPIO.setup(15,OPiGPIO.IN)
        OPiGPIO.add_event_detect(15,OPiGPIO.FALLING, callback=self.x0CallBack)
        #OPiGPIO.setup(13,OPiGPIO.OUT)
        self.pwm = OrangePwm(100, port.PA0)          #100Hz en PA6
        self.state = True

    def x0CallBack(self):
        if(self.state):
            self.pwm.start(0)
            self.pwm.changeDutyCycle(50)
            self.state=False
        else:
            self.pwm.stop()
            self.state=True


    