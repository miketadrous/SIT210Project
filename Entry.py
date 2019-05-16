import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

EntryGate =26
EntrySensor=22

GPIO.setup(EntryGate,GPIO.OUT)

GPIO.setup(EntrySensor, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def closeGate():

    p=GPIO.PWM(EntryGate,50)
    p.start(0)

    p.ChangeDutyCycle(12.8)
    time.sleep(1)
    p.ChangeDutyCycle(8.9)
    time.sleep(1)
    p.stop()


def openGate():

    p=GPIO.PWM(EntryGate,50)
    p.start(0)

    p.ChangeDutyCycle(8.9)
    time.sleep(1)
    p.ChangeDutyCycle(12.8)
    time.sleep(1)
    p.stop()

def StartEntryModule():
    gatestate="close"
    while True:
       if((GPIO.input(EntrySensor) ==0) & (gatestate=="close")):
           print("Beam Broken")
           openGate()
           gatestate="open"
       if((GPIO.input(EntrySensor) == 1) & (gatestate=="open")):
           print("Solid")
           closeGate()
           gatestate="close"

