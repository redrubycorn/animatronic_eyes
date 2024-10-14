from machine import I2C, Pin
from servo import Servo
from eye_servos_library import servos

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

for servo_name, servo_data in servos.items():
    index = servo_data["index"]
    print(f"{servo_name}: index {index}")
    servo_name = Servo(i2c=i2c, index=index)
    servo_name.position(90)
    
