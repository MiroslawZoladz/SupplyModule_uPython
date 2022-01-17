import machine
import time
from board import Board
from keyboard import keyboard

sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

My_Board = Board(i2c)
My_keyboard = keyboard()

while True:
    butt_read = My_keyboard.read():
    if butt_read == 'UP' and My_board.channel < 4:
        My_board.channel += 1
    elif butt_read == 'DOWN' and My_board.channel > 0:
        My_board.channel -= 1
    elif butt_read == 'RIGHT':
        My_board.inc()
    elif butt_read == 'LEFT':
        My_board.dec()
    elif butt_read == 'MIDDLE':
        My_board.save()
    else:
        pass
    
    My_board.param = 'v'
    voltage = My_board.measure()

    My_board.param = 'c'
    current = My_board.measure()

    if current > 10000:
        current = 0
        
    print(f"Channel: {My_board.channel}, Voltage: {voltage/1000}, Current: {Current/1000}")
        
    time.sleep(0.05)
        
        
            