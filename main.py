import sys
import PyQt5
from PyQt5.QtWidgets import *
import mainStack
from angleScreen import AngleScreen

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainStack.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def printName(self):
        print("Window")

    def openSetup(self):
        self.stackedWidget.setCurrentIndex(0)

    def openHome(self):
        self.stackedWidget.setCurrentIndex(1)

    def openPatients(self):
        self.stackedWidget.setCurrentIndex(2)

    def openJoints(self):
        self.stackedWidget.setCurrentIndex(3)

    def openOptions(self):
        self.stackedWidget.setCurrentIndex(4)

    def openAngle(self):
        self.stackedWidget.setCurrentIndex(5)

class NavigationManager:
    def __init__(self, window):
        self.window = window
        window.openHome()
        self.angleUI = AngleScreen(window)

        self.setupHomeListeners()
        self.setupPatientsListeners()
        self.setupJointsListeners()
        self.setupOptionsListeners()

    def setupHomeListeners(self):
        window = self.window
        window.patientBtn.clicked.connect(window.openPatients)
        # window.quickMeasureBtn.clicked.connect(window.openAngle)
        window.quickMeasureBtn.clicked.connect(lambda: self.angleUI.showuI(1))

    def setupPatientsListeners(self):
        window = self.window
        window.patient1_2.clicked.connect(window.openJoints)
        window.patient2_2.clicked.connect(window.openJoints)
        window.patientsCancel.clicked.connect(window.openHome)

    def setupJointsListeners(self):
        window = self.window
        window.elbow_2.clicked.connect(window.openOptions)
        window.ankle_2.clicked.connect(window.openOptions)
        window.knee_2.clicked.connect(window.openOptions)
        window.jointCancel_2.clicked.connect(window.openPatients)

    def setupOptionsListeners(self):
        window = self.window
        window.extension_2.clicked.connect(lambda: self.angleUI.showuI(4))
        window.flextion_2.clicked.connect(lambda: self.angleUI.showuI(4))
        window.measureTypeCancel.clicked.connect(window.openJoints)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    navigator = NavigationManager(window)
    # window.openHome()
    # window.quickMeasureBtn.clicked.connect(window.openAngle)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
