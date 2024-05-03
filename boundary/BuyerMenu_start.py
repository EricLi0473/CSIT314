from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QColor, QFont

from boundary.BuyerMenu import *
from boundary.BuyerMenu_Dialog_calculation_start import DialogCalculation
from boundary.BuyerMenu_Dialog_feedback_start import DialogFeedback
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog, QVBoxLayout, QScrollArea, QLabel

from qfluentwidgetspro import ContentDashboardCardWidget, SingleScoreWidget

from controller.Buyer.ViewPropertiesController import ViewPropertiesController
from controller.Buyer.AddPropertyIntoFavoritesControl import AddPropertyIntoFavoritesControl
from controller.Buyer.calculateMonthlyPaymentControl import CalculateMonthlyPaymentControl
from controller.Buyer.ViewNewFavouritesControl import ViewNewFavouritesControl
from controller.Buyer.ViewOldFavouritesControl import ViewOldFavouritesControl
from controller.User.SearchUserController import SearchUserController
from controller.User.UpdateUserController import UpdateUserController
from entity.User import User


"""
自定义拓展了插件包中的ContentDashboardCardWidget组件，增加了一个一组水平布局的labels，用于清晰显示房产的信息
增加了一组水平布局的button，用于编辑和删除对应房产信息卡片

"""


class BuyerContentDashboardCardWidget(ContentDashboardCardWidget):

    # 这个信号跟agentMenu class里的addContentDashboardCardWidgets方法连接，用于编辑后刷新界面
    favoriteAdded = pyqtSignal()

    # 参数是icon，title，content
    def __init__(self, icon, title, content, buyer_name, isChecked=True, parent=None):
        super().__init__(icon=icon, title=title, content=content, isChecked=isChecked, parent=parent)

        self.property_title = title
        self.content = content
        self.buyer_name = buyer_name

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

        # 创建一个水平布局，用于放置编辑和删除按钮
        buttons_layout = QHBoxLayout()

        # 添加编辑和删除按钮
        self.favorite_button = QPushButton('add to Favorite')
        self.calculater_button = QPushButton('Calculater')
        self.favorite_button.setStyleSheet("QPushButton {"
                                       "min-width: 250px; "
                                       "min-height: 30px; "
                                       "background-color: black;"
                                       "color: white;"
                                       "border: none;"
                                       "border-radius: 15px;"
                                       "font-family: PT Root UI;"  # 设置字体为 Arial
                                       "font-size: 14px;"  # 设置字体大小为 14 像素
                                       "font-weight: bold;"  # 设置字体加粗
                                       "}"
                                       "QPushButton:pressed {"
                                       "padding-top: 5px;"
                                       "padding-left: 5px;"
                                       "}"
                                       )
        self.calculater_button.setStyleSheet("QPushButton {"
                                         "min-width: 250px; "
                                         "min-height: 30px; "
                                         "background-color: rgb(170, 0, 0);"
                                         "color: white;"
                                         "border: none;"
                                         "border-radius: 15px;"
                                         "font-family: PT Root UI;"  # 设置字体为 Arial
                                         "font-size: 14px;"  # 设置字体大小为 14 像素
                                         "font-weight: bold;"  # 设置字体加粗
                                         "}"
                                         "QPushButton:pressed {"
                                         "padding-top: 5px;"
                                         "padding-left: 5px;"
                                         "}"
                                         )

        # 把编辑按钮和删除按钮放入水平布局之中
        buttons_layout.addWidget(self.favorite_button)
        buttons_layout.addWidget(self.calculater_button)

        # 调整按钮大小
        self.favorite_button.setFixedSize(QSize(80, 30))
        self.calculater_button.setFixedSize(QSize(80, 30))

        # 连接编辑和删除按钮的点击事件到相应的槽函数
        self.favorite_button.clicked.connect(self.addFavorite)
        self.calculater_button.clicked.connect(self.calculation)

        # 获取当前卡片的主垂直布局
        main_layout = self.layout()

        # 如果当前卡片没有主垂直布局，创建一个新的垂直布局并设置为主布局
        if not main_layout:
            main_layout = QVBoxLayout(self)

        # 在主垂直布局中添加属性标签布局和按钮布局
        main_layout.addLayout(properties_layout)
        main_layout.addLayout(buttons_layout)

        # 设置整体的边距和组件之间的间距
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

    # 编辑按钮对应的触发函数
    def addFavorite(self):
        favorite_control = AddPropertyIntoFavoritesControl()
        if favorite_control.addpropertyIntoFavorites(self.buyer_name, self.property_title):
            QMessageBox.warning(self, 'Success', 'Success to Add property to favorite list.')
        else:
            QMessageBox.warning(self, 'fail', 'failed to Add property to favorite list.')
        self.favoriteAdded.emit()


    # 删除按钮的函数
    def calculation(self):
        price = {'price': self.label_price.text().split(": ")[1]}

        dialog_addProperty = DialogCalculation(price=price, parent=self)

        dialog_addProperty.exec_()  # 以模态方式运行对话框
        # 需要当前title参数

