from boundary.Buyer.UI.BuyerMenu import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout

from controller.AdminControl import AdminControl


class BuyerMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BuyerMenu()
        self.ui.setupUi(self)

        self.displayUserList()

         #  隐藏window窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        self.ui.btn_dashboard1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.btn_dashboard2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))

        self.ui.btn_properties1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))
        self.ui.btn_properties2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.btn_profile1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))
        self.ui.btn_profile2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))

        self.ui.btn_favorites1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))
        self.ui.btn_favorites2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))

        self.ui.btn_messages1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(4))
        self.ui.btn_messages2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(4))

        self.ui.icon_name_widget.setHidden(True)



        for i in range(self.ui.TableWidget1.rowCount()):
            btn_edit = QPushButton('Edit')
            btn_freeze = QPushButton('Freeze')

            # 在 lambda 中创建一个新的作用域，通过默认参数捕获当前的行号
            btn_freeze.clicked.connect(lambda checked, row=i: self.editUser(row))
            btn_edit.clicked.connect(lambda checked, row=i: self.freezeUser(row))


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


    def addButtonToTable(self, row, column, text, function):
        # 创建按钮
        button = QPushButton(text)
        button.clicked.connect(function)
        # 创建布局
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(button)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        # 在表格中设置小部件
        self.ui.TableWidget1.setCellWidget(row, column, widget)


    def displayUserList(self):
        admin_control = AdminControl()
        user_list = admin_control.viewAllUser()

        self.ui.TableWidget1.clearContents()  # Clears the contents of the table but keeps the headers
        self.ui.TableWidget1.setRowCount(len(user_list))  # Sets the number of rows based on user list length
        self.ui.TableWidget1.setColumnCount(5)  # Set number of columns (username, password, email, usertype, status)
        self.ui.TableWidget1.setHorizontalHeaderLabels(["Username", "Password", "Email", "User Type", "Status"])

        for row_index, user_info in enumerate(user_list):
            for column_index, data in enumerate(user_info):
                self.ui.TableWidget1.setItem(row_index, column_index, QTableWidgetItem(str(data)))

        self.ui.TableWidget1.viewport().update()  # Forces the table's viewport to update


        # ... (前面的代码保持不变)
        self.ui.TableWidget1.setColumnCount(7)  # 增加一列用于“操作”
        self.ui.TableWidget1.setHorizontalHeaderLabels(
            ["Username", "Password", "Email", "User Type", "Status", "Edit", "Delete"])

        for row_index, user_info in enumerate(user_list):
            # ... (填充用户数据的代码保持不变)

            # 添加编辑和删除按钮
            self.addButtonToTable(row_index, 5, "Edit", lambda row=row_index: self.editUser(row))
            self.addButtonToTable(row_index, 6, "Freeze", lambda row=row_index: self.freezeUser(row))

        self.ui.TableWidget1.viewport().update()




    def editUser(self, row):
        # 获取用户信息
        username = self.ui.TableWidget1.item(row, 0).text()
        # 执行编辑操作
        print(f"Edit user {username}")

    def freezeUser(self, row):
        # 获取用户信息
        username = self.ui.TableWidget1.item(row, 0).text()
        # 执行删除操作
        reply = QMessageBox.question(self, '确认', f"您确定要冻结用户 {username} 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            admin_control = AdminControl()
            success = admin_control.freezeUser(username)
            if success:
                QMessageBox.information(self, '成功', f"用户 {username} 已被冻结")
                # 可选：更新表格中的状态列，显示用户已被冻结
                self.ui.TableWidget1.item(row, 4).setText('invalid')
            else:
                QMessageBox.warning(self, '失败', f"用户 {username} 冻结失败")



