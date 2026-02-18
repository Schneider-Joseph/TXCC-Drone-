import RPi.GPIO as GPIO
import time

PWM_PIN = 17
Frequency = 5000
Duty_Cycle = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN, Frequency)

try:
    pwm.start(Duty_Cycle)
    print(f"PWM started on GPIO {PWM_PIN} at {Frequency} Hz with {Duty_Cycle}% duty cycle")
    time.sleep(10)



except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("PWM stopped and GPIO cleaned up.")
