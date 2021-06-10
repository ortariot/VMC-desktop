import RPi.GPIO as GPIO
# as varuant https://github.com/metachris/RPIO 
# https://pypi.org/project/RPIO/
import sys


class ValveGPIO():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        # pin inicialization
        pin_valve_one = 2
        pin_valve_two = 3
        pin_valve_three = 27
        pin_valve_for = 5
        self.pin_store = {1: pin_valve_one,
                          2: pin_valve_two,
                          3: pin_valve_three,
                          4: pin_valve_for
                          }
        self.valve_store = {1: None,
                            2: None,
                            3: None,
                            4: None
                            }

    def set_duty(self, valve_num, duty):
        self.valve_store[valve_num].ChangeDutyCycle(duty)

    def set_freq(self, valve_num, freq):
        self.valve_store[valve_num].ChangeFrequency(freq)

    def sw_exit(self):
        GPIO.cleanup()
        sys.exit()

    def sw_start(self, valve_num, duty=50):
        self.valve_store[valve_num].start(duty)

    def sw_init(self, valve_num):
        GPIO.setup(self.pin_store[valve_num], GPIO.OUT)
        GPIO.output(self.pin_store[valve_num], False)
        self.valve_store[valve_num] = GPIO.PWM(self.pin_store[valve_num], 1)
        self.valve_store[valve_num].ChangeFrequency(0.5)

    def sw_stop(self, valve_num):
        self.valve_store[valve_num].stop()
        GPIO.cleanup(self.pin_store[valve_num])


def main():
    pass


main()
