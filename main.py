#!/bin/env python3.8
import sys
from PyQt5 import QtWidgets
import vd_design
from valve_gpio import ValveGPIO


class WindowsForms(QtWidgets.QMainWindow, vd_design.Ui_MainWindow, ValveGPIO):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ValveGPIO.__init__(self)
        self.vlv1_verticalSlider.setRange(1, 100)
        self.vlv1_verticalSlider.setValue(1)
        self.vlv1_lcdNumber.display(1)
        self.vlv1_verticalSlider.valueChanged.connect(self.slider_vlv1)
        self.vlv2_verticalSlider.setRange(1, 100)
        self.vlv2_verticalSlider.setValue(1)
        self.vlv2_lcdNumber.display(1)
        self.vlv2_verticalSlider.valueChanged.connect(self.slider_vlv2)
        self.vlv3_verticalSlider.setRange(1, 100)
        self.vlv3_verticalSlider.valueChanged.connect(self.slider_vlv3)
        self.vlv3_verticalSlider.setValue(1)
        self.vlv3_lcdNumber.display(1)
        self.vlv4_verticalSlider.setRange(1, 100)
        self.vlv4_verticalSlider.setValue(1)
        self.vlv4_verticalSlider.valueChanged.connect(self.slider_vlv4)
        self.vlv4_lcdNumber.display(1)
        self.vlv1_button.clicked.connect(self.btn_vlv1)
        self.vlv2_button.clicked.connect(self.btn_vlv2)
        self.vlv3_button.clicked.connect(self.btn_vlv3)
        self.vlv4_button.clicked.connect(self.btn_vlv4)

    def button_action(self, valve_num, button_obj, slider_obj):
        if button_obj.text() == f"VALVE{valve_num} ON":
            self.sw_init(valve_num)
            slider_obj.setEnabled(True)
            self.sw_start(valve_num, slider_obj.value())
            button_obj.setText(f"VALVE{valve_num} OFF")
        elif button_obj.text() == f"VALVE{valve_num} OFF":
            self.sw_stop(valve_num)
            button_obj.setText(f"VALVE{valve_num} ON")
            slider_obj.setEnabled(False)

    def slaide_action(self, valve_num, slider_obj, dysplay_obj):
        value_vlv1 = slider_obj.value()
        dysplay_obj.display(value_vlv1)
        self.set_duty(valve_num, value_vlv1)

    def slider_vlv1(self):
        self.slaide_action(1, self.vlv1_verticalSlider, self.vlv1_lcdNumber)

    def slider_vlv2(self):
        self.slaide_action(2, self.vlv1_verticalSlider, self.vlv1_lcdNumber)

    def slider_vlv3(self):
        self.slaide_action(3, self.vlv1_verticalSlider, self.vlv1_lcdNumber)

    def slider_vlv4(self):
        self.slaide_action(4, self.vlv1_verticalSlider, self.vlv1_lcdNumber)

    def btn_vlv1(self):
        self.button_action(1, self.vlv1_button, self.vlv1_verticalSlider)

    def btn_vlv2(self):
        self.button_action(2, self.vlv2_button, self.vlv2_verticalSlider)

    def btn_vlv3(self):
        self.button_action(3, self.vlv3_button, self.vlv3_verticalSlider)

    def btn_vlv4(self):
        self.button_action(4, self.vlv4_button, self.vlv4_verticalSlider)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowsForms()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
