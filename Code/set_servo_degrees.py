from machine import I2C, Pin
from servo import Servo
from time import sleep

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

# index for servos
right_upper_eyelid = 0
right_lower_eyelid = 1
left_upper_eyelid = 2
left_lower_eyelid = 3
right_left_right = 4
right_up_down = 5
left_up_down = 6
left_left_right = 7


right_upper_eyelid = Servo(i2c=i2c, index=right_upper_eyelid)
right_lower_eyelid = Servo(i2c=i2c, index=right_lower_eyelid)
left_upper_eyelid = Servo(i2c=i2c, index=left_upper_eyelid)
left_lower_eyelid = Servo(i2c=i2c, index=left_lower_eyelid)
right_left_right = Servo(i2c=i2c, index=right_left_right)
right_up_down = Servo(i2c=i2c, index=right_up_down)
left_up_down = Servo(i2c=i2c, index=left_up_down)
left_left_right = Servo(i2c=i2c, index=left_left_right)

# <servo_name>.position(degrees)


