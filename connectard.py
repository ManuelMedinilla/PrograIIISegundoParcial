import serial
import time

puerto = "COM5"
velocidad = 9600
ser = serial.Serial(puerto,velocidad,timeout=1)
time.sleep(2)

ser.write(b'Enciende el LED Arduino')
respuesta = ser.readline().decode('utf-8') 
print('LED encendido:', respuesta)

ser.close