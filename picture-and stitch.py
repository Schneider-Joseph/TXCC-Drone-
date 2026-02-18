mport RPi.GPIO as GPIO
import time
import os
import subprocess
import sys
sys.path.insert(1, '/home/tunxis001/my_project/lib/python3.13/site-packages')
import cv2
import imutils
from imutils import paths
import glob

print("[INFO] Starting to take pictures")
print("Current working directory:", os.getcwd())

# --- Servo Motor Configuration ---
SERVO_PIN = 18 # Use a PWM capable pin like GPIO 18 (Pin 12)
GPIO.setmode(GPIO.BCM) # Use BCM numbering
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM for the servo at 50Hz frequency
# A frequency of 50Hz is standard for most hobby servos
pwm = GPIO.PWM(SERVO_PIN, 50) 
pwm.start(0) # Start PWM with 0% duty cycle (stopped)

# Function to set the servo angle (0 to 180 degrees)
def set_angle(angle):
    # Duty cycle calculation: (angle / 18) + 2
    # This maps 0 degrees to ~2% duty cycle, 90 deg to ~7%, and 180 deg to ~12%
    duty_cycle = (angle / 18.0) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5) # Give the servo time to move
    
# --- Camera Configuration ---
def take_photo(filename="webcam_image.jpg"):
    print(f"Taking photo and saving as {filename}...")
    # Command to run fswebcam
    # -r specifies resolution, --no-banner removes the timestamp banner
    command = f"fswebcam -r 1280x720 --no-banner {filename}"
