import os
import time

 
def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")
 




while True:
    temp = temperature_of_raspberry_pi()
    print(temp)
    nTemp = temp[0] +temp[1] + temp[2] + temp[3]
    
    #if float(nTemp) >= 44:
      
    
    time.sleep(1)