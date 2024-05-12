from PyQt5.QtCore import pyqtSignal

from boundary.Admin.UI.AdminMenu_Dialog_AddUser import *
from controller.User.CreateUserController import CreateUserController
from PyQt5.QtWidgets import QMessageBox, QDialog


class DialogAddUser(QDialog):

    # 为dialog窗口设置触发信号
    userAdded = pyqtSignal()


    def __init__(self, parent=None):
        super(DialogAddUser, self).__init__(parent)
        self.ui = Ui_Dialog_AddUser()
        self.ui.setupUi(self)

        self.ui.ComboBox_type.addItems(["admin", "agent", "buyer", "seller"])

        self.ui.PushButton_create.clicked.connect(self.userCreate)

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
#todo 7 create user account
    def userCreate(self):
        try:
            # 获取输入框和组合框中的值
            username = self.ui.LineEdit_username.text()
            password = self.ui.LineEdit_password.text()
            email = self.ui.LineEdit_email.text()
            userType = self.ui.ComboBox_type.currentText()

            # 调用后端的 createUser 方法
            create_control = CreateUserController()
            success = create_control.createUser(username, password, email, userType)

            if success:
                QMessageBox.information(self, 'Success', f"Successful create new account")
                self.userAdded.emit()
                self.accept()  # 关闭对话框
                return True
            else:
                QMessageBox.warning(self, "Error", "Could not create user.")
                return False
        except Exception as e:
            # 打印或记录异常信息
            print(f"Failed to create user: {e}")
            QMessageBox.warning(self, "Error", f"Failed to create user: {e}")
            # 返回 False
            return False