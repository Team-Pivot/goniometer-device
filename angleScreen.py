from encoder import Encoder
import requests
from apiError import ApiError

# If you're not running on the pi, comment out any lines with encoder
class AngleScreen:
    def __init__(self, window):
        self.window = window
        self.sourceIndex = -1
        self.angle = 10
        self.encoder = Encoder(window)

    def showUI(self, source, measurementType):
        window = self.window
        measureTypes = self.window.measurementType
        if (measurementType == 0):
            window.measurement['measurementType'] = measureTypes['exten']
        else:
            window.measurement['measurementType'] = measureTypes['flex']
        self.sourceIndex = source
        window.openAngle()
        self.setupListeners()
        self.encoder.enable()

    def setupListeners(self):
        window = self.window
        window.angleCancel.clicked.connect(self.exit)
        window.sendBtn.clicked.connect(self.sendMeasurement)

    def exit(self):
        window = self.window
        if (self.sourceIndex == 1):
            window.openHome()
        elif (self.sourceIndex == 4):
            window.openOptions(window.measurement['jointType'])

    # TODO: all api calls should be in one locaiton
    def sendMeasurement(self):
        print('Sending measurement...')
        self.encoder.disable()
        self.angle = self.encoder.angle
        # measurementUri = 'http://localhost:3000/v1/clients/{}/measurements'.format(self.window.measurement['clientId'])
        measurementUri = 'http://ec2-18-220-197-38.us-east-2.compute.amazonaws.com:80/v1/clients/{}/measurements'.format(self.window.measurement['clientId'])
        print(measurementUri)
        measurement = self.window.measurement
        measurement['angle'] = float(self.angle)
        print("About to send: {}".format(measurement))
        post = requests.post(measurementUri, data = measurement)
        if post.status_code != 201:
            raise ApiError('sendMeasurement failed w/ error {}'.format(post.json()))
        else:
            print('got a resp: \n{}'.format(post.json()))
            self.exit()
