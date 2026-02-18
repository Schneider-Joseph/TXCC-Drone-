from gpiozero import Servo
from time import sleep

# Define the GPIO pin connected to the servo's control wire
# Use the BCM (Broadcom SOC channel) numbering scheme
servo_pin_x = 17 
servo_pin_y = 18

# Create a Servo object
# The min_pulse_width and max_pulse_width might need adjustment for your specific servo
my_servo_x = Servo(servo_pin_x, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
my_servo_y = Servo(servo_pin_y, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

try:
    while True:
        # Move to the minimum position (x-axis) (e.g., 25 degrees)
        print("Moving x-axis to min position")
        my_servo_x.value = 0.00  # Value ranges from -1 (min) to 1 (max)
      
        
        # Move to the minimum position (y-axis) (e.g., 25 degrees)
        print("Moving y-axis to min position")
        my_servo_y.value = -1.00  # Value ranges from -1 (min) to 1 (max)
        
        sleep(2)

        # Move to the middle position (x-axis) (e.g., 25 degrees)
        print("Moving x-axis to mid position")
        my_servo_x.value = 0.00  # Value ranges from -1 (min) to 1 (max)
    
        
        # Move to the middle position (y-axis) (e.g., 25 degrees)
        print("Moving y-axis to mid position")
        my_servo_y.value = -0.30  # Value ranges from -1 (min) to 1 (max)
        
        sleep(2)

        # Move to the maximum position (x-axis) (e.g., 25 degrees)
        print("Moving x-axis to max position")
        my_servo_x.value = 0.00  # Value ranges from -1 (min) to 1 (max)

        sleep(2)
        
        # Move to the maximum position (y-axis) (e.g., 25 degrees)
        print("Moving y-axis to max position")
        my_servo_y.value = -1.00  # Value ranges from -1 (min) to 1 (max)
        
        sleep(2)

        # Set a specific angle (x-axis) (e.g., 25 degrees)
        print("Moving x-axis to 45 degrees")
        my_servo_x.value = 0  # Value ranges from -1 (min) to 1 (max)
