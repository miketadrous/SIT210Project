import smbus
import time

bus = smbus.SMBus(1)

# This is the Particle Photon address we need to talk to
address = 0x05

def writeData(value):
    bus.write_i2c_block_data(address,0x01,value)
    time.sleep(1)
    return -1

def readData():
    number = bus.read_byte(address)
    return number
 
