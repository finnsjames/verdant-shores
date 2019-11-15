from PyQt5 import QtCore, QtWidgets, QtGui, QtChart
from time_ui import Ui_Dialog     # compiled PyQt dialogue ui
import time
from precious import MyPrecious

class TimeDialog(QtWidgets.QDialog):
    """New observation dialogue window"""
    
    def __init__(self, superclock):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Set time")

        # store parent window
        self.superclock = superclock

        # connect okay button
        self.ui.dialog_button_box.accepted.connect(self.handle_ok)

    def handle_ok(self):
        
        pattern = "%H:%M:%S"
        
        print(self.ui.sidereal_value.text())
        self.superclock.starting_sidereal_time = time.mktime(time.strptime(self.ui.sidereal_value.text(), pattern))
        self.superclock.starting_time = time.time()