from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QFont

from boundary.Seller.UI.SellerMenu import *
from boundary.Seller.UI_Function.SellerMenu_Dialog_feedback_start import DialogFeedback
from controller.Seller.ViewPropertiesControl import ViewPropertiesControl
from controller.User.SearchUserController import SearchUserController
from controller.User.UpdateUserController import UpdateUserController
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QLabel

from qfluentwidgetspro import ContentDashboardCardWidget


class BuyerContentDashboardCardWidget(ContentDashboardCardWidget):

    # 这个信号跟agentMenu class里的addContentDashboardCardWidgets方法连接，用于编辑后刷新界面
    favoriteAdded = pyqtSignal()

    # 参数是icon，title，content
    def __init__(self, icon, property , user, isChecked=True, parent=None):
        super().__init__(icon=icon, title=property.title, content=property.description, isChecked=isChecked, parent=parent)

        # self.property_title = title
        # self.content = content
        # self.buyer_name = buyer_name
        self.property = property
        self.user = user
        # 创建水平布局放置房产属性标签
        properties_layout = QHBoxLayout()

        # 设置字体
        font = QFont("PT Root UI", 10)

        # 初始化属性标签并添加到水平布局
        self.label_beds = QLabel("Beds: N/A")
        self.label_beds.setFont(font)
        properties_layout.addWidget(self.label_beds)

        self.label_baths = QLabel("Baths: N/A")
        self.label_baths.setFont(font)
        properties_layout.addWidget(self.label_baths)

        self.label_size = QLabel("Size: N/A")
        self.label_size.setFont(font)
        properties_layout.addWidget(self.label_size)

        self.label_price = QLabel("Price: N/A")
        self.label_price.setFont(font)
        properties_layout.addWidget(self.label_price)

        self.label_status = QLabel("Status: N/A")
        self.label_status.setFont(font)
        properties_layout.addWidget(self.label_status)

        self.label_views = QLabel("Views: N/A")
        self.label_views.setFont(font)
        properties_layout.addWidget(self.label_views)

        self.label_agent = QLabel("Agent: N/A")
        self.label_agent.setFont(font)
        properties_layout.addWidget(self.label_agent)

        self.label_seller = QLabel("Seller: N/A")
        self.label_seller.setFont(font)
        properties_layout.addWidget(self.label_seller)

        # 获取当前卡片的主垂直布局
        main_layout = self.layout()

        # 如果当前卡片没有主垂直布局，创建一个新的垂直布局并设置为主布局
        if not main_layout:
            main_layout = QVBoxLayout(self)

        # 在主垂直布局中添加属性标签布局和按钮布局
        main_layout.addLayout(properties_layout)

        # 设置整体的边距和组件之间的间距
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

class SellerMenu(QMainWindow):
    def __init__(self, user, loginMenu):
        super().__init__()
        self.ui = Ui_sellerMenu()
        self.ui.setupUi(self)

        self.user = user  # 获取从主窗口中传递过来的agent_name，用于显示对应agent房产

        # 与 类似AdminMenu，它是使用username（登录代理的用户名）和对LoginMenu实例的引用来初始化的。
        # 添加注销按钮，该按钮连接到实例logout的方法LoginMenu
        self.loginMenu = loginMenu
        self.ui.btn_logout.clicked.connect(self.logout)

        # 自使用函数
        self.viewSellerProperties()
        self.accountPage()
        # property页面中的add按钮绑定openAddPropertyDialog方法
        self.ui.btn_feedback.clicked.connect(self.OpenFeedbackDialog)

        # property页面中的SearchLine实现动态搜索，并绑定searchProperty方法

        # 给缩小化和正常化的导航栏里的每一个图标（button）绑定到stack widget里对应的页面
        self.ui.btn_dashboard1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.btn_dashboard2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))

        self.ui.btn_property.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))
        self.ui.btn_property2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.btn_profile1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))
        self.ui.btn_profile2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))

        self.ui.btn_update_profile.clicked.connect(self.updateInfo)


        self.ui.icon_name_widget_2.setHidden(True)

        #  隐藏window窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获得鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

