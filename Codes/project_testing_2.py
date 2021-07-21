import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('com6',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print incoming
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:
        pyautogui.keyDown('left')

    if 'Forward' in incoming:
        pyautogui.keyDown('right')

    if 'Vup' in incoming:
        pyautogui.keyDown('down')
        

    if 'Vdown' in incoming:
       
        pyautogui.keyDown('up')

    incoming = "";
