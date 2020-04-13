import requests
from apiError import ApiError
from PyQt5 import QtCore, QtGui, QtWidgets

class PatientList:
    # patientsUri = 'http://localhost:3000/v1/clients'
    patientsUri = 'http://ec2-18-220-197-38.us-east-2.compute.amazonaws.com:80/v1/clients'

    def __init__(self, window):
        self.window = window

    def showUI(self):
		window = self.window
        window.openPatients()
		window.patientsCancel.clicked.connect(lambda: window.openHome())
        self.getPatients()

    def getPatients(self):
        resp = requests.get(self.patientsUri)
        if resp.status_code != 200:
            raise ApiError('getPatients failed w/ error {}'.format(resp.status_code))
        else:
            print('got a resp')
            self.populateUI(resp.json())

    def populateUI(self, response):
        #test values
        # response.append({'firstName':'Jeff', 'lastName':'Wongo'})
        # response.append({'firstName':'Alan', 'lastName':'Watts'})
        # response.append({'firstName':'Dan', 'lastName':'Dude'})
        # response.append({'firstName':'Dan', 'lastName':'Dude'})
        # response.append({'firstName':'Dan', 'lastName':'Dude'})
        # response.append({'firstName':'Dan', 'lastName':'Dude'})
        d = {}
        y = 0
        window = self.window
        for i in range(0, len(response)):
            if (i == 0):
                y += 20
            else:
                y += 60
            # print(response[i])
            d['button{}'.format(i)] = QtWidgets.QPushButton()
            d['button{}'.format(i)].setGeometry(QtCore.QRect(30, y, 351, 41))
            font = QtGui.QFont()
            font.setPointSize(10)
            d['button{}'.format(i)].setFont(font)
            name = response[i]['firstName'] + ' ' + response[i]['lastName']
            _translate = QtCore.QCoreApplication.translate
            d['button{}'.format(i)].setText(_translate("MainWindow", name))
            window.scrollLayout.addWidget(d['button{}'.format(i)])
            id = response[i]['id']
            d['button{}'.format(i)].clicked.connect(lambda: self.setClient(id))
            d['button{}'.format(i)].show()
        for val in d.values():
            val.show()

    def setClient(self, patientId):
        self.window.measurement['clientId'] = patientId
        self.window.openJoints()
