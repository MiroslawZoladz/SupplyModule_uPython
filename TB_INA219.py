import machine
from INA219 import INA219_Current,INA219_Voltage

sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

#ina_vol = INA219_Voltage(i2c)
ina_cur = INA219_Current(i2c)

# ina_vol.config('sadc', 0xF)
ina_cur.config('sadc', 0xF)

# ina_vol.config('badc', 0xF)
ina_cur.config('badc', 0xF)

# ina_vol.config('pg', 0x0)
ina_cur.config('pg', 0x0)

# ina_vol.config('brng', 0x0)
ina_cur.config('brng', 0x0)

# print("Bus voltage raw: %i " % ina_vol.measure_raw())
print("Shunt voltage raw: %i " % ina_cur.measure_raw())

# print("Bus voltage: %i " % ina_vol.measure())
print("Shunt voltage: %i " % ina_cur.measure())

print("Coefficient: %f" % ina_cur.read_coefficient())

# ina_vol.callib(2)
ina_cur.callib(32)

# print("%f" % ina_vol.read_coefficient())
print("Coefficient: %f" % ina_cur.read_coefficient())

# print("Bus voltage: %i " % ina_vol.measure())
print("Shunt voltage: %i " % ina_cur.measure())