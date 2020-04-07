import requests
from apiError import ApiError
from PyQt5 import QtCore, QtGui, QtWidgets

class PatientList:
    patientsUri = 'http://localhost:3000/v1/clients'

    def __init__(self, window):
        self.window = window

    def showUI(self):
        self.window.openPatients()
        self.getPatients()
        # self.setupListeners()

    def getPatients(self):
        resp = requests.get(self.patientsUri)
        if resp.status_code != 200:
            raise ApiError('getPatients failed w/ error {}'.format(resp.status_code))
        else:
            print('got a resp')
            self.populateUI(resp.json())

    def populateUI(self, response):
        #test values
        response.append({'firstName':'Jeff', 'lastName':'Wongo'})
        response.append({'firstName':'Alan', 'lastName':'Watts'})
        d = {}
        y = 0
        window = self.window
        for i in range(0, len(response)):
            if (i == 0):
                y += 20
            else:
                y += 60
            # print(response[i])
            d['button{}'.format(i)] = QtWidgets.QPushButton(window.scrollAreaWidgetContents_2)
            d['button{}'.format(i)].setGeometry(QtCore.QRect(30, y, 351, 41))
            font = QtGui.QFont()
            font.setPointSize(10)
            d['button{}'.format(i)].setFont(font)
            name = response[i]['firstName'] + ' ' + response[i]['lastName']
            _translate = QtCore.QCoreApplication.translate
            d['button{}'.format(i)].setText(_translate("MainWindow", name))
            d['button{}'.format(i)].show()
        print(len(d))
        for val in d.values():
            print(val.parent())
            val.show()