class BuyerFavContentDashboardCardWidget(ContentDashboardCardWidget):

    # 这个信号跟agentMenu class里的addContentDashboardCardWidgets方法连接，用于编辑后刷新界面
    ##refreshRequested = pyqtSignal()

    # 参数是icon，title，content
    def __init__(self, icon, title, content, buyer_name, isChecked=True, parent=None):
        super().__init__(icon=icon, title=title, content=content, isChecked=isChecked, parent=parent)

        self.property_title = title
        self.content = content
        self.buyer_name = buyer_name

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

        # 创建一个水平布局，用于放置编辑和删除按钮
        buttons_layout = QHBoxLayout()

        # 添加编辑和删除按钮
        self.calculater_button = QPushButton('Calculater')
        self.calculater_button.setStyleSheet("QPushButton {"
                                         "min-width: 250px; "
                                         "min-height: 30px; "
                                         "background-color: rgb(170, 0, 0);"
                                         "color: white;"
                                         "border: none;"
                                         "border-radius: 15px;"
                                         "font-family: PT Root UI;"  # 设置字体为 Arial
                                         "font-size: 14px;"  # 设置字体大小为 14 像素
                                         "font-weight: bold;"  # 设置字体加粗
                                         "}"
                                         "QPushButton:pressed {"
                                         "padding-top: 5px;"
                                         "padding-left: 5px;"
                                         "}"
                                         )

        # 把编辑按钮和删除按钮放入水平布局之中
        buttons_layout.addWidget(self.calculater_button)

        # 调整按钮大小
        self.calculater_button.setFixedSize(QSize(80, 30))

        # 连接编辑和删除按钮的点击事件到相应的槽函数
        self.calculater_button.clicked.connect(self.calculation)

        # 获取当前卡片的主垂直布局
        main_layout = self.layout()

        # 如果当前卡片没有主垂直布局，创建一个新的垂直布局并设置为主布局
        if not main_layout:
            main_layout = QVBoxLayout(self)

        # 在主垂直布局中添加属性标签布局和按钮布局
        main_layout.addLayout(properties_layout)
        main_layout.addLayout(buttons_layout)

        # 设置整体的边距和组件之间的间距
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

    # 删除按钮的函数
    def calculation(self):
        price = {'price': self.label_price.text().split(": ")[1]}

        dialog_addProperty = DialogCalculation(price=price, parent=self)

        dialog_addProperty.exec_()  # 以模态方式运行对话框
        # 需要当前title参数

