import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

chan_led = 18
chan1 = 17
chan_reset = 27
locked = True

GPIO.setup(chan_led, GPIO.OUT)
GPIO.setup(chan1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(chan_reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

file_path = "/tmp/file"
cmd = "DEPLOY HERMES!!!\n"

def lock():
	global locked
	locked = True
	GPIO.output(chan_led, GPIO.LOW)

def unlock():
	global locked
	locked = False
	GPIO.output(chan_led, GPIO.HIGH)

def button_pressed(param):
	if locked:
		return
	lock()
	print "button %s pressed" % param
	f = open(file_path, "a")
	f.write(cmd)
	f.close()

def reset_pressed(param):
	if not locked:
		return
	print "reset"
	unlock()

GPIO.add_event_detect(chan_reset, GPIO.RISING, bouncetime=1300)
GPIO.add_event_callback(chan_reset, reset_pressed)

GPIO.add_event_detect(chan1, GPIO.RISING, bouncetime=1300)
GPIO.add_event_callback(chan1, button_pressed)

lock()

while True:
	time.sleep(1)
	print ""





