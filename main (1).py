import rotaryio
import board
import time

# For the LCD
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2
lcd_address = 0x27 #The i2c address for the LCD backpack in the IDEA center

# Initialise I2C bus.
# i2c = busio.I2C(board.SCL, board.SDA)

# Initialise the lcd class
# lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, False, True, lcd_address)


# For the encoder
encoder = rotaryio.IncrementalEncoder(board.D0, board.D1)
last_position = 0
initialTime = time.monotonic() -0.1
TIC_PER_ROTATION = 256

loopCount = 0
rpm = 0

lst = []

while True:
    # lcd.backlight = True
    
    position = encoder.position
    currentTime = time.monotonic()
    if currentTime != initialTime:
        rpm = ((position - last_position) / (currentTime - initialTime)) * 60 / TIC_PER_ROTATION / 4

    last_position = position
    initialTime = currentTime
    lst.append(rpm)

    if loopCount == 200:
        loopCount = 0
        lst = []
        average_rpm = sum(lst) / len(lst)
        
        # Print a two line message
        # lcd.clear()
        # value = str(average_rpm)
        # lcd.message = value
        
        print(average_rpm)

    loopCount += 1





