import urllib
import RPi.GPIO as GPIO
import time
import json
GPIO.setmode(GPIO.BCM)
sw1 = 5
sw2 = 6
sw3 = 13
sw4 = 19

load1_on = 18
load2_on = 23
load3_on = 24
load4_on = 25

#GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

GPIO.setup(sw1,GPIO.IN)



while True:
 
  url = "http://121.200.50.200:9114/service.svc/DoWork?str=2"
# url = "http://www.google.com"
  response = urllib.urlopen(url).read()
 # print response
 # j=json.loads(response)
  #print response
#  print j['DoWorkResult']
  load1= response[26:29]
  load2= response[30:33]
  load3= response[34:37]
  load4= response[38:41]
  print (load1+load2+load3+load4)
  
  if load1 == 'L11':
    GPIO.output(18,GPIO.HIGH)
    load1_current_stutas=1;
  if load1 == 'L10':
    GPIO.output(18,GPIO.LOW)
    load1_current_stutas=0;
  if load2 == 'L21':
    GPIO.output(23,GPIO.HIGH)
  else:
    GPIO.output(23,GPIO.LOW)
  if load3 == 'L31':
    GPIO.output(24,GPIO.HIGH)
  else:
    GPIO.output(24,GPIO.LOW)
  if load4 == 'L41':
    GPIO.output(25,GPIO.HIGH)
  else:
    GPIO.output(25,GPIO.LOW) 
  
 
 

##  if GPIO.input(sw1):
#   if load1_current_stutas==1:
#       GPIO.output(load1,GPIO.LOW)
#       time.sleep(1)
#        urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L1&st=0")
#   else:
#       GPIO.output(load1,GPIO.HIGH)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L1&st=1")
# if GPIO.input(sw2):
#   if load1_current_stutas==1:
#       GPIO.output(load2,GPIO.LOW)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=0")
#   else:
#      GPIO.output(load2,GPIO.HIGH)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=1")
   
# if GPIO.input(sw3):
#   if load1_current_stutas==1:
#       GPIO.output(load3,GPIO.LOW)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=0")
#    else:
#      GPIO.output(load3,GPIO.HIGH)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=1")
#  if GPIO.input(sw4):
#   if load1_current_stutas==1:
#       GPIO.output(load4,GPIO.LOW)
#       time.sleep(1)
#       urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=0")
#   else:
#       GPIO.output(load4,GPIO.HIGH)
#        time.sleep(1)
#        urllib.urlopen("http://121.200.50.200:9114/service.svc/LoadStatus?lo=L2&st=1")
  
      


 # GPIO.output(18,GPIO.HIGH)
  #GPIO.output(23,GPIO.HIGH)
  #GPIO.output(24,GPIO.HIGH)
  #GPIO.output(25,GPIO.HIGH)
 # time.sleep(1)
 # print "LED off"
 # GPIO.output(18,GPIO.LOW)
 # GPIO.output(23,GPIO.LOW)
 # GPIO.output(24,GPIO.LOW)
 # GPIO.output(25,GPIO.LOW)

  

