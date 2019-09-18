from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UiRunningConverter(QtWidgets.QWidget):    #parameter changed from "object" to "QtWidgets.QWidget"
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, RunningConverter):
        RunningConverter.setObjectName("RunningConverter")
        RunningConverter.resize(275, 187)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        RunningConverter.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RunningConverter)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.lbDistance = QtWidgets.QLabel(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setKerning(False)
        self.lbDistance.setFont(font)
        self.lbDistance.setObjectName("lbDistance")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbDistance)
        self.leDistance = QtWidgets.QLineEdit(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.leDistance.setFont(font)
        self.leDistance.setText("")
        self.leDistance.setFrame(True)
        self.leDistance.setAlignment(QtCore.Qt.AlignCenter)
        self.leDistance.setObjectName("leDistance")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leDistance)
        self.lbTime = QtWidgets.QLabel(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.lbTime.setFont(font)
        self.lbTime.setObjectName("lbTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbTime)
        self.leTime = QtWidgets.QLineEdit(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.leTime.setFont(font)
        self.leTime.setText("")
        self.leTime.setAlignment(QtCore.Qt.AlignCenter)
        self.leTime.setObjectName("leTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leTime)
        self.lbPace = QtWidgets.QLabel(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.lbPace.setFont(font)
        self.lbPace.setObjectName("lbPace")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbPace)
        self.lePace = QtWidgets.QLineEdit(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.lePace.setFont(font)
        self.lePace.setText("")
        self.lePace.setAlignment(QtCore.Qt.AlignCenter)
        self.lePace.setObjectName("lePace")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lePace)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btConvert = QtWidgets.QPushButton(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.btConvert.setFont(font)
        self.btConvert.setObjectName("btConvert")
        self.verticalLayout_2.addWidget(self.btConvert)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(RunningConverter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(RunningConverter)
        QtCore.QMetaObject.connectSlotsByName(RunningConverter)

    def retranslateUi(self, RunningConverter):
        _translate = QtCore.QCoreApplication.translate
        RunningConverter.setWindowTitle(_translate("RunningConverter", "Running Converter"))
        self.lbDistance.setText(_translate("RunningConverter", "DISTANCE (km)"))
        self.lbTime.setText(_translate("RunningConverter", "TIME (min)"))
        self.lbPace.setText(_translate("RunningConverter", "PACE (min/km)"))
        self.btConvert.setText(_translate("RunningConverter", "Convert!"))
        self.btConvert.clicked.connect(self.distributer)

    def distributer(self):
        try:
            self.label.setText("")
            if self.lePace.text() == "":
                self.pace()
            elif self.leDistance.text() == "":
                self.distance()
            elif self.leTime.text() == "":
                self.time()
        except ValueError:
            self.label.setText("Fill in two fields with correct numbers")

    def pace(self):
        distance = self.leDistance.text()
        time = self.leTime.text()
        pace = round((float(time) / float(distance)), 2)
        minutes = int(float(pace))
        seconds = (float(pace) * 60) % 60
        self.lePace.setText("%2d.%02d" % (minutes, seconds))

    def distance(self):
        time = self.leTime.text()
        pace = self.pace_reversed()
        distance = round((float(time) / pace), 2)
        self.leDistance.setText(str(distance))

    def time(self):
        distance = self.leDistance.text()
        pace = self.pace_reversed()
        time = round((float(distance) * pace), 0)
        self.leTime.setText(str(time))

    def pace_reversed(self):
        pace = float(self.lePace.text())
        minutes = int(pace)
        seconds = (pace - minutes) * 10**4 / 60
        return float("%2d.%02d" % (minutes, seconds))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ex = UiRunningConverter()
    ex.show()
    sys.exit(app.exec())


