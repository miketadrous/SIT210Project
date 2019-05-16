#!/usr/bin/env python
import threading
import RPi.GPIO as GPIO
import time

import NumbersDisplay

import Rasp_i2c_Photon

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)


Slot1=6
Slot2=20
Slot3=16
Slot4=12
Slot5=21

Slot1Green=9
Slot1Red=11
Slot2Green=5
Slot2Red=13
Slot3Green=8
Slot3Red=25
Slot4Green=15
Slot4Red=7
Slot5Green=24
Slot5Red=18


Slot1State=0
Slot2State=0
Slot3State=0
Slot4State=0
Slot5State=0

Slots=5
ParkedCars=0

           
GPIO.setup(Slot1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Slot2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Slot3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Slot4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Slot5, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(Slot1Green,GPIO.OUT)
GPIO.setup(Slot1Red,GPIO.OUT)
GPIO.setup(Slot2Green,GPIO.OUT)
GPIO.setup(Slot2Red,GPIO.OUT)
GPIO.setup(Slot3Green,GPIO.OUT)
GPIO.setup(Slot3Red,GPIO.OUT)
GPIO.setup(Slot4Green,GPIO.OUT)
GPIO.setup(Slot4Red,GPIO.OUT)
GPIO.setup(Slot5Green,GPIO.OUT)
GPIO.setup(Slot5Red,GPIO.OUT)

def parkedCarsCalculation():
    global Slot1State
    global Slot2State
    global Slot3State
    global Slot4State
    global Slot5State
    global ParkedCars

    ParkedCars=Slot1State+Slot2State+Slot3State+Slot4State+Slot5State

    print (ParkedCars)

def updateDisplayNumber():
    global Slots
    global ParkedCars
    NumbersDisplay.ShowAvailable(Slots-ParkedCars)
    
def slot1():
    global Slot1State
    while True:
        if ((GPIO.input(Slot1)== 0) & (Slot1State==0)):
            Slot1State=1
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot1Green,GPIO.LOW)
            GPIO.output(Slot1Red,GPIO.HIGH)
            time.sleep(1)
            print ("Park1 Occupied!")
        if ((GPIO.input(Slot1)== 1) & (Slot1State==1)):
            Slot1State=0
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot1Green,GPIO.HIGH)
            GPIO.output(Slot1Red,GPIO.LOW)
            time.sleep(1)
            print ("Park1 empty!")

def slot2():
    global Slot2State
    while True:
        if ((GPIO.input(Slot2)== 0) & (Slot2State==0)):
            Slot2State=1
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot2Green,GPIO.LOW)
            GPIO.output(Slot2Red,GPIO.HIGH)
            time.sleep(1)
            print ("Park2 Occupied!")
        if ((GPIO.input(Slot2)== 1) & (Slot2State==1)):
            Slot2State=0
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot2Green,GPIO.HIGH)
            GPIO.output(Slot2Red,GPIO.LOW)
            time.sleep(1)
            print ("Park2 empty!")

def slot3():
    global Slot3State
    while True:
        if ((GPIO.input(Slot3)== 0) & (Slot3State==0)):
            Slot3State=1
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot3Green,GPIO.LOW)
            GPIO.output(Slot3Red,GPIO.HIGH)
            time.sleep(1)
            print ("Park3 Occupied!")
        if ((GPIO.input(Slot3)== 1) & (Slot3State==1)):
            Slot3State=0
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot3Green,GPIO.HIGH)
            GPIO.output(Slot3Red,GPIO.LOW)
            time.sleep(1)
            print ("Park3 empty!")

def slot4():
    global Slot4State
    while True:
        if ((GPIO.input(Slot4)== 0) & (Slot4State==0)):
            Slot4State=1
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot4Green,GPIO.LOW)
            GPIO.output(Slot4Red,GPIO.HIGH)
            time.sleep(1)
            print ("Park4 Occupied!")
        if ((GPIO.input(Slot4)== 1) & (Slot4State==1)):
            Slot4State=0
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot4Green,GPIO.HIGH)
            GPIO.output(Slot4Red,GPIO.LOW)
            time.sleep(1)
            print ("Park4 empty!")

def slot5():
    global Slot5State
    while True:
        if ((GPIO.input(Slot5)== 0) & (Slot5State==0)):
            Slot5State=1
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot5Green,GPIO.LOW)
            GPIO.output(Slot5Red,GPIO.HIGH)
            time.sleep(1)
            print ("Park5 Occupied!")
        if ((GPIO.input(Slot5)== 1) & (Slot5State==1)):
            Slot5State=0
            parkedCarsCalculation()
            updateDisplayNumber()
            GPIO.output(Slot5Green,GPIO.HIGH)
            GPIO.output(Slot5Red,GPIO.LOW)
            time.sleep(1)
            print ("Park5 empty!")
            
def sendData():
    global Slot1State
    global Slot2State
    global Slot3State
    global Slot4State
    global Slot5State

    while True:

        data =[]
        data.append(Slot1State)
        data.append(Slot2State)
        data.append(Slot3State)
        data.append(Slot4State)
        data.append(Slot5State)
    
        Rasp_i2c_Photon.writeData(data)

