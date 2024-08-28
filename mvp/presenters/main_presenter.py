from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal

class MainPresenter(QObject):
    messageChanged = pyqtSignal()
    statesChanged = pyqtSignal()

    def __init__(self, view, model):
        super().__init__()
        self._view = view
        self._model = model
        self._view.rootContext().setContextProperty("presenter", self)

    @pyqtProperty(str, notify=messageChanged, final=True)
    def message(self):
        return self._model.message

    @pyqtSlot(str)
    def updateMessage(self, new_message):
        self._model.message = new_message
        self.messageChanged.emit()

    @pyqtProperty(str, notify=statesChanged, final=True)
    def states(self):
        return self._model.states

    @pyqtSlot(list)
    def updateMessage(self, values):
        self._model.states = values
        self.statesChanged.emit()
