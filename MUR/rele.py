import pymurapi as mur
from time import sleep
auv = mur.mur_init()

def keep_depth(value):
    error = auv.get_depth() - value
    
    power_2 = 0
    power_3 = 0
    power_value = 100
   
    if error > 0:
        power_2 = power_value
        power_3 = power_value
        
    if error < 0:
        power_2 = -power_value
        power_3 = -power_value
        
    if abs(error) < 0.1:
        power_2 = 0
        power_3 = 0
      
    auv.set_motor_power(2, power_2)
    auv.set_motor_power(3, power_3)
    return error
    
    
    
while True:
    error=keep_depth(2)
    sleep(0.02)
    print(error)
    sleep(0.2)
    print(f'depth = {auv.get_depth()}')
