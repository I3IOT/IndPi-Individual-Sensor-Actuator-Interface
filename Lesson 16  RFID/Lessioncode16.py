'''
#This code To Write with RFID

import RPi.GPIO as GPIO 
import SimpleMFRC522 
reader = SimpleMFRC522.SimpleMFRC522() 
try: 
        text = raw_input('New data:') 
        print("Now place your tag to write") 
        reader.write(text) 
        print("Written") 
finally: 
        GPIO.cleanup() 
'''

'''
# This code To Read with RFID
 #!/usr/bin/env python 
import RPi.GPIO as GPIO 
import SimpleMFRC522 
reader = SimpleMFRC522.SimpleMFRC522() 
try: 
        id, text = reader.read() 
        print(id) 
        print(text) 
finally: 
        GPIO.cleanup() 
'''
