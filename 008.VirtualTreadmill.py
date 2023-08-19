# *_* coding： UTF-8 *_*
# 开发团队：DATA SUMMER LLC
# 网站：http://datasummer.net/
#      http://cuppett.atwebpages.com/
#   VirtualTreadmill.py


import time
import sys
leave=0                                      
print ("==========virtual treadmill=========")
print (30 *"#")
weight=float(input("Enter your weight（kg）："))    # The input weight can be a float                  
speed=float(input("Speed (km/h)："))                #The speed of the input can be a float
times=int(input("Running time (minutes)："))         # The running time entered is an integer in minutes
times=times*60                                            # convert minutes to seconds
while leave<times :                                       # convert minutes to seconds
    leave+=1   
    min, sec = divmod(times-leave,60)                     # Convert seconds to minutes and seconds
    leave_time=str(min)+'Minuutes'+str(sec)+'Second' 
    dista=leave/3600 * speed                              # Calculate running distance
    calor =weight * 30/(400/(speed*1000/60)) * leave/60/60    # Calculate calories
    sys.stdout.write('\r')
    sys.stdout.write('time left:{}  running distance:{:.2f}km  burn calories:{:.2f} kcal'.format(leave_time,dista,calor))
    sys.stdout.flush
    time.sleep(1)
