import RPi.GPIO as GPIO
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
        # GPIO pin inicialization as OUT
        GPIO.setup(pin_valve_one, GPIO.OUT)
        GPIO.setup(pin_valve_two, GPIO.OUT)
        GPIO.setup(pin_valve_three, GPIO.OUT)
        GPIO.setup(pin_valve_for, GPIO.OUT)
        # OUT inicialization as PWM object
        self.valve_one = GPIO.PWM(pin_valve_one, 1)
        self.valve_two = GPIO.PWM(pin_valve_two, 1)
        self.valve_three = GPIO.PWM(pin_valve_three, 1)
        self.valve_for = GPIO.PWM(pin_valve_for, 1)
        # dict for valve independent control
        self.valve_store = {1: self.valve_one,
                            2: self.valve_two,
                            3: self.valve_three,
                            4: self.valve_for
                            }
        for valve in self.valve_store.values():
            valve.stop()
            valve.ChangeFrequency(0.5)

    def set_duty(self, valve_num, duty):
        self.valve_store[valve_num].ChangeDutyCycle(duty)

    def set_freq(self, valve_num, freq):
        self.valve_store[valve_num].ChangeFrequency(freq)

    def sw_exit(self):
        GPIO.cleanup()
        sys.exit()

    def sw_start(self, valve_num, duty=50):
        self.valve_store[valve_num].start(duty)

    def sw_stop(self, valve_num):
        self.valve_store[valve_num].stop()


def main():
    pass


main()
