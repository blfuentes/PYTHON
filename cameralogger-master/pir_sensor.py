import RPi.GPIO as GPIO
import os
import datetime
import time
import csv
import picamera
import display

GPIO.setmode(GPIO.BCM)

display.initDisplay()
        
sensor = 4

GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

camera = picamera.PiCamera()

filepath = "/var/www/html/sensor/log.csv"
mode = 'a' if os.path.exists(filepath) else 'w'
fieldnames = ['date', 'value']
with open(filepath, mode) as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if mode == 'w':
        writer.writeheader()
        mode = 'a'

numHIGH = 0
try:
    while True:
        time.sleep(0.1)
        previous_state = current_state
        current_state = GPIO.input(sensor)
        if current_state != previous_state:
            new_state = "HIGH" if current_state else "LOW"
            with open(filepath, mode) as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                print("GPIO pin %s is %s" % (sensor, new_state))
                event = datetime.datetime.now()
                if new_state == "HIGH":
                    numHIGH = numHIGH+1
                    if numHIGH == 10:
                        numHIGH = 0
                    display.displayNumber(numHIGH)
                    camera.capture('/var/www/html/sensor/images/'+str(event)+'.jpg')
                writer.writerow({'date': event, 'value': new_state})
finally:
    GPIO.cleanup()
