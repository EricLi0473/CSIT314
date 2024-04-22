from PyQt5.QtCore import pyqtSignal

from boundary.AgentMenu_Dialog_UpdateProperty import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog


class DialogUpdateProperty(QDialog):

    # 为dialog窗口设置触发信号
    propertyUpdated = pyqtSignal()


    def __init__(self, parent=None):
        super(DialogUpdateProperty, self).__init__(parent)
        self.ui = Ui_Dialog_UpdateProperty()
        self.ui.setupUi(self)

        self.ui.ComboBox_status.addItems(["available", "sold"])

        self.ui.PushButton_update.clicked.connect(self.getUpdatedProperty)

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

    def getUpdatedProperty(self):
        # 收集对话框中的数据
        newTitle = self.ui.LineEdit_title.text()
        description = self.ui.LineEdit_des.text()
        bedNum = self.ui.LineEdit_bed.text()
        bathNum = self.ui.LineEdit_bath.text()
        size = self.ui.LineEdit_size.text()
        price = self.ui.LineEdit_price.text()
        status = self.ui.ComboBox_status.currentText()
        sellerName = self.ui.LineEdit_seller.text()

        self.propertyUpdated.emit()
        self.accept()

        return newTitle, description, bedNum, bathNum, size, price, status, sellerName