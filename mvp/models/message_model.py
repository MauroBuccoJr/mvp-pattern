class MessageModel:

    def __init__(self):
        self._message = "Hello, World!"
        self._states = ["" for i in range(10)]

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def states(self):
        return self._states
    
    @states.setter
    def states(self, values):
        self._states = values

