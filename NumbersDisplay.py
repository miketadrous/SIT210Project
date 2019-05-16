
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

SDI   = 17
RCLK  = 4
SRCLK = 27

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

GPIO.setup(SDI, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.output(SDI, GPIO.LOW)
GPIO.output(RCLK, GPIO.LOW)
GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):
        for bit in range(0, 8): 
                GPIO.output(SDI, 0x80 & (dat << bit))
                GPIO.output(SRCLK, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(RCLK, GPIO.LOW)


def PrintZero():
        hc595_shift(segCode[0])
        time.sleep(0.5)

def PrintOne():
        hc595_shift(segCode[1])
        time.sleep(0.5)

def PrintTwo():
        hc595_shift(segCode[2])
        time.sleep(0.5)

def PrintThree():
        hc595_shift(segCode[3])
        time.sleep(0.5)

def PrintFour():
        hc595_shift(segCode[4])
        time.sleep(0.5)

def PrintFive():
        hc595_shift(segCode[5])
        time.sleep(0.5)
        
def PrintEmpty():
        hc595_shift(segCode[16])
        time.sleep(0.5)

def ShowAvailable(number):
        if (number==1):
                PrintOne()
        if (number==2):
                PrintTwo()
        if (number==3):
                PrintThree()
        if (number==4):
                PrintFour()
        if (number==5):
                PrintFive()
        if (number==0):
                PrintZero()

                
                
        
