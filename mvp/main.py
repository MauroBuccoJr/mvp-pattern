import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
from presenters.main_presenter import MainPresenter
from models.message_model import MessageModel

def change_message():
    presenter.updateMessage("123456")
    print(model.message)


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    model = MessageModel()
    engine = QQmlApplicationEngine()
    presenter = MainPresenter(engine, model)
    engine.load(QUrl('mvp/views/main.qml'))
    view = engine.rootObjects()[-1]
    #view.setSource(QUrl('mvp/views/main.qml'))
    
    view.show()
    change_message()
    sys.exit(app.exec_())
