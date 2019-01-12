import serial
from drawnow import *
import numpy as np
import matplotlib.pyplot as plt

readings=[]
plt.ion() #for Plotting live data from the gas sensor

ser = serial.Serial('/dev/tty.usbserial', 9600)
#ser=serial.Serial('com1l',9600) #Serial Objects

def createFigure():
    plt.plot(readings,'ro--')
    plt.ylabel('Hydrogen gas Readings')
    plt.show()

while True:
    while(ser.inWaiting()==0):
        pass
    data=ser.readline().decode().strip()
    dataArray=data.split(',')
    temp=float(dataArray[0])
    #   print(dat)
    readings.append(temp)
    drawnow(createFigure)
    plt.pause(.0001)
