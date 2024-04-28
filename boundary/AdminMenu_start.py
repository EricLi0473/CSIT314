from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont

from boundary.AdminMenu import *
from AdminMenu_Dialog_AddUser_start import DialogAddUser
from AdminMenu_Dialog_UpdateUser_start import DialogUpdateUser
from AdminMenu_Dialog_AddProfile_start import DialogAddProfile
from AdminMenu_Dialog_UpdatedProfile_start import DialogUpdateProfile
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog, QLabel

from controller.Admin.FreezeUserController import FreezeUserController
from controller.Admin.ActivateUserController import ActivateUserController
from controller.User.UpdateUserController import UpdateUserController
from controller.Admin.ViewProfilesController import ViewProfilesController
from controller.Admin.ViewUsersController import ViewUserController
from controller.Admin.UpdateProfileController import UpdateProfileController
from controller.Admin.SearchProfileController import SearchUserController

class ProfileListItem(QWidget):

    requestRefresh = pyqtSignal()
    def __init__(self, text, parent=None):
        super(ProfileListItem, self).__init__(parent)
        layout = QHBoxLayout(self)

        self.text_label = QLabel(text)
        font = QFont()
        font.setPointSize(9)  # Set the font size
        font.setFamily("PT Root UI")  # Set the font family
        self.text_label.setFont(font)
        self.text_label.setStyleSheet("background-color: transparent;")  # Set the background to transparent

        self.edit_button = QPushButton("Edit")

        self.edit_button.setStyleSheet("""
                        QPushButton {
                            background-color: #0078D7; /* 背景色 */
                            color: white; /* 文字颜色 */
                            border-radius: 5px; /* 边框圆角 */
                            padding: 5px; /* 内边距 */
                            margin: 2px; /* 外边距 */
                            border: none; /* 无边框 */
                            font-family: 'PT Root UI', PT root UI bold; /* 字体 */
                        }
                        QPushButton:hover {
                            background-color: #005A9E; /* 鼠标悬停时的背景色 */
                        }
                        QPushButton:pressed {
                            background-color: #003A6C; /* 鼠标按下时的背景色 */
                        }
                    """)


        self.edit_button.clicked.connect(self.editProfile)

        layout.addWidget(self.text_label)
        layout.addWidget(self.edit_button)

        # Adjust the margins and spacing as needed
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

    def editProfile(self):
        oldProfilename = self.text_label.text()

        update_dialog = DialogUpdateProfile()

        if update_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # 用户点击了对话框中的确认按钮，信号是Accepted
            newProfileName = update_dialog.getUpdatedData()

            print(oldProfilename, newProfileName)

            # 调用后端的更新方法来更新用户信息
            if UpdateProfileController().updateProfile(oldProfilename, newProfileName):
                QMessageBox.information(self, 'Success', f"Successful update")
                self.requestRefresh.emit()
            else:
                QMessageBox.warning(self, 'Failed', f"Update failure")
            # 更新完毕后刷新表格显示




