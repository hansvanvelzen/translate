# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Mon Jan 29 10:33:06 2007
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(QtCore.QSize(QtCore.QRect(0,0,400,300).size()).expandedTo(Form.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(Form)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.tblTM = QtGui.QTableWidget(Form)
        self.tblTM.setObjectName("tblTM")
        self.gridlayout.addWidget(self.tblTM,0,0,1,1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def tr(self, string):
        return QtGui.QApplication.translate("Form", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, Form):
        Form.setWindowTitle(self.tr("Lookup"))
        self.tblTM.setRowCount(0)
        self.tblTM.setColumnCount(2)
        self.tblTM.clear()
        self.tblTM.setColumnCount(2)
        self.tblTM.setRowCount(0)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
