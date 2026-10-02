import serial
import time

ser = serial.Serial('COM10', 9600)
while True:
    data = ser.readline()
    data = data.decode()
    data = data.strip()
    print(data)


print(data)
#Temeperature in Fahreignheit(Omor)
TEMP_READING = 23  

#Humidity in kg/m^3
HUMIDITY = 0.234

#Pressure in Pascal
PRESSURE = 0.2


CLIENT_COMMENT = "The device calculations is accurate, but better changesneed to be made"