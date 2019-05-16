import BlynkLib
import time
import Parking
import Entry
import Exit
import RPi.GPIO as GPIO

# Initialize Blynk
blynk = BlynkLib.Blynk('735a98e9209d460891cf9312a3204a1e')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(6)
def my_write_handler(value):
    if (value==['1']):
        Entry.openGate()
    if (value==['0']):
        Entry.closeGate()

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(7)
def my_write_handler(value):
    if (value==['1']):
        Exit.openGate()
    if (value==['0']):
        Exit.closeGate()


# Register Virtual Pins
@blynk.VIRTUAL_WRITE(11)
def my_write_handler(value):
    if (value==['1']):
        GPIO.output(Parking.Slot1Green,GPIO.LOW)
        GPIO.output(Parking.Slot1Red,GPIO.HIGH)
    if (value==['0']):
        GPIO.output(Parking.Slot1Green,GPIO.HIGH)
        GPIO.output(Parking.Slot1Red,GPIO.LOW)


# Register Virtual Pins
@blynk.VIRTUAL_WRITE(12)
def my_write_handler(value):
    if (value==['1']):
        GPIO.output(Parking.Slot2Green,GPIO.LOW)
        GPIO.output(Parking.Slot2Red,GPIO.HIGH)
    if (value==['0']):
        GPIO.output(Parking.Slot2Green,GPIO.HIGH)
        GPIO.output(Parking.Slot2Red,GPIO.LOW)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(13)
def my_write_handler(value):
    if (value==['1']):
        GPIO.output(Parking.Slot3Green,GPIO.LOW)
        GPIO.output(Parking.Slot3Red,GPIO.HIGH)
    if (value==['0']):
        GPIO.output(Parking.Slot3Green,GPIO.HIGH)
        GPIO.output(Parking.Slot3Red,GPIO.LOW)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(14)
def my_write_handler(value):
    if (value==['1']):
        GPIO.output(Parking.Slot4Green,GPIO.LOW)
        GPIO.output(Parking.Slot4Red,GPIO.HIGH)
    if (value==['0']):
        GPIO.output(Parking.Slot4Green,GPIO.HIGH)
        GPIO.output(Parking.Slot4Red,GPIO.LOW)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(15)
def my_write_handler(value):
    if (value==['1']):
        GPIO.output(Parking.Slot5Green,GPIO.LOW)
        GPIO.output(Parking.Slot5Red,GPIO.HIGH)
    if (value==['0']):
        GPIO.output(Parking.Slot5Green,GPIO.HIGH)
        GPIO.output(Parking.Slot5Red,GPIO.LOW)
    

@blynk.VIRTUAL_READ(1)
def my_read_handler():    
    if(Parking.Slot1State==1):
        blynk.virtual_write(1,255)
    else:
        blynk.virtual_write(1,0)
        
@blynk.VIRTUAL_READ(2)
def my_read_handler():        
    if(Parking.Slot2State==1):
        blynk.virtual_write(2,255)
    else:
        blynk.virtual_write(2,0)
        
@blynk.VIRTUAL_READ(3)
def my_read_handler():
    if(Parking.Slot3State==1):
        blynk.virtual_write(3,255)
    else:
        blynk.virtual_write(3,0)

@blynk.VIRTUAL_READ(4)
def my_read_handler():
    if(Parking.Slot4State==1):
        blynk.virtual_write(4,255)
    else:
        blynk.virtual_write(4,0)
        
@blynk.VIRTUAL_READ(5)
def my_read_handler():
    if(Parking.Slot5State==1):
        blynk.virtual_write(5,255)
    else:
        blynk.virtual_write(5,0)
    


def AppControl():

    tmr_start_time = time.time()
    while True:
        blynk.run()
        my_read_handler()
        t = time.time()
        if t - tmr_start_time > 1:
            my_read_handler()
            tmr_start_time += 1



