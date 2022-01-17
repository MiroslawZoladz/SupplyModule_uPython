from nonvolatile_float import nonvolatile_float

class MCP4021:
    
    __PIN_UD = 14
    
    def __init__(self, pin_cs):
        self._pin_cs = pin_cs
        self._state = 0
        self._nonvolatile_state = nonvolatile_float()
        
        GPIO.setup(self.__PIN_UD, GPIO.OUT)
        GPIO.setup(self._pin_cs, GPIO.OUT)
        
        self.set(self._nonvolatile_state.get())
        
    def UD(self, val):
        GPIO.output(self.__PIN_UD, val)
        
    def CS(self, val):
        GPIO.output(self._pin_cs, val)
        
    def dec(self, step_nr):
        self.CS(GPIO.HIGH)
        self.UD(GPIO.HIGH)
        self.CS(GPIO.LOW)
        for i in range(step_nr):
            self.UD(GPIO.LOW)
            self.UD(GPIO.HIGH)
            if (self._state>0):
                state -= 1
        self.CS(GPIO.HIGH)
        self.nonvolatile_state.set(state)
        
    def inc(self, step_nr):
        self.CS(GPIO.HIGH)
        self.UD(GPIO.LOW)
        self.CS(GPIO.LOW)
        for i in range(step_nr):
            self.UD(GPIO.LOW)
            self.UD(GPIO.HIGH)
            if (self._state<63):
                state += 1
        self.CS(GPIO.HIGH)
        self.nonvolatile_state.set(state)
        
    def set(self, val):
        self.dec(64)
        self.inc(val)
        
    def save(self):
        self.nonvolatile_state.save()
            
        