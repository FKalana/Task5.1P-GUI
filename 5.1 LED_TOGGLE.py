import RPi.GPIO as GPIO  # Importing the GPIO library for Raspberry Pi
GPIO.setmode(GPIO.BOARD)  # Setting the GPIO pin numbering mode to BOARD
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setup(11, GPIO.OUT)  # Setting up pin 11 as an output
GPIO.setup(13, GPIO.OUT)  # Setting up pin 13 as an output
GPIO.setup(15, GPIO.OUT)  # Setting up pin 15 as an output

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 600, 600, 600)  # Setting window geometry
        self.setWindowTitle("LED Toggle")  # Setting window title
        self.initUI()  # Initializing the UI
        
    def initUI(self):
        # Creating buttons
        self.b = QtWidgets.QPushButton(self)
        self.b.setText("Blue")  # Setting button text
        self.b.move(60, 0)  # Moving button position
        self.b.clicked.connect(self.blue)  # Connecting button click to blue function
        
        self.r = QtWidgets.QPushButton(self)
        self.r.setText("Red")  # Setting button text
        self.r.move(90, 0)  # Moving button position
        self.r.clicked.connect(self.red)  # Connecting button click to red function
        
        self.y = QtWidgets.QPushButton(self)
        self.y.setText("Yellow")  # Setting button text
        self.y.move(180,0)  # Moving button position
        self.y.clicked.connect(self.yellow)  # Connecting button click to yellow function
        
        self.e = QtWidgets.QPushButton(self)
        self.e.setText("Quit")  # Setting button text
        self.e.move(50, 50)  # Moving button position
        self.e.clicked.connect(self.close)  # Connecting button click to close function
        
    def blue(self):
        # Turning on blue LED and turning off others
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        
    def red(self):
        # Turning on red LED and turning off others
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        
    def yellow(self):
        # Turning on yellow LED and turning off others
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        
    def close(self):
        # Turning off all LEDs
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()  # Creating instance of MyWindow class
    win.show()  # Displaying the window
    sys.exit(app.exec_())  # Exiting the application when window is closed

window()  # Calling the window function to run the application
