from PyQt5.QtCore import pyqtSignal

from boundary.SellerMenu_Dialog_feedback import *
from controller.User.GiveRatingToAgentControl import GiveRatingToAgentControl
from controller.User.GiveCommentToAgentControl import GiveCommentToAgentControl
from controller.Buyer.getAllAgentNameController import getAllAgentNameController
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem, QPushButton, \
    QWidget, QHBoxLayout, QDialog


class DialogFeedback(QDialog):

    # 为dialog窗口设置触发信号
    propertyAdded = pyqtSignal()


    def __init__(self, user, parent=None):
        super(DialogFeedback, self).__init__(parent)
        self.ui = Ui_BuyerMenu_Dialog_feedback()
        self.ui.setupUi(self)
        self.user = user

        self.ui.btn_score.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(0))
        self.ui.btn_review.clicked.connect(lambda: self.ui.SlideAniStackedWidget.setCurrentIndex(1))

        self.ui.btn_submit_score.clicked.connect(self.giveScore)
        self.ui.btn_submit_review.clicked.connect(self.giveReview)

        get_agent_list = getAllAgentNameController()
        agent_list = get_agent_list.getAllAgentName()

        print(agent_list)

        self.ui.ComboBox_agent.addItems(agent_list)
        self.ui.ComboBox_agent_2.addItems(agent_list)
        self.ui.ComboBox_score.addItems(["1", "2", "3", "4", "5"])
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
#todo 39
    def giveScore(self):
        score_control = GiveRatingToAgentControl()
        score = self.ui.ComboBox_score.currentText()
        agent = self.ui.ComboBox_agent_2.currentText()

        if score_control.giveRatingToAgent(self.user.userid, agent, score):
            QMessageBox.warning(self, 'Submission Result', 'Successfully submitted!')
        else:
            QMessageBox.warning(self, 'Submission Result', 'Failed to submit.')
#todo 40
    def giveReview(self):
        review_control = GiveCommentToAgentControl()
        review = self.ui.TextEdit_review.toPlainText()
        agent = self.ui.ComboBox_agent.currentText()

        if review_control.giveCommentToAgent(self.user.userid, agent, review):
            QMessageBox.warning(self, 'Submission Result', 'Successfully submitted!')
        else:
            QMessageBox.warning(self, 'Submission Result', 'Failed to submit.')
