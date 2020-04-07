class AngleScreen:
    def __init__(self, window):
        self.window = window
        self.sourceIndex = -1

    def showUI(self, source):
        self.sourceIndex = source
        self.window.openAngle()
        self.setupListeners()

    def setupListeners(self):
        window = self.window
        if (self.sourceIndex == 1):
            window.angleCancel.clicked.connect(window.openHome)
        elif (self.sourceIndex == 4):
            window.angleCancel.clicked.connect(window.openOptions)
