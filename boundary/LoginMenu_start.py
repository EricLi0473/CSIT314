import qfluentwidgetspro
from qfluentwidgetspro import setLicense

from boundary.LoginMenu import *
from boundary.BuyerMenu_start import BuyerMenu
from boundary.AdminMenu_start import AdminMenu

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from controller.UserControl import UserControl


class LoginMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)

        self.userControl = UserControl()

        self.ui.pushButton_login.clicked.connect(self.login)    # 给login按钮绑定事件槽

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


    # login方法（检查用户输入的用户名和密码，是否与数据库匹配）
    def login(self):
        username = self.ui.lineEdit_username.text()
        password = self.ui.lineEdit_password.text()

        try:
            user, userType = self.userControl.checkLogin(username, password)
            if user is not None:
                self.hide()  # 登录成功，隐藏登录窗口
                if userType == 'buyer':
                    self.buyerMenu = BuyerMenu()
                    self.buyerMenu.show()  # 显示 BuyerMenu 窗口
                elif userType == 'admin':
                    self.sellerMenu = AdminMenu()
                    self.sellerMenu.show()  # 显示 SellerMenu 窗口
                else:
                    QMessageBox.warning(self, 'Error', 'User type not recognized.')
            else:
                QMessageBox.warning(self, 'Error', 'Invalid username or password.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', str(e))



if __name__ == '__main__':
    setLicense("17p+aRZcg1zLmzz5JHZbwF5MEsgrZ2v/sMCF0ZMgl7tjbDQ+iqb5oe8Gq3Bw9pGmHuJCSCx+IJMi5D5HM+a76JLvEaCtdqIRPqfnVYU78vMxV/5+euglfNOomqMr7nMUV0zg5qkg3uDd2kZtNNFLBk4L8KGWG1GRQxDEz9/7rg64pcvCO7sfhSwghandzAM5nmOJLyjISSEFHOEt4F03qrw/zChLUBJWwIUlbie7xR5Okf0HO8tNGkbhrwr7YHx5")

    app = QApplication(sys.argv)
    win = LoginMenu()
    sys.exit(app.exec_())
