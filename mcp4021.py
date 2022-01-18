from machine import Pin
from nonvolatile_float import nonvolatile_float

class MCP4021:
    
    __PIN_UD = 14
    
    def __init__(self, pin_cs):
        self._state = 0
        self._nonvolatile_state = nonvolatile_float()        
        self._ud_pin = Pin(self.__PIN_UD, Pin.OUT, Pin.PULL_UP, value = False)
        self._cs_pin = Pin(pin_cs, Pin.OUT, Pin.PULL_UP, value = False)
        
        self.set(self._nonvolatile_state.get())
        
    def UD(self, val):
        GPIO.output(self.__PIN_UD, val)
        
    def CS(self, val):
        GPIO.output(self._pin_cs, val)
        
    def dec(self, step_nr):
        self._cs_pin.on()
        self._ud_pin.on()
        self._cs_pin.off()
        for i in range(step_nr):
            self._ud_pin.off()
            self._ud_pin.on()
            if (self._state>0):
                self._state -= 1
        self._cs_pin.on()
        self._nonvolatile_state.set(self._state)
        
    def inc(self, step_nr):
        self._cs_pin.on()
        self._ud_pin.off()
        self._cs_pin.off()
        for i in range(step_nr):
            self._ud_pin.off()
            self._ud_pin.on()
            if (self._state<63):
                self._state += 1
        self._cs_pin.on()
        self._nonvolatile_state.set(self._state)
        
    def set(self, val):
        self.dec(64)
        self.inc(val)
        
    def save(self):
        self._nonvolatile_state.save()
            
        