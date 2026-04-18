# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow_V0.4.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(1366, 768))
        mainWindow.setMaximumSize(QSize(4096, 2048))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_system_info = QTextBrowser(self.centralwidget)
        self.list_system_info.setObjectName(u"list_system_info")

        self.verticalLayout.addWidget(self.list_system_info)

        self.list_history_sessions = QListWidget(self.centralwidget)
        self.list_history_sessions.setObjectName(u"list_history_sessions")

        self.verticalLayout.addWidget(self.list_history_sessions)

        self.btn_mode_sel_1 = QPushButton(self.centralwidget)
        self.btn_mode_sel_1.setObjectName(u"btn_mode_sel_1")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_1.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_1.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_1)

        self.btn_mode_sel_2 = QPushButton(self.centralwidget)
        self.btn_mode_sel_2.setObjectName(u"btn_mode_sel_2")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_2.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_2)

        self.btn_mode_sel_3 = QPushButton(self.centralwidget)
        self.btn_mode_sel_3.setObjectName(u"btn_mode_sel_3")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_3.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_3)

        self.btn_mode_sel_4 = QPushButton(self.centralwidget)
        self.btn_mode_sel_4.setObjectName(u"btn_mode_sel_4")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_4.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_4)

        self.btn_mode_sel_5 = QPushButton(self.centralwidget)
        self.btn_mode_sel_5.setObjectName(u"btn_mode_sel_5")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_5.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_5.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_5)

        self.btn_mode_sel_6 = QPushButton(self.centralwidget)
        self.btn_mode_sel_6.setObjectName(u"btn_mode_sel_6")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_6.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_6.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_6)

        self.btn_mode_sel_7 = QPushButton(self.centralwidget)
        self.btn_mode_sel_7.setObjectName(u"btn_mode_sel_7")
        sizePolicy.setHeightForWidth(self.btn_mode_sel_7.sizePolicy().hasHeightForWidth())
        self.btn_mode_sel_7.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_mode_sel_7)

        self.btn_loacl_knowledge_base = QPushButton(self.centralwidget)
        self.btn_loacl_knowledge_base.setObjectName(u"btn_loacl_knowledge_base")
        sizePolicy.setHeightForWidth(self.btn_loacl_knowledge_base.sizePolicy().hasHeightForWidth())
        self.btn_loacl_knowledge_base.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_loacl_knowledge_base)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_sys_setting = QPushButton(self.centralwidget)
        self.btn_sys_setting.setObjectName(u"btn_sys_setting")
        sizePolicy.setHeightForWidth(self.btn_sys_setting.sizePolicy().hasHeightForWidth())
        self.btn_sys_setting.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_sys_setting)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(11, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.web_chat_display = QWebEngineView(self.centralwidget)
        self.web_chat_display.setObjectName(u"web_chat_display")
        sizePolicy.setHeightForWidth(self.web_chat_display.sizePolicy().hasHeightForWidth())
        self.web_chat_display.setSizePolicy(sizePolicy)
        self.web_chat_display.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.web_chat_display)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_message_input = QTextEdit(self.centralwidget)
        self.text_message_input.setObjectName(u"text_message_input")

        self.horizontalLayout.addWidget(self.text_message_input)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_send_message = QPushButton(self.centralwidget)
        self.btn_send_message.setObjectName(u"btn_send_message")
        sizePolicy.setHeightForWidth(self.btn_send_message.sizePolicy().hasHeightForWidth())
        self.btn_send_message.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn_send_message)

        self.btn_clear_message = QPushButton(self.centralwidget)
        self.btn_clear_message.setObjectName(u"btn_clear_message")
        sizePolicy.setHeightForWidth(self.btn_clear_message.sizePolicy().hasHeightForWidth())
        self.btn_clear_message.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn_clear_message)

        self.btn_upload_file = QPushButton(self.centralwidget)
        self.btn_upload_file.setObjectName(u"btn_upload_file")
        sizePolicy.setHeightForWidth(self.btn_upload_file.sizePolicy().hasHeightForWidth())
        self.btn_upload_file.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.btn_upload_file)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 6)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 30))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u96ea\u96ea\u7684AI\u5ba2\u6237\u7aefV0.4", None))
        self.btn_mode_sel_1.setText(QCoreApplication.translate("mainWindow", u"\u65e5\u5e38\u804a\u5929", None))
        self.btn_mode_sel_2.setText(QCoreApplication.translate("mainWindow", u"\u79d1\u7814\u52a9\u7406-API\u6a21\u5f0f", None))
        self.btn_mode_sel_3.setText(QCoreApplication.translate("mainWindow", u"\u79d1\u7814\u52a9\u7406-\u8131\u654f\u6a21\u5f0f", None))
        self.btn_mode_sel_4.setText(QCoreApplication.translate("mainWindow", u"\u79d1\u7814\u52a9\u7406-\u672c\u5730\u6a21\u5f0f", None))
        self.btn_mode_sel_5.setText(QCoreApplication.translate("mainWindow", u"Coding\u6a21\u5f0f", None))
        self.btn_mode_sel_6.setText(QCoreApplication.translate("mainWindow", u"\u8c46\u5305\u6587\u6863\u751f\u6210", None))
        self.btn_mode_sel_7.setText(QCoreApplication.translate("mainWindow", u"\u6a21\u5f0f7\uff08INOP\uff09", None))
        self.btn_loacl_knowledge_base.setText(QCoreApplication.translate("mainWindow", u"\u672c\u5730\u77e5\u8bc6\u5e93", None))
        self.btn_sys_setting.setText(QCoreApplication.translate("mainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.btn_send_message.setText(QCoreApplication.translate("mainWindow", u"\u53d1\u9001\u6d88\u606f", None))
        self.btn_clear_message.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u7a7a\u5f53\u524d\u804a\u5929\u8bb0\u5f55", None))
        self.btn_upload_file.setText(QCoreApplication.translate("mainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
    # retranslateUi

