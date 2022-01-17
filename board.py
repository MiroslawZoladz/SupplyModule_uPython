from MCP4021 import MCP4021
from INA219 import INA219_Voltage, INA219_Current

class channel:
    def __init__(self, pot, meters):
        self.pot = pot
        self.meters = meters
        
class Board:
    
    __MAX_CHANNEL_NR = 5
    
    __channel_cs_numbers = [18, 22, 28, 27, 26]
    __channel_addresses = [0x44, 0x43, 0x42, 0x41, 0x40]
        
    def __init__(self, i2c):
        
        self.channels = []
        for channel_cs_nr, channel_addr in zip(self.__channel_cs_numbers, self.__channel_addresses):
            p = MCP4021(channel_cs_nr)
            m = {'c':INA219_Current(i2c, channel_addr), 'v':INA219_Voltage(i2c, channel_addr)}
            self.channels.append(channel(pot = p, meters = m))
        
        self.channel = 0
        self.param = 'c'
        
    def set(self, value):
        self.channels[self._channel].pot.set(value)
    def inc(self):
        self.channels[self._channel].pot.inc(1)
    def dec(self):
        self.channels[self._channel].pot.dec(1)
    def save(self):
        delf.channels[self._channel].pot.save()
    def measure(self):
        self.channels[self._channel].meters[self._param].measure()
    def callib(self, value):
        self.channels[self._channel].meters[self._param].callib(value)
    def config(self, name, value):
        self.channels[self._channel].meters[self._param].config(name, value)
    def coeff(self):
        self.channels[self._channel].meters[self._param].read_coefficient()
    def raw(self):
        self.channels[self._channel].meters[self._param].measure_raw()
        