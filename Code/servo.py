from time import sleep
from pca9685 import PCA9685


class Servo:
    def __init__(self, i2c, index, address=0x40, freq=50, min_us=400, max_us=2400,
                 degrees=180):
        self.period_us = 1000000 / freq # period in us to work easier with servos pulse width which is in us
        self.min_duty = self._us2duty(min_us) # convert the min_us to a pwm value the PCA can use
        self.max_duty = self._us2duty(max_us) # convert the max_us to a pwm value the PCA can use
        self.degrees = degrees
        self.freq = freq
        self.index = index
        self.pca9685 = PCA9685(i2c, address)
        self.pca9685.freq(freq)

    def _us2duty(self, value):
        """
        Converts a duty cycle from us to a pwm signal the PCA9685 can use. It uses the following formula:
        pwm_value = pulse_width_us / period_us * 4096
        
        Parameters:
        value (int or float): The value in us between min_us and max_us to convert to a pwm value.
        
        Returns:
        An int pwm value between 0 and 4096 that the PCA9685 can use.
        
        Example:
        obj._us2duty(1400)
        """
        return int(value / self.period_us * 4096)

    def position(self, degrees):
        """
        Takes a value in degrees, converts it to a pwm value the PCA9685 can use and then sets the angle of the servo.
        
        Parameters:
        degrees (int): The degree you want to set the servo to.
        
        Returns:
        None
        
        Example:
        obj.position(90)
        """
        span = self.max_duty - self.min_duty
        duty = self.min_duty + span * degrees / self.degrees
        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685.duty(self.index, duty)
