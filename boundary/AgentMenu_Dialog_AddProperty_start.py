from PyQt5.QtCore import pyqtSignal

from boundary.AgentMenu_Dialog_AddProperty import *
from controller.Agent.CreatePropertyControl import CreatePropertyControl
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog


class DialogAddProperty(QDialog):

    # 为dialog窗口设置触发信号
    propertyAdded = pyqtSignal()


    def __init__(self, agent_name, parent=None):
        super(DialogAddProperty, self).__init__(parent)
        self.agent_name = agent_name
        self.ui = Ui_Dialog_AddProperty()
        self.ui.setupUi(self)

        self.ui.PushButton_create.clicked.connect(self.propertyCreate)

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

    def propertyCreate(self):
        try:
            # 获取输入框和组合框中的值
            title = self.ui.LineEdit_title.text()
            description = self.ui.LineEdit_des.text()
            bedrooms = self.ui.LineEdit_bed.text()
            bathrooms = self.ui.LineEdit_bath.text()
            size = self.ui.LineEdit_size.text()
            price = self.ui.LineEdit_price.text()
            seller = self.ui.LineEdit_seller.text()

            # 调用后端的 createUser 方法
            create_control = CreatePropertyControl()
            print(self.agent_name,title,description,bedrooms,bathrooms,size,price,seller)
            success = create_control.createProperty(self.agent_name, title, description, bedrooms, bathrooms
                                                    , size, price, seller)

            if success:
                QMessageBox.information(self, 'Success', f"Successful create property")
                self.propertyAdded.emit()
                self.accept()  # 关闭对话框
                return True
            else:
                QMessageBox.warning(self, "Error", "Could not create property.")
                return False
        except Exception as e:
            # 打印或记录异常信息
            print(f"Failed to create user: {e}")
            QMessageBox.warning(self, "Error", f"Failed to create user: {e}")
            # 返回 False
            return False