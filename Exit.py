import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

EntryGate=19
EntrySensor=14

GPIO.setup(EntryGate,GPIO.OUT)

GPIO.setup(14, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def closeGate():

    p=GPIO.PWM(EntryGate,50)
    p.start(0)

    p.ChangeDutyCycle(8.9)
    time.sleep(1)
    p.ChangeDutyCycle(4)
    time.sleep(1)
    p.stop()


def openGate():

    p=GPIO.PWM(EntryGate,50)
    p.start(0)

    p.ChangeDutyCycle(4)
    time.sleep(1)
    p.ChangeDutyCycle(8.9)
    time.sleep(1)
    p.stop()

def StartExitModule():
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
