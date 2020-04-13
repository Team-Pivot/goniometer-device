import sys
import PyQt5
from PyQt5.QtWidgets import *
import customWindow
from angleScreen import AngleScreen
from patientListScreen import PatientList

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, customWindow.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        # todo: make this into a patient object to store joint, flextion, ect...
        self.jointTypes = {
            'elbow':'elbow',
            'ankle':'ankle',
            'knee':'knee'
        }
        self.measurementType = {
            'flex':'flexion',
            'exten':'extension'
        }

        # session info
        self.measurement = {
            'angle': 0.0,
            'endAngle': 0.0,
            'jointType': '',
            'measurementType': '',
            'clientId': '',
            'clinic':'58aa8171-7c36-11ea-8966-9828a60a17af'
        }
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

    def openOptions(self, joint):
        if (joint == 'elbow'):
            self.measurement['jointType'] = self.jointTypes['elbow']
        elif (joint == 'ankle'):
            self.measurement['jointType'] = self.jointTypes['ankle']
        else:
            self.measurement['jointType'] = self.jointTypes['knee']
        self.stackedWidget.setCurrentIndex(4)

    def openAngle(self):
        self.stackedWidget.setCurrentIndex(5)

class NavigationManager:
    def __init__(self, window):
        self.window = window
        window.openHome()
        self.angleUI = AngleScreen(window)
        self.patientListUI = PatientList(window)

        self.setupHomeListeners()
        self.setupPatientsListeners()
        self.setupJointsListeners()
        self.setupOptionsListeners()

    def setupHomeListeners(self):
        window = self.window
        # window.patientBtn.clicked.connect(window.openPatients)
        window.patientBtn.clicked.connect(lambda: self.patientListUI.showUI())
        # window.quickMeasureBtn.clicked.connect(window.openAngle)
        window.quickMeasureBtn.clicked.connect(lambda: self.angleUI.showUI(1))

    def setupPatientsListeners(self):
        window = self.window
        # window.patient1_2.clicked.connect(window.openJoints)
        # window.patient2_2.clicked.connect(window.openJoints)
        window.patientsCancel.clicked.connect(window.openHome)

    def setupJointsListeners(self):
        window = self.window
        window.elbow_2.clicked.connect(lambda: window.openOptions('elbow'))
        window.ankle_2.clicked.connect(lambda: window.openOptions('ankle'))
        window.knee_2.clicked.connect(lambda: window.openOptions('knee'))
        window.jointCancel_2.clicked.connect(window.openPatients)

    def setupOptionsListeners(self):
        window = self.window
        window.extension_2.clicked.connect(lambda: self.angleUI.showUI(4, 0))
        window.flextion_2.clicked.connect(lambda: self.angleUI.showUI(4, 1))
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
