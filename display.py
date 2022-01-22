import machine
from ssd1306 import SSD1306_I2C
import framebuf
import freesans24
import writer

class Display:
    
    __CHAN_NAMES = {0:'core', 1:'peri', 2:'ddm', 3:'dda', 4:'disc'}
    
    def __init__(self, i2c):    
        self._oled = SSD1306_I2C(128, 64, i2c)
        self._font_writer = writer.Writer(self._oled, freesans24)
        
    def show(self, chan_nr, curr, vol):
        self._oled.fill(0)
        for x,y,t in zip((0,48,48),(22,8,40),(self.__CHAN_NAMES[chan_nr],f"{curr:.3f}V",f"{vol:.3f}A")):
            self._font_writer.set_textpos(x, y)
            self._font_writer.printstring(t)
        self._oled.show()