class BuyerMenu(QMainWindow):
    def __init__(self, user, loginMenu):
        super().__init__()
        self.ui = Ui_BuyerMenu()
        self.ui.setupUi(self)

        self.user = user  # 获取从主窗口中传递过来的agent_name，用于显示对应agent房产

        # 与 类似AdminMenu，它是使用username（登录代理的用户名）和对LoginMenu实例的引用来初始化的。
        # 添加注销按钮，该按钮连接到实例logout的方法LoginMenu
        self.loginMenu = loginMenu
        self.ui.btn_logout.clicked.connect(self.loginMenu.logout)

        # 自使用函数
        self.viewNewAndOldProperties()
        self.viewNewPropertyFavouritesList()
        self.addOldFavContentDashboardCardWidgets()
        self.profilePage()
        # property页面中的add按钮绑定openAddPropertyDialog方法


        # property页面中的SearchLine实现动态搜索，并绑定searchProperty方法


        # 给缩小化和正常化的导航栏里的每一个图标（button）绑定到stack widget里对应的页面
        self.ui.btn_dashboard1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.btn_dashboard2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))

        self.ui.btn_property.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))
        self.ui.btn_property2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.btn_profile1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))
        self.ui.btn_profile2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(2))

        self.ui.btn_favorites1.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))
        self.ui.btn_favorites2.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))
        self.ui.btn_switch_to_new.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(3))

        self.ui.btn_switch_to_old.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(4))

        self.ui.btn_feedback.clicked.connect(self.OpenFeedbackDialog)
        self.ui.btn_update_profile.clicked.connect(self.updateInfo)


        self.ui.SearchLineEdit.textChanged.connect(self.searchPropertyAll)
        self.ui.SearchLineEdit_new.textChanged.connect(self.searchPropertyNew)
        self.ui.SearchLineEdit_old.textChanged.connect(self.searchPropertyOld)

        self.ui.icon_name_widget.setHidden(True)

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

    def refreshAllProperty(self):
        self.viewNewAndOldProperties()
        self.viewNewPropertyFavouritesList()
        self.addOldFavContentDashboardCardWidgets()
    ##def ContentDashboardCardWidgets
    def refreshFavProperty(self):
        self.viewNewPropertyFavouritesList()
        self.addOldFavContentDashboardCardWidgets()
    #35
    def searchPropertyAll(self):
        search_text = self.ui.SearchLineEdit.text().strip().lower()
        self.viewNewAndOldProperties(search_text)

    def searchPropertyNew(self):
        search_text = self.ui.SearchLineEdit_new.text().strip().lower()
        self.viewNewPropertyFavouritesList(search_text)

    def searchPropertyOld(self):
        search_text = self.ui.SearchLineEdit_old.text().strip().lower()
        self.addOldFavContentDashboardCardWidgets(search_text)
    #todo userstory:36, search both new and old property listings,将搜索和 viewAll分开
    def viewNewAndOldProperties(self, search_text=""):

        property_control = ViewPropertiesController()  # 实例化后端class

        # 调用实例化之后的后端class内的viewAllProperty方法，使用properties_data储存后端返回的房产数据
        properties_data = property_control.viewProperties()

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

        # 动态创建和添加属性卡片到 UI，默认给found绑定了一个false用于搜索
        found = False
        for property_data in properties_data:
            # 搜索时如果有任何字母时是属于title的
            if search_text.lower() in property_data.title.lower():
                found = True
                card_widget = BuyerContentDashboardCardWidget(
                    icon=QIcon('path_to_icon.png'),
                    title=property_data.title,  # 获取title
                    content=property_data.description,  # 获取description
                    buyer_name=self.user.username,
                    isChecked=False
                )

                # 设置自定义属性数据
                card_widget.label_beds.setText(f"Beds: {property_data.bedNum}")
                card_widget.label_baths.setText(f"Baths: {property_data.bathNum}")
                card_widget.label_size.setText(f"Size: {property_data.size}")
                card_widget.label_price.setText(f"Price: {property_data.price}")
                card_widget.label_status.setText(f"Status: {property_data.status}")
                card_widget.label_views.setText(f"Views: {property_data.views}")
                card_widget.label_agent.setText(f"Agents: {User().findAUser(property_data.agentId).username}")

                layout.addWidget(card_widget)

                card_widget.favoriteAdded.connect(self.refreshFavProperty)

        if not found:  # 如果没有找到匹配的房产，可能需要处理这种情况
            label_no_result = QLabel("No properties found matching the search criteria.")
            layout.addWidget(label_no_result)

    #41
    def viewNewPropertyFavouritesList(self, search_text=""):

        new_favorite_control = ViewNewFavouritesControl()  # 实例化后端class

        # 调用实例化之后的后端class内的viewAllProperty方法，使用properties_data储存后端返回的房产数据
        properties_data = new_favorite_control.viewNewFavorites(self.user.username)

        # 定位并获取对应的stacked widget中的页面位置，在这里我把他放进了page_manage中的SmoothScrollArea组件里
        # 并且用scroll_area储存位置
        scroll_area = self.ui.SlideAniStackedWidget.findChild(SmoothScrollArea, 'SmoothScrollArea_2')

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

        # 动态创建和添加属性卡片到 UI，默认给found绑定了一个false用于搜索
        found = False
        for property_data in properties_data:
            # 搜索时如果有任何字母时是属于title的
            if search_text.lower() in property_data.Title.lower():
                found = True
                card_widget = BuyerFavContentDashboardCardWidget(
                    icon=QIcon('path_to_icon.png'),
                    title=property_data.Title,  # 获取title
                    content=property_data.Description,  # 获取description
                    buyer_name=self.user.username,
                    isChecked=False
                )

                # 设置自定义属性数据
                card_widget.label_beds.setText(f"Beds: {property_data.BedNum}")
                card_widget.label_baths.setText(f"Baths: {property_data.BathNum}")
                card_widget.label_size.setText(f"Size: {property_data.Size}")
                card_widget.label_price.setText(f"Price: {property_data.Price}")
                card_widget.label_status.setText(f"Status: {property_data.Status}")
                card_widget.label_views.setText(f"Views: {property_data.Views}")
                card_widget.label_agent.setText(f"Agents: {property_data.Agentname}")

                #刷新页面，refreshRequested信号绑定到了refreshUserList

                layout.addWidget(card_widget)

        if not found:  # 如果没有找到匹配的房产，可能需要处理这种情况
            label_no_result = QLabel("No properties found matching the search criteria.")
            layout.addWidget(label_no_result)

    #42
    def addOldFavContentDashboardCardWidgets(self, search_text=""):

        old_favorite_control = ViewOldFavouritesControl()  # 实例化后端class

        # 调用实例化之后的后端class内的viewAllProperty方法，使用properties_data储存后端返回的房产数据
        properties_data = old_favorite_control.viewOldFavorites(self.user.username)


        # 定位并获取对应的stacked widget中的页面位置，在这里我把他放进了page_manage中的SmoothScrollArea组件里
        # 并且用scroll_area储存位置
        scroll_area = self.ui.SlideAniStackedWidget.findChild(SmoothScrollArea, 'SmoothScrollArea_3')

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

        # 动态创建和添加属性卡片到 UI，默认给found绑定了一个false用于搜索
        found = False
        for property_data in properties_data:
            # 搜索时如果有任何字母时是属于title的
            if search_text.lower() in property_data.Title.lower():
                found = True
                card_widget = BuyerFavContentDashboardCardWidget(
                    icon=QIcon('path_to_icon.png'),
                    title=property_data.Title,  # 获取title
                    content=property_data.Description,  # 获取description
                    buyer_name=self.user.username,
                    isChecked=False
                )

                # 设置自定义属性数据
                card_widget.label_beds.setText(f"Beds: {property_data.BedNum}")
                card_widget.label_baths.setText(f"Baths: {property_data.BathNum}")
                card_widget.label_size.setText(f"Size: {property_data.Size}")
                card_widget.label_price.setText(f"Price: {property_data.Price}")
                card_widget.label_status.setText(f"Status: {property_data.Status}")
                card_widget.label_views.setText(f"Views: {property_data.Views}")
                card_widget.label_agent.setText(f"Agents: {property_data.Agentname}")

                #刷新页面，refreshRequested信号绑定到了refreshUserList

                layout.addWidget(card_widget)

        if not found:  # 如果没有找到匹配的房产，可能需要处理这种情况
            label_no_result = QLabel("No properties found matching the search criteria.")
            layout.addWidget(label_no_result)

    def OpenFeedbackDialog(self):
        dialog_feedback = DialogFeedback(buyer_name=self.user.username)

        dialog_feedback.exec_()  # 以模态方式运行对话框

    def profilePage(self):
        get_user_info = SearchUserController()
        info_list = get_user_info.seachAUser(self.user.username)

        self.ui.Label_username.setText(info_list.username)
        self.ui.Label_password.setText(info_list.password)
        self.ui.Label_email.setText(info_list.email)
        self.ui.Label_status.setText(info_list.userStatus)

    def refreshprofilePage(self):
        self.profilePage()

    def updateInfo(self):
        newUserName = self.ui.LineEdit_newUserName.text()
        newPassword = self.ui.LineEdit_newPassword.text()
        newEmail = self.ui.LineEdit_newEmail.text()
        userType = "buyer"

        updated_info_control = UpdateUserController()
        updated_info_control.updateUser(self.user.username, newUserName, newPassword, newEmail, userType)
        self.user.username = newUserName
        self.refreshprofilePage()
        self.refreshAllProperty()
