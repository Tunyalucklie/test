#test in mac without color detection from camera
import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem11301', 115200, timeout=10) #gonna check port later
time.sleep(1)

while True:
    color = input('Put the color ')
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
    
    