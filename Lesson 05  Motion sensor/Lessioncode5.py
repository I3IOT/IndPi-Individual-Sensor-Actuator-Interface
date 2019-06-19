import RPi.GPIO as GPIO 
import time 
sensor = 8 
led = 10 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(sensor,GPIO.IN) 
GPIO.setup(led,GPIO.OUT) 
GPIO.output(led,False) 
print "Initializing PIR Sensor......" 
time.sleep(12) 
print "PIR Ready..." 
print " " 
try:  
   while True: 
      if GPIO.input(sensor): 
          GPIO.output(led,True) 
          print "Motion Detected" 
          while GPIO.input(sensor): 
              time.sleep(0.2) 
      else: 
          GPIO.output(led,False) 
except KeyboardInterrupt: 
    GPIO.cleanup() 
