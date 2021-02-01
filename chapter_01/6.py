import sys
from PySide2 import QtCore, QtWidgets

# Create a Qt application
app = QtWidgets.QApplication(sys.argv)

# Create a Window
mywindow = QtWidgets.QWidget()
mywindow.resize(320, 240)
mywindow.setWindowTitle('Hello, World!')

# Create a label and display it all together
mylabel = QtWidgets.QLabel(mywindow)
mylabel.setText('Hello, World!')
mylabel.setGeometry(QtCore.QRect(200, 200, 200, 200))

mywindow.show()

# Enter Qt application main loop
sys.exit(app.exec_())