import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library 
from time import sleep # Import the sleep function from the time module 
GPIO.setwarnings(False) # Ignore warning for now 
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set ini
tial value to low (off) 
while True: # Run forever 
 GPIO.output(8, GPIO.HIGH) # Turn on 
 sleep(1) # Sleep for 1 second 
 print(‘LED ON’) 
 GPIO.output(8, GPIO.LOW) # Turn off 
 sleep(1) # Sleep for 1 second 
 print(‘LED OFF’)
