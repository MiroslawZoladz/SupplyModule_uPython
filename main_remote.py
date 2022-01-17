HELP = "c|v: Set set up current electrical parameter\n"\
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

sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

My_board = Board(i2c)

while True:
    
    command = input("Give command:")
    
    tokens = command.split()
    
    if tokens[0] == 'ch':
        My_board.channel = int(tokens[1])
    elif tokens[0] == 'v':
        My_board.param = 'v'
    elif tokens[0] == 'c':
        My_board.param = 'c'
    elif tokens[0] == 's':
        My_board.set(int(tokens[1]))
    elif tokens[0] == 'm':
        val = My_board.measure()
        if val>10000:
            val  = 0
        print(val)
    elif tokens[0] == 'l':
        My_board.callib(int(tokens[1]))
    elif tokens[0] == 'g':
        My_board.config(tokens[1], int(tokens[2]))
    elif tokens[0] == 'f':
        print(My_board.coeff())
    elif tokens[0] == 'r':
        print(My_board.raw())
    elif tokens[0] == 'a':
        My_board.save()
    else:
        print(HELP)
        
        
    