class AdminMenu(QMainWindow):
    def __init__(self, loginMenu):
        super().__init__()
        self.ui = Ui_AdminMenu()
        self.ui.setupUi(self)

        # 实例化后，它会收到对实例的引用LoginMenu( loginMenu)。
        # 创建一个注销按钮，并将其clicked信号连接到实例logout的方法LoginMenu。
        self.loginMenu = loginMenu
        self.ui.btn_log_out.clicked.connect(self.loginMenu.logout)


        # 自运行下列方法
        self.displayUserList()
        self.viewProfile()

        #  隐藏window窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

        # 给缩小化和正常化的导航栏里的每一个图标（button）绑定到stack weidget里对应的页面
        self.ui.btn_dashboard1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.btn_dashboard2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))

        self.ui.btn_manage.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))
        self.ui.btn_manage2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.btn_profile1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))
        self.ui.btn_profile2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))

        self.ui.btn_favorites1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))
        self.ui.btn_favorites2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))

        self.ui.btn_messages1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(4))
        self.ui.btn_messages2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(4))

        # 给user mange和profile manage中的add按钮绑定对应的触发窗口
        self.ui.btn_addUser.clicked.connect(self.openAddUserDialog)
        self.ui.btn_addProfile1.clicked.connect(self.openAddProfileDialog)

        # 给user mange的搜索栏绑定实时搜索方法
        self.ui.SearchLineEdit.textChanged.connect(self.filterUsers)

        #  隐藏window窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        # 开启窗口时默认隐藏缩小化的导航栏
        self.ui.icon_name_widget.setHidden(True)


        # 给user_info_table_widget里的动态添加的3种button（edit,freeze，activate)
        # 编辑button的显示名称
        # 绑定对应的触发function(editUser, freezeUser, activate)
        # 使用lambda默认参数捕获动态添加时当前的行号（重点注意：lambda checked）
        for i in range(self.ui.TableWidget1.rowCount()):
            btn_edit = QPushButton('Edit')
            btn_freeze = QPushButton('Freeze')
            btn_activate = QPushButton('activate')

            # 在 lambda 中创建一个新的作用域，通过默认参数捕获当前的行号
            btn_freeze.clicked.connect(lambda checked, row=i: self.editUser(row))
            btn_edit.clicked.connect(lambda checked, row=i: self.freezeUser(row))
            btn_activate.clicked.connect(lambda checked, row=i: self.activate(row))

        for column in range(self.ui.TableWidget1.columnCount()):
            self.ui.TableWidget1.resizeColumnToContents(column)
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


    # function批量创建在user_manage_table_weight中的动态按钮
    def addButtonToTable(self, row, column, text, function):
        # 创建按钮
        button = QPushButton(text)
        button.clicked.connect(function)

        button.setStyleSheet("""
                QPushButton {
                    background-color: #0078D7; /* 背景色 */
                    color: white; /* 文字颜色 */
                    border-radius: 5px; /* 边框圆角 */
                    padding: 5px; /* 内边距 */
                    margin: 2px; /* 外边距 */
                    border: none; /* 无边框 */
                    font-family: 'PT Root UI', PT root UI bold; /* 字体 */
                }
                QPushButton:hover {
                    background-color: #005A9E; /* 鼠标悬停时的背景色 */
                }
                QPushButton:pressed {
                    background-color: #003A6C; /* 鼠标按下时的背景色 */
                }
            """)

        # 创建布局
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.addWidget(button)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        # 在表格中设置小部件
        self.ui.TableWidget1.setCellWidget(row, column, widget)


    # 批量设置动态按钮
    def setupTableButtons(self, row_index):

        # 调用addButtonToTable方法，动态添加edit按钮，并且为他们绑定点击实现editUser方法，
        # 使用lambda默认参数捕获动态添加时当前的行号（重点注意：lambda checked）
        self.addButtonToTable(row_index, 5, "Edit", lambda checked, row=row_index: self.editUser(row))

        # 调用addButtonToTable方法，动态添加freeze按钮，并且为他们绑定点击实现freezeUser方法，
        # 使用lambda默认参数捕获动态添加时当前的行号（重点注意：lambda checked）
        self.addButtonToTable(row_index, 6, "Freeze", lambda checked, row=row_index: self.freezeUser(row))

        # 调用addButtonToTable方法，动态添加Activate按钮，并且为他们绑定点击实现activateUser方法，
        # 使用lambda默认参数捕获动态添加时当前的行号（重点注意：lambda checked）
        self.addButtonToTable(row_index, 7, "Activate", lambda checked, row=row_index: self.activateUser(row))




    # 在user manage页面中的表格窗口（user_manage_table_widget)中显示数据库中user的信息
    def displayUserList(self):
        viewUser_control = ViewUserController()    # 实例化AdminControl()

        # 调用ViewUserController()中的viewAllUser（）方法，获取用户信息，并添加到user_list
        user_list = viewUser_control.TransferUserToList(viewUser_control.viewAllUser())

        self.ui.TableWidget1.clearContents()        # 清除 QTableWidget 中现有的内容，但保留表头
        self.ui.TableWidget1.setRowCount(len(user_list))        # 根据用户列表的长度，设置 QTableWidget 的行数
        self.ui.TableWidget1.setColumnCount(8)          # 设置 QTableWidget 的列数为8（用户名，密码，邮箱，用户类型，状态）

        # 设置 QTableWidget 的水平表头标签
        self.ui.TableWidget1.setHorizontalHeaderLabels(
            ["Username", "Password", "Email", "User Type", "Status", "Edit", "Freeze", "Activate"])

        # 遍历用户信息列表，填充 QTableWidget 的每一行
        # 遍历单个用户信息的每一项，填充对应的单元格
        # 在指定行和列创建表格项 QTableWidgetItem，并设置其文本为用户信息数据

        for row_index, user_info in enumerate(user_list):
            for column_index, data in enumerate(user_info):
                self.ui.TableWidget1.setItem(row_index, column_index, QTableWidgetItem(str(data)))
                self.setupTableButtons(row_index)
        self.ui.TableWidget1.viewport().update()  # 要求 QTableWidget 的视图组件进行更新，以便显示最新的内容

    # add user窗口
    def openAddUserDialog(self):
        # 显示 AddUserDialog 对话框
        dialog_addUser = DialogAddUser(self)

        # 用户点击确认之后触发userAdded信号，信号连接refreshUserList方法刷新页面
        dialog_addUser.userAdded.connect(self.refreshUserList)

        dialog_addUser.exec_()  # 以模态方式运行对话框

    # add profile窗口
    def openAddProfileDialog(self):
        # 显示 AddProfileDialog 对话框
        dialog_addProfile = DialogAddProfile(self)

        # 用户点击确认之后触发profileAdded信号，信号连接refreshProfileList方法刷新页面
        dialog_addProfile.profileAdded.connect(self.refreshProfileList)

        dialog_addProfile.exec_()  # 以模态方式运行对话框

    # 刷新user manage表格页面
    def refreshUserList(self):
        # 清除现有数据
        self.ui.TableWidget1.clearContents()
        self.ui.TableWidget1.setRowCount(0)

        # 重新从数据库获取数据并填充到 QTableWidget
        self.displayUserList()

    # 刷新profile manage页面
    def refreshProfileList(self):
        # 清除现有数据
        self.ui.RoundListWidget.clear()

        # 重新从数据库获取数据并填充到 QTableWidget
        self.viewProfile()

    # 编辑对应用户，用row参数定位定位老数据
    def editUser(self, row):

        oldUsername = self.ui.TableWidget1.item(row, 0).text()

        update_dialog = DialogUpdateUser()

        if update_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # 用户点击了对话框中的确认按钮，信号是Accepted
            # 获取对话框中的更新后的用户数据，edit窗口会传4个数据回来
            newUsername, newPassword, newEmail, newUserType = update_dialog.getUpdatedData()

            # 调用后端的更新方法来更新用户信息
            update_control = UpdateUserController()
            success = update_control.updateUser(oldUsername, newUsername, newPassword, newEmail, newUserType)
            if success:
                QMessageBox.information(self, 'Success', f"Successful update account")
            else:
                QMessageBox.information(self, 'Error', f"Could not update account")
            # 更新完毕后刷新表格显示
            self.displayUserList()



    # function冻结用户
    def freezeUser(self, row):
        # 获取用户信息
        username = self.ui.TableWidget1.item(row, 0).text()
        # 弹出对话框，等待用户选择
        reply = QMessageBox.question(self, '确认', f"您确定要冻结用户 {username} 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 选择是的时候，调用AdminControl中的freezeUser方法
        if reply == QMessageBox.Yes:
            freeze_control = FreezeUserController()
            success = freeze_control.freezeUser(username)
            if success:
                QMessageBox.information(self, '成功', f"用户 {username} 已被冻结")
                self.ui.TableWidget1.item(row, 4).setText('invalid')  # 更新状态
            else:
                QMessageBox.warning(self, '失败', f"用户 {username} 冻结失败")


    def activateUser(self, row):
        # 获取用户信息
        username = self.ui.TableWidget1.item(row, 0).text()
        # 弹出对话框，等待用户选择
        reply = QMessageBox.question(self, '确认', f"您确定要激活用户 {username} 吗？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 选择是的时候，调用AdminControl中的activateUser方法
        if reply == QMessageBox.Yes:
            activate_user_control = ActivateUserController()
            success = activate_user_control.activateUser(username)
            if success:
                QMessageBox.information(self, '成功', f"用户 {username} 已被激活")
                self.ui.TableWidget1.item(row, 4).setText('valid')  # 更新状态
            else:
                QMessageBox.warning(self, '失败', f"用户 {username} 激活失败")

    # 搜索栏过滤用户，用户输入的text是参数
    def filterUsers(self, text):
        # 从当前用户数据中过滤用户
        self.displayFilteredUsers(text)

    # 根据用户输入的文本来过滤和显示用户信息到表格
    def displayFilteredUsers(self, filter_text):
        viewUser_control = ViewUserController()

        user_list = viewUser_control.TransferUserToList(viewUser_control.viewAllUser())        # 全部用户数据
        self.ui.TableWidget1.clearContents()            # 清除当前内容
        self.ui.TableWidget1.setRowCount(0)             # 清除当前行数

        for user_data in user_list:

            # 判断用户列表中的用户名是否包含搜索框中输入的文本（不区分大小写）
            # 如果包含，就在 QTableWidget 中添加一行并填充相应的用户数据
            if filter_text.lower() in user_data[0].lower():
                row_position = self.ui.TableWidget1.rowCount()
                self.ui.TableWidget1.insertRow(row_position)
                self.ui.TableWidget1.setItem(row_position, 0, QTableWidgetItem(user_data[0]))  # username
                self.ui.TableWidget1.setItem(row_position, 1, QTableWidgetItem(user_data[1]))  # password
                self.ui.TableWidget1.setItem(row_position, 2, QTableWidgetItem(user_data[2]))  # email
                self.ui.TableWidget1.setItem(row_position, 3, QTableWidgetItem(user_data[3]))  # userType
                self.ui.TableWidget1.setItem(row_position, 4, QTableWidgetItem(user_data[4]))  # status

                self.setupTableButtons(row_position)                                           # 添加按钮

        self.ui.TableWidget1.viewport().update()

    # profile 页面信息获取
    def viewProfile(self):
        view_profile_control = ViewProfilesController()
        profile_list = view_profile_control.TransferProfileToList(view_profile_control.viewAllProfile())

        self.ui.RoundListWidget.clear()

        for profile in profile_list:
            profile_name = profile[0]
            print(profile_name)

            # Create the custom widget for the list item
            profile_widget = ProfileListItem(profile_name)
            profile_widget.requestRefresh.connect(self.refreshProfileList)

            # Create the list item and set its widget
            list_item = QListWidgetItem(self.ui.RoundListWidget)
            list_item.setSizeHint(
                profile_widget.sizeHint())  # Ensure the list item has the right size for the custom widget

            # Finally, add the widget to the list
            self.ui.RoundListWidget.addItem(list_item)
            self.ui.RoundListWidget.setItemWidget(list_item, profile_widget)

