from machine import Pin

Buttons = {'UP':4, 'DOWN':0, 'LEFT':3, 'RIGHT':2, 'MIDDLE':1}

class keyboard:
    
    def __init__(self):
        
        self._butt_up_pin(Buttons['UP'], Pin.IN, Pin.PULL_UP)
        self._butt_dn_pin(Buttons['DOWN'], Pin.IN, Pin.PULL_UP)
        self._butt_lt_pin(Buttons['LEFT'], Pin.IN, Pin.PULL_UP)
        self._butt_rt_pin(Buttons['RIGHT'], Pin.IN, Pin.PULL_UP)
        self._butt_md_pin(Buttons['MIDDLE'], Pin.IN, Pin.PULL_UP)
        
        self._previous_keyboard_state = self.read_buttons()
        
    def read_buttons(self):
        if  self._butt_up_pin.val == 0:
            return 'UP'
        elif self._butt_dn_pin.val == 0:
            return 'DOWN'
        elif self._butt_lt_pin.val == 0:
            return 'LEFT'
        elif self._butt_rt_pin.val == 0:
            return 'RIGHT'
        elif self._butt_md_pin.val == 0:
            return 'MIDDLE'
        else:
            return 'RELEASED'
        
    def read(self):
        result = 'RELEASED'
        
        current_keyboard_state = self.read_buttons()
        if (current_keyboard_state != 'RELEASED') and (self._previous_keyboard_state == 'RELEASED'):
            result = current_keyboard_state
        self._previous_keyboard_state = current_keyboard_state
        return result
        
        
        