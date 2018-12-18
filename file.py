import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

locked = True
bouncetime = 1500

chan_led = 14
chan_lock = 22

chan_evo = 23
chan_dev = 24
chan_test = 20
chan_prod = 25

buttons = {chan_evo: "evo", chan_dev: "dev", chan_test: "test", chan_prod: "prod"}

GPIO.setup(chan_led, GPIO.OUT)
GPIO.setup(chan_lock, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for (button, name) in buttons.items():
        print("setting {} {}".format(button, name))
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
	#if locked:
	#	return
	#lock()
	print "button %s pressed" % param
	if param not in buttons:
		print "error: unknown button %s" % param
		return
	filepath = file_path + buttons[param]
	f = open(filepath, "a")
	f.write(cmd)
	f.close()

def reset_pressed(param):
        print("trying to unlock")
	if not locked:
		return
	print "reset"
	unlock()

GPIO.add_event_detect(chan_lock, GPIO.RISING, bouncetime=bouncetime)
GPIO.add_event_callback(chan_lock, reset_pressed)

for (button, name) in buttons.items():
        print "button {} name {}".format(button, name)
	GPIO.add_event_detect(button, GPIO.RISING, bouncetime=bouncetime)
	GPIO.add_event_callback(button, button_pressed)

lock()

while True:
	time.sleep(1)
	pass # do nothing
