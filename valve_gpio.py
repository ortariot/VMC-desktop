import RPi.GPIO as GPIO
import sys


class ValveGPIO():
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        # pin inicialization
        pin_valve_one = 2
        pin_valve_two = 3
        pin_valve_three = 4
        pin_valve_for = 5
        # GPIO pin inicialization as OUT
        GPIO.setup(pin_valve_one, GPIO.OUT)
        GPIO.setup(pin_valve_two, GPIO.OUT)
        GPIO.setup(pin_valve_three, GPIO.OUT)
        GPIO.setup(pin_valve_for, GPIO.OUT)
        # OUT inicialization as PWM object
        valve_one = GPIO.PWM(pin_valve_one, 1)
        valve_two = GPIO.PWM(pin_valve_two, 1)
        valve_three = GPIO.PWM(pin_valve_three, 1)
        valve_for = GPIO.PWM(pin_valve_for, 1)
        # dict for valve independent control
        self.valve_store = {1: valve_one,
                            2: valve_two,
                            3: valve_three,
                            4: valve_for
                            }

    def set_duty(self, valve_num, duty):
        self.valve_store[valve_num].ChangeDutyCycle(duty)

    def set_freq(self, valve_num, freq):
        self.valve_store[valve_num].ChangeFrequency(freq)

    def sw_exit(self):
        GPIO.cleanup()
        sys.exit()

    def sw_start(self, valve_num):
        self.valve_store[valve_num].start(50)

    def sw_stop(self, valve_num):
        self.valve_store[valve_num].stop()


def main():
    pass


main()
