import machine
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import freesans20
import writer


WIDTH  = 128                                          
HEIGHT = 64                                             

i2c=machine.SoftI2C(sda=machine.Pin(20), scl=machine.Pin(21), freq=100000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)

font_writer = writer.Writer(oled, freesans20)
for y,t in zip((0,24,44),('vdd','1.234V','0.836A')):
    font_writer.set_textpos(0, y)
    font_writer.printstring(t)
oled.show()