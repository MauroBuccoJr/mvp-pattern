import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "MVP Example"

    Column {
        anchors.centerIn: parent

        TextField {
            id: messageInput
            placeholderText: "Enter a message"
        }

        Button {
            text: "Update Message"
            onClicked: presenter.updateMessage(messageInput.text)
        }

        Text {
            id: messageDisplay
            text: presenter.message
        }
    }
}
