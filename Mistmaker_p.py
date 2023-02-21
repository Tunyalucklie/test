#On Jetson Nano 
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=10) #gonna check port later
time.sleep(1)

while True:
    color = input('put the color ')
    if color == 'Red' :
            arduino.write(b'Red')
    
    if color == 'Orange' :
            arduino.write(b'Orange')
  
    if color == 'Blue' :
            arduino.write(b'Blue')
    
    if color == 'Green' :
            arduino.write(b'Green')
    
    if color == 'Violet' :
            arduino.write(b'Violet')