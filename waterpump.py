import RPi.GPIO as GPIO
import time
 

RELAY_PIN = 27
sleep_timer = 5 #in seconds 


GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.HIGH)

def relay_on():
        GPIO.output(RELAY_PIN, GPIO.LOW)
        print("Water Pump ON")

def relay_off():
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        print("Water Pump OFF")
