import time 
from Adafruit_8x8 import ColorEightByEight 
grid = ColorEightByEight(address=0x70) 
iter = 0 
# Continually update the 8x8 display one pixel at a time 
while(True):   
 iter += 1 
 for x in range(0, 8):    
   for y in range(0, 8):    
      grid.setPixel(x, y, iter % 4 )   
         time.sleep(0.02
