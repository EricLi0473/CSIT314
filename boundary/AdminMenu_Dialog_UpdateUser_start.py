from PyQt5.QtCore import pyqtSignal

from boundary.AdminMenu_Dialog_UpdateUser import *
from controller.AdminControl import AdminControl
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog


class DialogUpdateUser(QDialog):

    # 为dialog窗口设置触发信号
    userUpdated = pyqtSignal()


    def __init__(self, parent=None):
        super(DialogUpdateUser, self).__init__(parent)
        self.ui = Ui_Dialog_UpdateUser()
        self.ui.setupUi(self)

        self.ui.ComboBox_type.addItems(["admin", "agent", "buyer", "seller"])
        self.ui.ComboBox_status.addItems(["valid", "invalid"])

        self.ui.PushButton_update.clicked.connect(self.getUpdatedData)

    # GUI窗口拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获得鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)   # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def getUpdatedData(self):
        # 收集对话框中的数据
        newUsername = self.ui.LineEdit_newName.text()
        password = self.ui.LineEdit_password.text()
        email = self.ui.LineEdit_email.text()
        type = self.ui.ComboBox_type.currentText()
        states = self.ui.ComboBox_status.currentText()

        self.userUpdated.emit()
        self.accept()

        return newUsername, password, email, type, states

