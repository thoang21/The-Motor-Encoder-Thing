import rotaryio
import board
import time

import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A4, frequency=50)

# Create a servo object, my_servo.
myServo = servo.ContinuousServo(pwm)

MinInput = 0
MaxInput = 10000
MinThrottle = 0
MaxThrottle = 0.4


# For the LCD
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2
lcd_address = 0x27 #The i2c address for the LCD backpack in the IDEA center

# Initialise I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the lcd class
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, False, True, lcd_address)


# For the encoder
encoder = rotaryio.IncrementalEncoder(board.D2, board.D3)
last_position = 0
initialTime = time.monotonic() -0.1
TIC_PER_ROTATION = 20

loopCount = 0
rpm = 0

lst = []

def mathMap(input,minInput,maxInput,minOutput,maxOutput):
    return (input - minInput)*(maxOutput - minOutput)/(maxInput - minInput) + minOutput

setpoint = 3000
myServo.throttle = mathMap(setpoint, MinInput, MaxInput, MinThrottle, MaxThrottle)
TOLERANCE = 100
kP = 20000
change = 0.005

while True:
    lcd.backlight = True

    position = encoder.position
    currentTime = time.monotonic()
    if currentTime != initialTime:
        rpm = ((position - last_position) / (currentTime - initialTime)) * 60 / TIC_PER_ROTATION                   # / 4
        time.sleep(0.02)
        # print(currentTime - initialTime)

    last_position = position
    initialTime = currentTime
    lst.append(rpm)

    if loopCount == 50:
        yay = int((sum(lst) / len(lst)))
        average_rpm = yay #yay * 3.28
        print(average_rpm)
        loopCount = 0
        lst = []

        error = setpoint - average_rpm
        change = error / kP

        if average_rpm < setpoint + TOLERANCE and average_rpm > setpoint - TOLERANCE:
            myServo.throttle = myServo.throttle
        else:
            myServo.throttle += change

        # Print a two line message
        lcd.clear()
        value = str(average_rpm)
        lcd.message = value

    loopCount += 1
