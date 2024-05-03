from PyQt5.QtCore import pyqtSignal
from qfluentwidgetspro import setLicense

from boundary.LoginMenu import *
from boundary.AdminMenu_start import AdminMenu
from boundary.AgentMenu_start import AgentMenu
from boundary.BuyerMenu_start import BuyerMenu

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from controller.User.LoginController import LoginController
from controller.User.CreateUserController import CreateUserController


class LoginMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)

        # 引入了一个currentSession属性来跟踪当前活动的会话窗口（如AdminMenu或AgentMenu）
        # 最初，它被设置为None因为第一次启动时没有活动会话LoginMenu。
        self.currentSession = None

        self.ui.pushButton_login.clicked.connect(self.login)    # 给login按钮绑定login的方法

        # 主界面have account和sign up绑定对应切换界面
        self.ui.pushButton_account.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.pushButton_Sign.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.ComboBox_type.addItems(["admin","agent", "buyer", "seller"])    # 给注册时的combobox增加选项卡

        self.ui.pushButton_reg.clicked.connect(self.signUp)     # 给sign up界面绑定signUp的方法

        #  隐藏window窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

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

    # 改进了代码架构，把登录成功后的检查userType并打开对应窗口封装成了一个方法
    def after_login_success(self, username):
        user = self.user_login_control.findUser(username)

        # 它首先检查是否存在现有会话窗口 ( currentSession)。
        # 如果是这样，它就会隐藏它。这可确保一次仅打开一个会话窗口。
        if self.currentSession:
            self.currentSession.hide()

        # 根据用户类型 ( user_type)，它实例化AdminMenu AgentMenu并将其分配给currentSession。
        # 新实例化的会话窗口将显示给用户。
        if user.userTypeId == 1:
            #todo AdminMenu没有传user进去，我不太清楚要怎么重构
            self.adminMenu = AdminMenu(self)
            self.currentSession = self.adminMenu
            self.adminMenu.show()
        elif user.userTypeId == 2:
            self.agentMenu = AgentMenu(user, self)
            self.currentSession = self.agentMenu
            self.agentMenu.show()
        elif user.userTypeId == 4:
            self.buyerMenu = BuyerMenu(user, self)
            self.currentSession = self.buyerMenu
            self.buyerMenu.show()
        else:
            QMessageBox.warning(self, 'Error', 'User type not recognized.')

    # login方法，封装套娃
    def login(self):
        self.user_login_control = LoginController()

        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        try:
            if self.user_login_control.checkLogin(username, password):
                QMessageBox.warning(self, 'Success', f'Welcome, {username}')
                self.hide()
                self.after_login_success(username)      # 调用上面的type检查方法，套娃
            else:
                QMessageBox.warning(self, 'Error', 'Invalid username or password.')
        except Exception as e:  # Replace SpecificException with the actual exception you expect
            QMessageBox.warning(self, 'Error', str(e))


    def signUp(self):
        username = self.ui.lineEdit_username_reg.text()
        password = self.ui.lineEdit_password_reg.text()
        email = self.ui.lineEdit_email.text()
        user_type = self.ui.ComboBox_type.currentText()

        # 调用后端的 createUser 方法
        create_control = CreateUserController()
        success = create_control.createUser(username, password, email, user_type)

        if success:
            try:
                username = username
                password = password
                self.user_login_control = LoginController()

                if self.user_login_control.checkLogin(username, password):
                    self.hide()
                    self.after_login_success(username)  # 调用上面的type检查方法，套娃
                else:
                    QMessageBox.warning(self, 'Error', 'Invalid username or password.')
            except Exception as e:  # Replace SpecificException with the actual exception you expect
                QMessageBox.warning(self, 'Error', str(e))

        else:
            QMessageBox.warning(self, 'Error', 'Sign up failed. Please check your details.')

    def logout(self):
        if self.currentSession:
            self.currentSession.hide()
        self.currentSession = None
        self.show()

if __name__ == '__main__':
    setLicense(
        "17p+aRZcg1zLmzz5JHZbwF5MEsgrZ2v/sMCF0ZMgl7tjbDQ+iqb5oe8Gq3Bw9pGmHuJCSCx+IJMi5D5HM+a76JLvEaCtdqIRPqfnVYU78vMxV/5+euglfNOomqMr7nMUV0zg5qkg3uDd2kZtNNFLBk4L8KGWG1GRQxDEz9/7rg64pcvCO7sfhSwghandzAM5nmOJLyjISSEFHOEt4F03qrw/zChLUBJWwIUlbie7xR5Okf0HO8tNGkbhrwr7YHx5")

    app = QApplication(sys.argv)
    win = LoginMenu()
    sys.exit(app.exec_())
