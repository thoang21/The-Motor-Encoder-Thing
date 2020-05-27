# Continuous Servo Test Program for CircuitPython
import time
import board
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A4, frequency=50)

# Create a servo object, my_servo.
myServo = servo.ContinuousServo(pwm)

MAX_THROTTLE = 1.0
THROTTLE_CHANGE = 0.005

myServo.throttle = -MAX_THROTTLE

while True:
    if myServo.throttle >= 1:
        break
    myServo.throttle += THROTTLE_CHANGE
    print(myServo.throttle)
    time.sleep(0.05)
