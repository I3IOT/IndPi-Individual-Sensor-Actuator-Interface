
'''
#PRINT Hello World

from RPLCD import CharLCD 
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12]) 
lcd.write_string(u'Hello world!') '''

'''
#LINE BREAKS
from RPLCD import CharLCD 
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12]) 
lcd.write_string(u'Hello\n\rworld!') '''

'''
#CLEAR THE SCREEN

import time 
from RPLCD import CharLCD 
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12]) 
lcd.write_string(u'Hello world!') 
time.sleep(2) 
lcd.clear()'''
