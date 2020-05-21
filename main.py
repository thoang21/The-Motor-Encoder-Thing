import rotaryio
import board
import time

encoder = rotaryio.IncrementalEncoder(board.D0, board.D1)
last_position = None
initialTime = time.monotonic()[
TIC_PER_ROTATION = 256


while True:
    position = encoder.position
    currentTime = time.monotonic() - initialTime
    print((currentTime,position))

    #if last_position is None or position != last_position:
        #print(position)
    last_position = position
