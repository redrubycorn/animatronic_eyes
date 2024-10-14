from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servo

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
servo = Servo(i2c=i2c)

servos = {
    "right_upper_eyelid": 0,
    "right_lower_eyelid": 1,
    "left_upper_eyelid": 2,
    "left_lower_eyelid": 3,
    "right_left_right": 4,
    "right_up_down": 5,
    "left_up_down": 6,
    "left_left_right": 7
}

def set_servo_position(index, position):
    servo.position(index=index, degrees=position)