from machine import I2C, Pin
from eyeservo import Servo

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

test_servo = Servo(i2c=i2c, index=0)

test_servo.position(0)