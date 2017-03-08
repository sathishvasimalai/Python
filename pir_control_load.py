
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
start=0
pir_flg=0
while True:
      

       i=GPIO.input(7)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             time.sleep(0.1)
             end = time.time()
             fps=int(round( end - start ))
             print(fps)


             if( fps >= 30 and pir_flg == 1):
                 GPIO.output(3, 0)  #Turn OFF LED
                 print "light off"
                 pir_flg=0

           
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             GPIO.output(3, 1)  #Turn ON LED
             time.sleep(0.1)
             pir_flg=1
             start = time.time()
             
