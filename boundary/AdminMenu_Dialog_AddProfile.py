# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminMenu_Dialog_AddProfile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AddProfile(object):
    def setupUi(self, Dialog_AddProfile):
        Dialog_AddProfile.setObjectName("Dialog_AddProfile")
        Dialog_AddProfile.resize(346, 199)
        Dialog_AddProfile.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog_AddProfile)
        self.gridLayout.setObjectName("gridLayout")
        self.label_profile = QtWidgets.QLabel(Dialog_AddProfile)
        font = QtGui.QFont()
        font.setFamily("PT Root UI Bold")
        font.setPointSize(12)
        self.label_profile.setFont(font)
        self.label_profile.setObjectName("label_profile")
        self.gridLayout.addWidget(self.label_profile, 0, 0, 1, 1)
        self.LineEdit_profile = LineEdit(Dialog_AddProfile)
        self.LineEdit_profile.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 2px 3px 2px 8px;\n"
"}\n"
"\n"
"LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
"    background-color: rgba(249, 249, 249, 0.5);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 100);\n"
"}\n"
"\n"
"LineEdit:focus {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"    background-color: white;\n"
"}\n"
"\n"
"TextEdit:focus,\n"
"PlainTextEdit:focus {\n"
"    border-bottom: 1px solid #009faa;\n"
"    background-color: white;\n"
"}\n"
"\n"
"LineEdit:disabled, TextEdit:disabled,\n"
"PlainTextEdit:disabled {\n"
"    color: rgba(0, 0, 0, 150);\n"
"    background-color: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 13);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 13);\n"
"}\n"
"\n"
"#lineEditButton {\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"#lineEditButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#lineEditButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"")
        self.LineEdit_profile.setObjectName("LineEdit_profile")
        self.gridLayout.addWidget(self.LineEdit_profile, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PushButton_create = FilledPushButton(Dialog_AddProfile)
        self.PushButton_create.setStyleSheet("OutlinedPushButtonBase,\n"
"OutlinedToolButtonBase {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    padding: 6px 10px 6px 10px;\n"
"    color: black;\n"
"    outline: none;\n"
"}\n"
"\n"
"OutlinedToolButtonBase {\n"
"    padding: 8px 9px 9px 8px;\n"
"}\n"
"\n"
"OutlinedPushButtonBase:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"}\n"
"\n"
"OutlinedPushButtonBase:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"}\n"
"\n"
"OutlinedPushButtonBase[hasIcon=false] {\n"
"    padding: 6px 10px 6px 10px;\n"
"}\n"
"\n"
"OutlinedPushButtonBase[hasIcon=true] {\n"
"    padding: 6px 10px 6px 26px;\n"
"}\n"
"\n"
"OutlinedPushButtonBase:checked {\n"
"    color: white;\n"
"}\n"
"\n"
"OutlinedPushButtonBase:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"}\n"
"\n"
"OutlinedPushButton:checked,\n"
"OutlinedPushButton:checked:pressed {\n"
"    color: #009faa;\n"
"}\n"
"\n"
"Chip[isClosable=true][hasIcon=false] {\n"
"    padding: 5px 32px 5px 10px;\n"
"}\n"
"\n"
"Chip[isClosable=true][hasIcon=true] {\n"
"    padding: 5px 32px 5px 33px;\n"
"}\n"
"\n"
"Chip[isClosable=false][hasIcon=false] {\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"Chip[isClosable=false][hasIcon=true] {\n"
"    padding: 5px 10px 5px 33px;\n"
"}\n"
"\n"
"FilledPushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"FilledPushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"FilledPushButton {\n"
"    color: white;\n"
"}\n"
"\n"
"FilledToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"FilledPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 0.786);\n"
"}\n"
"\n"
"FilledPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 0.36);\n"
"}\n"
"\n"
"TextPushButton {\n"
"    color: black;\n"
"    background: transparent;\n"
"    border-radius: 5px;\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"    border: none;\n"
"}\n"
"\n"
"TextPushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"TextPushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"TextPushButton[level=\"Error\"] {\n"
"    color: #cf1010;\n"
"}\n"
"\n"
"TextPushButton[level=\"Warning\"] {\n"
"    color: #875101;\n"
"}\n"
"\n"
"TextPushButton[level=\"Success\"] {\n"
"    color: #026f02;\n"
"}\n"
"\n"
"TextPushButton[level=\"Attension\"] {\n"
"    color: #009faa;\n"
"}\n"
"\n"
"TextPushButton:hover{\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"TextPushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"}\n"
"\n"
"TextPushButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"Tag[hasIcon=false] {\n"
"    padding: 5px 8px 5px 8px;\n"
"}\n"
"\n"
"Tag[hasIcon=true] {\n"
"    padding: 5px 8px 5px 31px;\n"
"}\n"
"\n"
"RoundPushButton[hasIcon=false] {\n"
"    padding: 7px 24px 7px 24px;\n"
"}\n"
"\n"
"RoundPushButton[hasIcon=true] {\n"
"    padding: 7px 16px 7px 33px;\n"
"}")
        self.PushButton_create.setObjectName("PushButton_create")
        self.horizontalLayout.addWidget(self.PushButton_create)
        self.PushButton_cancel = PushButton(Dialog_AddProfile)
        self.PushButton_cancel.setObjectName("PushButton_cancel")
        self.horizontalLayout.addWidget(self.PushButton_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(Dialog_AddProfile)
        self.PushButton_cancel.clicked.connect(Dialog_AddProfile.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddProfile)

    def retranslateUi(self, Dialog_AddProfile):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddProfile.setWindowTitle(_translate("Dialog_AddProfile", "Dialog"))
        self.label_profile.setText(_translate("Dialog_AddProfile", "new profile name"))
        self.PushButton_create.setText(_translate("Dialog_AddProfile", "Create user"))
        self.PushButton_cancel.setText(_translate("Dialog_AddProfile", "Cancel"))
from qfluentwidgets import LineEdit, PushButton
from qfluentwidgetspro import FilledPushButton