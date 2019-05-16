#!/usr/bin/env python
import threading
import RPi.GPIO as GPIO
import time

import Entry
import Exit
import NumbersDisplay
import Parking
import LCDi2CLibrary
import BlynkControl

GPIO.setwarnings(False)



if __name__ == '__main__': #Program starting from here 

    try:
     
        t1 = threading.Thread(target=Parking.slot1, args=())
        t2 = threading.Thread(target=Parking.slot2, args=())
        t3 = threading.Thread(target=Parking.slot3, args=())
        t4 = threading.Thread(target=Parking.slot4, args=())
        t5 = threading.Thread(target=Parking.slot5, args=())
        t5 = threading.Thread(target=Parking.slot5, args=())

        Parking.updateDisplayNumber()

        t6 = threading.Thread(target=Exit.StartExitModule, args=())
        t7 = threading.Thread(target=Entry.StartEntryModule, args=())

        t8 = threading.Thread(target=LCDi2CLibrary.RefreshScreen, args=())
        t9 = threading.Thread(target=Parking.sendData, args=())
        t10 = threading.Thread(target=BlynkControl.AppControl, args=())
 
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()     
        t9.start()
        t10.start()
       






        
    except KeyboardInterrupt:
        GPIO.cleanup()
