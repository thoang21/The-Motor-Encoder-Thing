import rotaryio
import board
import time

encoder = rotaryio.IncrementalEncoder(board.D0, board.D1)
last_position = 0
initialTime = time.monotonic() -0.1
TIC_PER_ROTATION = 256

loopCount = 0
rpm = 0

lst = []

while True:
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
        print(average_rpm)

    loopCount += 1



