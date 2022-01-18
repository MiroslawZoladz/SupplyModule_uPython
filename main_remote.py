HELP = "v/c: Set set up current electrical parameter\n"\
            "ch : set up current channel\n"\
            "s : set up value of c/v (returns err if is the same)\n"\
            "m : measurement\n"\
            "l : callibration\n"\
            "a : archive settings \n"\
            "r : read register\n"\
            "f : read coefficient\n"\
            "g : [brng/pg/badc] config device\n"

import machine
import time
from board import Board

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.SoftI2C(sda=sda, scl=scl, freq=100000)

board = Board(i2c)

while True:
    
    command = input("Give command:")
    
    tokens = command.split()
    
    if tokens[0] == 'ch':
        board.set_channel(int(tokens[1]))
    elif tokens[0] == 'v':
        board.set_param(tokens[0])
    elif tokens[0] == 'c':
        board.set_param(tokens[0])
    elif tokens[0] == 's':
        board.set(int(tokens[1]))
    elif tokens[0] == 'm':
        val = board.measure()
        if val>10000:
            val  = 0
        print(val)
    elif tokens[0] == 'l':
        board.callib(int(tokens[1]))
    elif tokens[0] == 'g':
        board.config(tokens[1], int(tokens[2]))
    elif tokens[0] == 'f':
        print(board.coeff())
    elif tokens[0] == 'r':
        print(board.raw())
    elif tokens[0] == 'a':
        board.save()
    else:
        print(HELP)
        
        
    