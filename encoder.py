from RPi import GPIO
from time import sleep
import threading
from PyQt5 import QtCore, QtGui, QtWidgets

class Encoder:
	def __init__(self, window):
		self.window = window
		self.activated = 0
		self.angle = 0
		self.clk = -1
		self.dt = -1
		self.btn = -1

	def enable(self):
		self.setupPins()
		self.activated = 1
		encoderThread = threading.Thread(target=self.pollPins, args=())
		encoderThread.start()

	def disable(self):
		self.activated = 0

	def setupPins(self):
		GPIO.setmode(GPIO.BOARD)

		#set power pin
		GPIO.setup(37, GPIO.OUT)
		GPIO.output(37, GPIO.HIGH)

		self.clk = 40        #clockwise
		self.dt = 38         #counter clockwise
		self.btn = 36        #shaft push set angle to 0

		GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.btn, GPIO.RISING)

	def pollPins(self):
		print("Starting encoder thread")
		clk = self.clk
		dt = self.dt
		btn = self.btn
		angle = 0
		clkLastState = GPIO.input(clk)
		try:
			while self.activated:
				if (angle == 360):
					angle = 0
				clkState = GPIO.input(clk)
				if GPIO.event_detected(btn):
					angle = 0
					print("angle: {}".format(angle))
					strAngle = str(angle)
					self.window.angle_2.setText(_translate("MainWindow", strAngle))
				if clkState != clkLastState:
					dtState = GPIO.input(dt)
					if dtState != clkState:
						angle -= 9
					else:
						angle += 9
					print("angle: {}".format(angle))
					strAngle = str(angle)
					self.window.angle_2.setText(_translate("MainWindow", strAngle))
				self.angle = angle
				clkLastState = clkState
		finally:
			GPIO.cleanup()
			self.angle = angle
			print("Ending encoder thread")
			print('final angle: {}'.format(angle))
