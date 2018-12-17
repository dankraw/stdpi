import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

id = 17
id2 = 27
GPIO.setup(id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(id2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file_path = "/tmp/file"
cmd = "DEPLOY HERMES!!!\n"

def pressCb(param):
	print "button %s pressed" % (param)
	f = open(file_path, "a")
	f.write(cmd)
	f.close()

GPIO.add_event_detect(id, GPIO.RISING, bouncetime=1300)
GPIO.add_event_callback(id, pressCb)

GPIO.add_event_detect(id2, GPIO.RISING, bouncetime=1300)
GPIO.add_event_callback(id2, pressCb)

while True:
	time.sleep(0.3) 
	print "alive"





