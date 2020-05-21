"""Simple test for 16x2 character lcd connected to an PCF8574 I2C LCD backpack. This is what we have in the IDEA center"""
import time
import board
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

while True:

    # Turn backlight on
    lcd.backlight = True
    # Print a two line message
    lcd.clear()
    lcd.message = "Hello\nCircuitPython"
    # Wait 2s
    time.sleep(2)
    lcd.clear()
    # Print two line message right to left
    lcd.text_direction = lcd.RIGHT_TO_LEFT
    lcd.message = "Hello\nCircuitPython"
    # Wait 2s
    time.sleep(2)
    # Return text direction to left to right
    lcd.text_direction = lcd.LEFT_TO_RIGHT
    # Display cursor
    lcd.clear()
    lcd.cursor = True
    lcd.message = "Cursor! "
    # Wait 2s
    time.sleep(2)
    # Display blinking cursor
    lcd.clear()
    lcd.blink = True
    lcd.message = "Blinky Cursor!"
    # Wait 2s
    time.sleep(2)
    lcd.blink = False
    lcd.clear()
    # Create message to scroll
    scroll_msg = "<-- Scroll"
    lcd.message = scroll_msg
    # Scroll message to the left
    for i in range(len(scroll_msg)):
        time.sleep(0.5)
        lcd.move_left()
    lcd.clear()
    lcd.message = "Going to sleep\nCya later!"
    time.sleep(2)
    # Turn backlight off
    lcd.backlight = False
    time.sleep(2)
    lcd.clear()