#todo 26 view all properties
    def viewSellerProperties(self):

        view_property_control = ViewPropertiesControl()  # 实例化后端class

        # 调用实例化之后的后端class内的viewAllProperty方法，使用properties_data储存后端返回的房产数据
        seller_properties = view_property_control.viewProperties(self.user.userid)
        self.showSellerProperties(seller_properties)



    def showSellerProperties(self,seller_properties):
        seller_properties = sorted(seller_properties, key=lambda x: x.shortListed + x.views, reverse=True)
        # 定位并获取对应的stacked widget中的页面位置，在这里我把他放进了page_manage中的SmoothScrollArea组件里
        # 并且用scroll_area储存位置
        scroll_area = self.ui.SlideAniStackedWidget.findChild(SmoothScrollArea, 'SmoothScrollArea')

        # scroll内部需要一个Widget组件，使用代码创建以一个widget，并且添加到scroll_area中
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        scroll_area.setWidgetResizable(True)

        # 在content_widget中创建一个垂直布局，将来用于动态添加房产卡片信息
        layout = QVBoxLayout(content_widget)
        content_widget.setLayout(layout)

        # 清除既有的 widgets，以添加最新的数据
        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)
                widget_to_remove.deleteLater()

        for property_data in seller_properties:
            card_widget = BuyerContentDashboardCardWidget(
                icon=QIcon('path_to_icon.png'),
                ##title=property_data.title,  # 获取title
                # content=property_data.description,  # 获取description
                # buyer_name=self.user.username,
                property=property_data,
                user=self.user,
                isChecked=False
            )

            # 设置自定义属性数据
            card_widget.label_beds.setText(f"Beds: {property_data.bedNum}")
            card_widget.label_baths.setText(f"Baths: {property_data.bathNum}")
            card_widget.label_size.setText(f"Size: {property_data.size}")
            card_widget.label_price.setText(f"Price: {property_data.price}")
            card_widget.label_status.setText(f"Status: {property_data.status}")
            card_widget.label_views.setText(f"Views: {property_data.views}")
            card_widget.label_agent.setText(f"Agents: {property_data.agentName}")
            card_widget.label_seller.setText(f"Seller: {property_data.sellerName}")

            layout.addWidget(card_widget)

    def refreshSellerProperties(self):
        self.viewSellerProperties()

    def OpenFeedbackDialog(self):
        dialog_feedback = DialogFeedback(self.user)

        dialog_feedback.exec_()  # 以模态方式运行对话框
#todo 24 As a buyer, I want to be able to view my account so that I can ensure my details are correct.

    def accountPage(self):
        get_user_info = SearchUserController()
        info_list = get_user_info.seachAUser(self.user.username)
        self.showAccount(info_list)

    def showAccount(self,info_list):
        self.ui.Label_username.setText(info_list.username)
        self.ui.Label_username_2.setText(info_list.username)
        self.ui.Label_Password.setText(info_list.password)
        self.ui.Label_email.setText(info_list.email)
        self.ui.Label_status.setText(info_list.userStatus)

    def refreshaccountPage(self):
        self.accountPage()

#todo 25 As a buyer, I want to be able to update my account so that I can keep my information new.
    def updateInfo(self):
        newUserName = self.ui.LineEdit_newUserName.text()
        newPassword = self.ui.LineEdit_newPassword.text()
        newEmail = self.ui.LineEdit_newEmail.text()
        userType = "seller"

        updated_info_control = UpdateUserController()
        success = updated_info_control.updateUser(self.user.username, newUserName, newPassword, newEmail, userType)
        if success:
            self.warning("success", "update successfully")
            self.user.username = newUserName
            self.refreshaccountPage()
        else:
            self.warning("fail", "update failed")

    def warning(self,windowName,windowMassage):
        QMessageBox.warning(self, windowName, windowMassage)

    def information(self, windowName, windowMassage):
        QMessageBox.information(self, windowName, windowMassage)

    def logout(self):
        reply = QMessageBox.question(self, 'log out', f" are you sure log out ？",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.loginMenu.logout()