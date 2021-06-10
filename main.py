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
        self.vlv1_verticalSlider.setValue(50)
        self.vlv1_lcdNumber.display(50)
        self.vlv1_verticalSlider.valueChanged.connect(self.slider_vlv1)
        self.vlv2_verticalSlider.setRange(1, 100)
        self.vlv2_verticalSlider.setValue(50)
        self.vlv2_lcdNumber.display(50)
        self.vlv2_verticalSlider.valueChanged.connect(self.slider_vlv2)
        self.vlv3_verticalSlider.setRange(1, 100)
        self.vlv3_verticalSlider.valueChanged.connect(self.slider_vlv3)
        self.vlv3_verticalSlider.setValue(50)
        self.vlv3_lcdNumber.display(50)
        self.vlv4_verticalSlider.setRange(1, 100)
        self.vlv4_verticalSlider.setValue(50)
        self.vlv4_verticalSlider.valueChanged.connect(self.slider_vlv4)
        self.vlv4_lcdNumber.display(50)
        self.vlv1_button.clicked.connect(self.btn_vlv1)
        self.vlv2_button.clicked.connect(self.btn_vlv2)
        self.vlv3_button.clicked.connect(self.btn_vlv3)
        self.vlv4_button.clicked.connect(self.btn_vlv4)

    def slider_vlv1(self):
        value_vlv1 = self.vlv1_verticalSlider.value()
        self.vlv1_lcdNumber.display(value_vlv1)
        self.set_duty(1, value_vlv1)
   

    def slider_vlv2(self):
        value_vlv2 = self.vlv2_verticalSlider.value()
        self.vlv2_lcdNumber.display(value_vlv2)
        self.set_duty(2, value_vlv2)


    def slider_vlv3(self):
        value_vlv3 = self.vlv3_verticalSlider.value()
        self.vlv3_lcdNumber.display(value_vlv3)
        self.set_duty(3, value_vlv3)

    def slider_vlv4(self):
        value_vlv4 = self.vlv4_verticalSlider.value()
        self.vlv4_lcdNumber.display(value_vlv4)
        self.set_duty(4, value_vlv4)

    def btn_vlv1(self):
        if self.vlv1_button.text() == "VALVE1 ON":
            self.sw_start(1, self.vlv1_verticalSlider.value())
            self.vlv1_button.setText("VALVE1 OFF")
            self.vlv1_verticalSlider.setEnabled(True)
        elif self.vlv1_button.text() == "VALVE1 OFF":
            self.sw_stop(1)
            self.vlv1_button.setText("VALVE1 ON")
            self.vlv1_verticalSlider.setEnabled(False)

    def btn_vlv2(self):
        if self.vlv2_button.text() == "VALVE2 ON":
            self.sw_start(2), self.vlv2_verticalSlider.value()
            self.vlv2_button.setText("VALVE2 OFF")
            self.vlv2_verticalSlider.setEnabled(True)
        elif self.vlv2_button.text() == "VALVE2 OFF":
            self.sw_stop(2)
            self.vlv2_button.setText("VALVE2 ON")
            self.vlv2_verticalSlider.setEnabled(False)

    def btn_vlv3(self):
        if self.vlv3_button.text() == "VALVE3 ON":
            self.sw_start(3, self.vlv3_verticalSlider.value())
            self.vlv3_button.setText("VALVE3 OFF")
            self.vlv3_verticalSlider.setEnabled(True)
        elif self.vlv3_button.text() == "VALVE3 OFF":
            self.sw_stop(3)
            self.vlv3_button.setText("VALVE3 ON")
            self.vlv3_verticalSlider.setEnabled(False)

    def btn_vlv4(self):
        if self.vlv4_button.text() == "VALVE4 ON":
            self.sw_start(4, self.vlv4_verticalSlider.value())
            self.vlv4_button.setText("VALVE4 OFF")
            self.vlv4_verticalSlider.setEnabled(True)
        elif self.vlv4_button.text() == "VALVE4 OFF":
            self.sw_stop(4)
            self.vlv4_button.setText("VALVE4 ON")
            self.vlv4_verticalSlider.setEnabled(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowsForms()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
