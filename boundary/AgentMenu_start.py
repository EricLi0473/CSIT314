from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QIcon, QColor, QFont

from boundary.AgentMenu import *
from AdminMenu_Dialog_AddUser_start import DialogAddUser
from AdminMenu_Dialog_UpdateUser_start import DialogUpdateUser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog, QVBoxLayout, QScrollArea, QLabel

from qfluentwidgetspro import ContentDashboardCardWidget, SingleScoreWidget

from controller.Agent.RemovePropertyControl import RemovePropertyControl
from controller.Agent.UpdatePropertyControl import UpdatePropertyControl
from controller.Agent.ViewAllPropertyControl import ViewAllPropertyControl
from controller.Agent.ViewRatingControl import ViewRatingControl
from controller.Agent.ViewCommentControl import ViewCommentControl
from AgentMenu_Dialog_AddProperty_start import DialogAddProperty
from AgentMenu_Dialog_UpdateProperty_start import DialogUpdateProperty

"""
自定义拓展了插件包中的ContentDashboardCardWidget组件，增加了一个一组水平布局的labels，用于清晰显示房产的信息
增加了一组水平布局的button，用于编辑和删除对应房产信息卡片

"""


class ExtendedContentDashboardCardWidget(ContentDashboardCardWidget):

    # 这个信号跟agentMenu class里的addContentDashboardCardWidgets方法连接，用于编辑后刷新界面
    refreshRequested = pyqtSignal()

    # 参数是icon，title，content
    def __init__(self, icon, title, content, isChecked=True, parent=None):
        super().__init__(icon=icon, title=title, content=content, isChecked=isChecked, parent=parent)

        self.property_title = title
        self.content = content

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

        self.label_seller = QLabel("Seller: N/A")
        self.label_seller.setFont(font)
        properties_layout.addWidget(self.label_seller)

        # 创建一个水平布局，用于放置编辑和删除按钮
        buttons_layout = QHBoxLayout()

        # 添加编辑和删除按钮
        self.edit_button = QPushButton('Edit')
        self.delete_button = QPushButton('Delete')
        self.edit_button.setStyleSheet("QPushButton {"
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
        self.delete_button.setStyleSheet("QPushButton {"
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
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addWidget(self.delete_button)

        # 调整按钮大小
        self.edit_button.setFixedSize(QSize(80, 30))
        self.delete_button.setFixedSize(QSize(80, 30))

        # 连接编辑和删除按钮的点击事件到相应的槽函数
        self.edit_button.clicked.connect(self.editContent)
        self.delete_button.clicked.connect(self.deleteContent)

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
    def editContent(self):
        # 当编辑按钮被点击时调用此方法
        # 打包创建content card时传进来的当前数据
        property_data = {
            'title': self.property_title,
            'description': self.content,
            'beds': self.label_beds.text().split(": ")[1],
            'baths': self.label_baths.text().split(": ")[1],
            'size': self.label_size.text().split(": ")[1],
            'price': self.label_price.text().split(": ")[1],
            'status': self.label_status.text(),
            'seller': self.label_seller.text().split(": ")[1],
        }

        # 把打包数据传给UpdateProperty窗口，之后用于lineEdit中默认显示未编辑前的值
        update_dialog = DialogUpdateProperty(property_data=property_data, parent=self)

        # 用户点击了对话框中的确认按钮，信号是Accepted
        if update_dialog.exec_() == QtWidgets.QDialog.Accepted:
            # 获取对话框中的更新后的用户数据，UpdateProperty窗口传了如下数据回来
            newTitle, description, bedNum, bathNum, size, price, status, sellerName = update_dialog.getUpdatedProperty()

            # 调用后端的更新方法来更新用户信息
            update_control = UpdatePropertyControl()
            update_control.updatePropertry(newTitle, self.property_title, description, bedNum, bathNum, size, price,
                                           status, sellerName)

            # 更新完毕后刷新表格显示，前面的信号也跟这里连接
            self.refreshRequested.emit()



    # 删除按钮的函数
    def deleteContent(self):
        # 需要当前title参数
        property_title_to_delete = self.property_title

        remove_property_control = RemovePropertyControl()

        remove_property_control.remove_property(property_title_to_delete)

        self.setParent(None)  # 从布局中移除卡片
        self.deleteLater()  # 删除卡片对象


class AgentMenu(QMainWindow):
    def __init__(self, agent_name):
        super().__init__()
        self.ui = Ui_AgentMenu()
        self.ui.setupUi(self)

        self.agent_name = agent_name  # 获取从主窗口中传递过来的agent_name，用于显示对应agent房产

        # 自使用函数
        self.addContentDashboardCardWidgets()
        self.addRatings()
        self.addComments()

        # self.ui.TableWidget1.resizeColumnsToContents()

        # property页面中的add按钮绑定openAddPropertyDialog方法
        self.ui.btn_addProperty.clicked.connect(self.openAddPropertyDialog)

        # property页面中的SearchLine实现动态搜索，并绑定searchProperty方法
        self.ui.SearchLineEdit.textChanged.connect(self.searchProperty)

        # 给缩小化和正常化的导航栏里的每一个图标（button）绑定到stack widget里对应的页面
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

    # 根据后端方法（数据库）动态添加ContentDashboardCardWidgets组件，这里的search_text参数被search line传递
    def addContentDashboardCardWidgets(self, search_text=""):

        property_control = ViewAllPropertyControl()  # 实例化后端class

        # 调用实例化之后的后端class内的viewAllProperty方法，使用properties_data储存后端返回的房产数据
        properties_data = property_control.transferPropertiesToList(property_control.viewAllProperty(self.agent_name))

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
            if search_text.lower() in property_data[0].lower():
                found = True
                card_widget = ExtendedContentDashboardCardWidget(
                    icon=QIcon('path_to_icon.png'),
                    title=property_data[0],  # 获取title
                    content=property_data[1],  # 获取description
                    isChecked=False
                )

                # 设置自定义属性数据
                card_widget.label_beds.setText(f"Beds: {property_data[2]}")
                card_widget.label_baths.setText(f"Baths: {property_data[3]}")
                card_widget.label_size.setText(f"Size: {property_data[4]}")
                card_widget.label_price.setText(f"Price: {property_data[5]}")
                card_widget.label_status.setText(f"Status: {property_data[6]}")
                card_widget.label_views.setText(f"Views: {property_data[7]}")
                card_widget.label_seller.setText(f"Seller: {property_data[9]}")

                #刷新页面，refreshRequested信号绑定到了refreshUserList
                card_widget.refreshRequested.connect(self.refreshUserList)

                layout.addWidget(card_widget)

        if not found:  # 如果没有找到匹配的房产，可能需要处理这种情况
            label_no_result = QLabel("No properties found matching the search criteria.")
            layout.addWidget(label_no_result)

    def openAddPropertyDialog(self):
        # 创建并显示 AddUserDialog 对话框
        dialog_addProperty = DialogAddProperty(self.agent_name, self)

        dialog_addProperty.propertyAdded.connect(self.refreshUserList)

        dialog_addProperty.exec_()  # 以模态方式运行对话框

    def refreshUserList(self):

        self.addContentDashboardCardWidgets()

    def searchProperty(self):
        search_text = self.ui.SearchLineEdit.text().strip().lower()
        self.addContentDashboardCardWidgets(search_text)

    def addRatings(self):
        rating_control = ViewRatingControl()
        rating_list = rating_control.transferRatingToList(rating_control.viewRating(self.agent_name))

        self.ui.RoundListWidget.clear()

        font = QFont()
        font.setPointSize(9)
        font.setFamily("PT Root UI Bold")

        for rating in rating_list:
            username = rating[0]
            score = rating[1]

            item_text = f"{username}:\t{score}"
            # 创建一个新的列表项
            list_item = QListWidgetItem(item_text)
            # list_item.setFont(font)
            # 将列表项添加到列表中
            self.ui.RoundListWidget.addItem(list_item)

    def addComments(self):
        comment_control = ViewCommentControl()
        comment_list = comment_control.transferCommentToList(comment_control.viewComment(self.agent_name))

        self.ui.RoundListWidget_2.clear()

        font = QFont()
        font.setPointSize(9)
        font.setFamily("PT Root UI Bold")

        for comment in comment_list:
            username = comment[0]
            comment = comment[1]

            item_text = f"{username}:\t{comment}"
            # 创建一个新的列表项
            list_item = QListWidgetItem(item_text)
            # list_item.setFont(font)
            # 将列表项添加到列表中
            self.ui.RoundListWidget_2.addItem(list_item)
