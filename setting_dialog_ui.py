# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFontComboBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_SettingDialog(object):
    def setupUi(self, SettingDialog):
        if not SettingDialog.objectName():
            SettingDialog.setObjectName(u"SettingDialog")
        SettingDialog.resize(732, 744)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingDialog.sizePolicy().hasHeightForWidth())
        SettingDialog.setSizePolicy(sizePolicy)
        SettingDialog.setMinimumSize(QSize(320, 320))
        SettingDialog.setMaximumSize(QSize(4096, 4096))
        self.gridLayout = QGridLayout(SettingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_setting = QTabWidget(SettingDialog)
        self.tab_setting.setObjectName(u"tab_setting")
        self.tab_setting.setMinimumSize(QSize(0, 0))
        self.tab_setting.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setPointSize(16)
        self.tab_setting.setFont(font)
        self.tab_setting.setIconSize(QSize(16, 16))
        self.tab_api_setting = QWidget()
        self.tab_api_setting.setObjectName(u"tab_api_setting")
        sizePolicy.setHeightForWidth(self.tab_api_setting.sizePolicy().hasHeightForWidth())
        self.tab_api_setting.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.tab_api_setting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_api_setting)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.edit_chat_api_key = QLineEdit(self.tab_api_setting)
        self.edit_chat_api_key.setObjectName(u"edit_chat_api_key")
        sizePolicy.setHeightForWidth(self.edit_chat_api_key.sizePolicy().hasHeightForWidth())
        self.edit_chat_api_key.setSizePolicy(sizePolicy)
        self.edit_chat_api_key.setFont(font)

        self.horizontalLayout_2.addWidget(self.edit_chat_api_key)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_api_setting)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.edit_chat_api_url = QLineEdit(self.tab_api_setting)
        self.edit_chat_api_url.setObjectName(u"edit_chat_api_url")
        sizePolicy.setHeightForWidth(self.edit_chat_api_url.sizePolicy().hasHeightForWidth())
        self.edit_chat_api_url.setSizePolicy(sizePolicy)
        self.edit_chat_api_url.setFont(font)

        self.horizontalLayout_4.addWidget(self.edit_chat_api_url)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab_api_setting)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.edit_research_api_key = QLineEdit(self.tab_api_setting)
        self.edit_research_api_key.setObjectName(u"edit_research_api_key")
        sizePolicy.setHeightForWidth(self.edit_research_api_key.sizePolicy().hasHeightForWidth())
        self.edit_research_api_key.setSizePolicy(sizePolicy)
        self.edit_research_api_key.setFont(font)

        self.horizontalLayout_3.addWidget(self.edit_research_api_key)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab_api_setting)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.edit_research_api_url = QLineEdit(self.tab_api_setting)
        self.edit_research_api_url.setObjectName(u"edit_research_api_url")
        sizePolicy.setHeightForWidth(self.edit_research_api_url.sizePolicy().hasHeightForWidth())
        self.edit_research_api_url.setSizePolicy(sizePolicy)
        self.edit_research_api_url.setFont(font)

        self.horizontalLayout_5.addWidget(self.edit_research_api_url)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.tab_api_setting)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.edit_document_api_key = QLineEdit(self.tab_api_setting)
        self.edit_document_api_key.setObjectName(u"edit_document_api_key")
        sizePolicy.setHeightForWidth(self.edit_document_api_key.sizePolicy().hasHeightForWidth())
        self.edit_document_api_key.setSizePolicy(sizePolicy)
        self.edit_document_api_key.setFont(font)

        self.horizontalLayout_6.addWidget(self.edit_document_api_key)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.tab_api_setting)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.edit_document_api_url = QLineEdit(self.tab_api_setting)
        self.edit_document_api_url.setObjectName(u"edit_document_api_url")
        sizePolicy.setHeightForWidth(self.edit_document_api_url.sizePolicy().hasHeightForWidth())
        self.edit_document_api_url.setSizePolicy(sizePolicy)
        self.edit_document_api_url.setFont(font)

        self.horizontalLayout_7.addWidget(self.edit_document_api_url)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.tab_api_setting)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.edit_local_api_url = QLineEdit(self.tab_api_setting)
        self.edit_local_api_url.setObjectName(u"edit_local_api_url")
        sizePolicy.setHeightForWidth(self.edit_local_api_url.sizePolicy().hasHeightForWidth())
        self.edit_local_api_url.setSizePolicy(sizePolicy)
        self.edit_local_api_url.setFont(font)

        self.horizontalLayout_8.addWidget(self.edit_local_api_url)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.tab_api_setting)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.edit_local_model = QLineEdit(self.tab_api_setting)
        self.edit_local_model.setObjectName(u"edit_local_model")
        sizePolicy.setHeightForWidth(self.edit_local_model.sizePolicy().hasHeightForWidth())
        self.edit_local_model.setSizePolicy(sizePolicy)
        self.edit_local_model.setFont(font)

        self.horizontalLayout_9.addWidget(self.edit_local_model)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.verticalLayout_2.setStretch(6, 2)
        self.verticalLayout_2.setStretch(7, 2)
        self.verticalLayout_2.setStretch(9, 2)
        self.verticalLayout_2.setStretch(10, 2)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab_api_setting, "")
        self.tab_chat_setting = QWidget()
        self.tab_chat_setting.setObjectName(u"tab_chat_setting")
        sizePolicy.setHeightForWidth(self.tab_chat_setting.sizePolicy().hasHeightForWidth())
        self.tab_chat_setting.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.tab_chat_setting)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.tab_chat_setting)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.edit_chat_user_prefix = QLineEdit(self.tab_chat_setting)
        self.edit_chat_user_prefix.setObjectName(u"edit_chat_user_prefix")
        sizePolicy.setHeightForWidth(self.edit_chat_user_prefix.sizePolicy().hasHeightForWidth())
        self.edit_chat_user_prefix.setSizePolicy(sizePolicy)
        self.edit_chat_user_prefix.setFont(font)

        self.horizontalLayout_10.addWidget(self.edit_chat_user_prefix)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.tab_chat_setting)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)
        self.label_12.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.combo_chat_user_font = QFontComboBox(self.tab_chat_setting)
        self.combo_chat_user_font.setObjectName(u"combo_chat_user_font")
        sizePolicy.setHeightForWidth(self.combo_chat_user_font.sizePolicy().hasHeightForWidth())
        self.combo_chat_user_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.combo_chat_user_font)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.tab_chat_setting)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFont(font)
        self.label_13.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.combo_chat_user_size = QComboBox(self.tab_chat_setting)
        self.combo_chat_user_size.setObjectName(u"combo_chat_user_size")
        sizePolicy.setHeightForWidth(self.combo_chat_user_size.sizePolicy().hasHeightForWidth())
        self.combo_chat_user_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.combo_chat_user_size)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.tab_chat_setting)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font)
        self.label_14.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_14)

        self.btn_chat_user_color = QPushButton(self.tab_chat_setting)
        self.btn_chat_user_color.setObjectName(u"btn_chat_user_color")
        sizePolicy.setHeightForWidth(self.btn_chat_user_color.sizePolicy().hasHeightForWidth())
        self.btn_chat_user_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.btn_chat_user_color)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.tab_chat_setting)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)
        self.label_10.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.edit_chat_assistant_prefix = QLineEdit(self.tab_chat_setting)
        self.edit_chat_assistant_prefix.setObjectName(u"edit_chat_assistant_prefix")
        sizePolicy.setHeightForWidth(self.edit_chat_assistant_prefix.sizePolicy().hasHeightForWidth())
        self.edit_chat_assistant_prefix.setSizePolicy(sizePolicy)
        self.edit_chat_assistant_prefix.setFont(font)

        self.horizontalLayout_11.addWidget(self.edit_chat_assistant_prefix)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.tab_chat_setting)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)
        self.label_11.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.edit_chat_assistant_prompt = QLineEdit(self.tab_chat_setting)
        self.edit_chat_assistant_prompt.setObjectName(u"edit_chat_assistant_prompt")
        sizePolicy.setHeightForWidth(self.edit_chat_assistant_prompt.sizePolicy().hasHeightForWidth())
        self.edit_chat_assistant_prompt.setSizePolicy(sizePolicy)
        self.edit_chat_assistant_prompt.setFont(font)

        self.horizontalLayout_12.addWidget(self.edit_chat_assistant_prompt)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_17 = QLabel(self.tab_chat_setting)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFont(font)
        self.label_17.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.combo_chat_assisant_font = QFontComboBox(self.tab_chat_setting)
        self.combo_chat_assisant_font.setObjectName(u"combo_chat_assisant_font")
        sizePolicy.setHeightForWidth(self.combo_chat_assisant_font.sizePolicy().hasHeightForWidth())
        self.combo_chat_assisant_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.combo_chat_assisant_font)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.tab_chat_setting)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFont(font)
        self.label_16.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.combo_chat_assistant_size = QComboBox(self.tab_chat_setting)
        self.combo_chat_assistant_size.setObjectName(u"combo_chat_assistant_size")
        sizePolicy.setHeightForWidth(self.combo_chat_assistant_size.sizePolicy().hasHeightForWidth())
        self.combo_chat_assistant_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.combo_chat_assistant_size)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.tab_chat_setting)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFont(font)
        self.label_15.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.btn_chat_assisant_color = QPushButton(self.tab_chat_setting)
        self.btn_chat_assisant_color.setObjectName(u"btn_chat_assisant_color")
        sizePolicy.setHeightForWidth(self.btn_chat_assisant_color.sizePolicy().hasHeightForWidth())
        self.btn_chat_assisant_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.btn_chat_assisant_color)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.verticalLayout_3.setStretch(6, 1)
        self.verticalLayout_3.setStretch(7, 1)
        self.verticalLayout_3.setStretch(8, 1)
        self.verticalLayout_3.setStretch(9, 1)

        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab_chat_setting, "")
        self.tab_research_setting = QWidget()
        self.tab_research_setting.setObjectName(u"tab_research_setting")
        sizePolicy.setHeightForWidth(self.tab_research_setting.sizePolicy().hasHeightForWidth())
        self.tab_research_setting.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.tab_research_setting)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_18 = QLabel(self.tab_research_setting)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font)
        self.label_18.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_18)

        self.edit_research_user_prefix = QLineEdit(self.tab_research_setting)
        self.edit_research_user_prefix.setObjectName(u"edit_research_user_prefix")
        sizePolicy.setHeightForWidth(self.edit_research_user_prefix.sizePolicy().hasHeightForWidth())
        self.edit_research_user_prefix.setSizePolicy(sizePolicy)
        self.edit_research_user_prefix.setFont(font)

        self.horizontalLayout_19.addWidget(self.edit_research_user_prefix)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.tab_research_setting)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setFont(font)
        self.label_19.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_19)

        self.combo_research_user_font = QFontComboBox(self.tab_research_setting)
        self.combo_research_user_font.setObjectName(u"combo_research_user_font")
        sizePolicy.setHeightForWidth(self.combo_research_user_font.sizePolicy().hasHeightForWidth())
        self.combo_research_user_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.combo_research_user_font)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.tab_research_setting)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font)
        self.label_20.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_20)

        self.combo_research_user_size = QComboBox(self.tab_research_setting)
        self.combo_research_user_size.setObjectName(u"combo_research_user_size")
        sizePolicy.setHeightForWidth(self.combo_research_user_size.sizePolicy().hasHeightForWidth())
        self.combo_research_user_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.combo_research_user_size)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.tab_research_setting)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setFont(font)
        self.label_21.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_21)

        self.btn_research_user_color = QPushButton(self.tab_research_setting)
        self.btn_research_user_color.setObjectName(u"btn_research_user_color")
        sizePolicy.setHeightForWidth(self.btn_research_user_color.sizePolicy().hasHeightForWidth())
        self.btn_research_user_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.btn_research_user_color)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.tab_research_setting)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setFont(font)
        self.label_22.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_22)

        self.edit_research_assistant_prefix = QLineEdit(self.tab_research_setting)
        self.edit_research_assistant_prefix.setObjectName(u"edit_research_assistant_prefix")
        sizePolicy.setHeightForWidth(self.edit_research_assistant_prefix.sizePolicy().hasHeightForWidth())
        self.edit_research_assistant_prefix.setSizePolicy(sizePolicy)
        self.edit_research_assistant_prefix.setFont(font)

        self.horizontalLayout_23.addWidget(self.edit_research_assistant_prefix)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_23 = QLabel(self.tab_research_setting)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setFont(font)
        self.label_23.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_23)

        self.edit_research_assistant_prompt = QLineEdit(self.tab_research_setting)
        self.edit_research_assistant_prompt.setObjectName(u"edit_research_assistant_prompt")
        sizePolicy.setHeightForWidth(self.edit_research_assistant_prompt.sizePolicy().hasHeightForWidth())
        self.edit_research_assistant_prompt.setSizePolicy(sizePolicy)
        self.edit_research_assistant_prompt.setFont(font)

        self.horizontalLayout_24.addWidget(self.edit_research_assistant_prompt)

        self.horizontalLayout_24.setStretch(0, 1)
        self.horizontalLayout_24.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.tab_research_setting)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setFont(font)
        self.label_24.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_24)

        self.edit_research_assistant_font = QFontComboBox(self.tab_research_setting)
        self.edit_research_assistant_font.setObjectName(u"edit_research_assistant_font")
        sizePolicy.setHeightForWidth(self.edit_research_assistant_font.sizePolicy().hasHeightForWidth())
        self.edit_research_assistant_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_25.addWidget(self.edit_research_assistant_font)

        self.horizontalLayout_25.setStretch(0, 1)
        self.horizontalLayout_25.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_25 = QLabel(self.tab_research_setting)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setFont(font)
        self.label_25.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_25)

        self.edit_research_assistant_size = QComboBox(self.tab_research_setting)
        self.edit_research_assistant_size.setObjectName(u"edit_research_assistant_size")
        sizePolicy.setHeightForWidth(self.edit_research_assistant_size.sizePolicy().hasHeightForWidth())
        self.edit_research_assistant_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_26.addWidget(self.edit_research_assistant_size)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_26 = QLabel(self.tab_research_setting)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font)
        self.label_26.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_26)

        self.btn_research_assisant_color = QPushButton(self.tab_research_setting)
        self.btn_research_assisant_color.setObjectName(u"btn_research_assisant_color")
        sizePolicy.setHeightForWidth(self.btn_research_assisant_color.sizePolicy().hasHeightForWidth())
        self.btn_research_assisant_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_27.addWidget(self.btn_research_assisant_color)

        self.horizontalLayout_27.setStretch(0, 1)
        self.horizontalLayout_27.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(5, 1)
        self.verticalLayout_4.setStretch(6, 1)
        self.verticalLayout_4.setStretch(7, 1)
        self.verticalLayout_4.setStretch(8, 1)
        self.verticalLayout_4.setStretch(9, 1)

        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab_research_setting, "")
        self.tab_code_setting = QWidget()
        self.tab_code_setting.setObjectName(u"tab_code_setting")
        sizePolicy.setHeightForWidth(self.tab_code_setting.sizePolicy().hasHeightForWidth())
        self.tab_code_setting.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.tab_code_setting)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_27 = QLabel(self.tab_code_setting)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setFont(font)
        self.label_27.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_27)

        self.edit_code_user_prefix = QLineEdit(self.tab_code_setting)
        self.edit_code_user_prefix.setObjectName(u"edit_code_user_prefix")
        sizePolicy.setHeightForWidth(self.edit_code_user_prefix.sizePolicy().hasHeightForWidth())
        self.edit_code_user_prefix.setSizePolicy(sizePolicy)
        self.edit_code_user_prefix.setFont(font)

        self.horizontalLayout_28.addWidget(self.edit_code_user_prefix)

        self.horizontalLayout_28.setStretch(0, 1)
        self.horizontalLayout_28.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_28 = QLabel(self.tab_code_setting)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setFont(font)
        self.label_28.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_28)

        self.edit_code_user_font = QFontComboBox(self.tab_code_setting)
        self.edit_code_user_font.setObjectName(u"edit_code_user_font")
        sizePolicy.setHeightForWidth(self.edit_code_user_font.sizePolicy().hasHeightForWidth())
        self.edit_code_user_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_29.addWidget(self.edit_code_user_font)

        self.horizontalLayout_29.setStretch(0, 1)
        self.horizontalLayout_29.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_29 = QLabel(self.tab_code_setting)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setFont(font)
        self.label_29.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_29)

        self.combo_code_user_size = QComboBox(self.tab_code_setting)
        self.combo_code_user_size.setObjectName(u"combo_code_user_size")
        sizePolicy.setHeightForWidth(self.combo_code_user_size.sizePolicy().hasHeightForWidth())
        self.combo_code_user_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_30.addWidget(self.combo_code_user_size)

        self.horizontalLayout_30.setStretch(0, 1)
        self.horizontalLayout_30.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_30 = QLabel(self.tab_code_setting)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setFont(font)
        self.label_30.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_30)

        self.btn_code_user_color = QPushButton(self.tab_code_setting)
        self.btn_code_user_color.setObjectName(u"btn_code_user_color")
        sizePolicy.setHeightForWidth(self.btn_code_user_color.sizePolicy().hasHeightForWidth())
        self.btn_code_user_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_31.addWidget(self.btn_code_user_color)

        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.tab_code_setting)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setFont(font)
        self.label_31.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.edit_code_assistant_prefix = QLineEdit(self.tab_code_setting)
        self.edit_code_assistant_prefix.setObjectName(u"edit_code_assistant_prefix")
        sizePolicy.setHeightForWidth(self.edit_code_assistant_prefix.sizePolicy().hasHeightForWidth())
        self.edit_code_assistant_prefix.setSizePolicy(sizePolicy)
        self.edit_code_assistant_prefix.setFont(font)

        self.horizontalLayout_32.addWidget(self.edit_code_assistant_prefix)

        self.horizontalLayout_32.setStretch(0, 1)
        self.horizontalLayout_32.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_32 = QLabel(self.tab_code_setting)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setFont(font)
        self.label_32.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_32)

        self.edit_code_assistant_prompt = QLineEdit(self.tab_code_setting)
        self.edit_code_assistant_prompt.setObjectName(u"edit_code_assistant_prompt")
        sizePolicy.setHeightForWidth(self.edit_code_assistant_prompt.sizePolicy().hasHeightForWidth())
        self.edit_code_assistant_prompt.setSizePolicy(sizePolicy)
        self.edit_code_assistant_prompt.setFont(font)

        self.horizontalLayout_33.addWidget(self.edit_code_assistant_prompt)

        self.horizontalLayout_33.setStretch(0, 1)
        self.horizontalLayout_33.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_33 = QLabel(self.tab_code_setting)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setFont(font)
        self.label_33.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_33)

        self.edit_code_assistant_font = QFontComboBox(self.tab_code_setting)
        self.edit_code_assistant_font.setObjectName(u"edit_code_assistant_font")
        sizePolicy.setHeightForWidth(self.edit_code_assistant_font.sizePolicy().hasHeightForWidth())
        self.edit_code_assistant_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.edit_code_assistant_font)

        self.horizontalLayout_34.setStretch(0, 1)
        self.horizontalLayout_34.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_34 = QLabel(self.tab_code_setting)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setFont(font)
        self.label_34.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_34)

        self.edit_code_assistant_size = QComboBox(self.tab_code_setting)
        self.edit_code_assistant_size.setObjectName(u"edit_code_assistant_size")
        sizePolicy.setHeightForWidth(self.edit_code_assistant_size.sizePolicy().hasHeightForWidth())
        self.edit_code_assistant_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_35.addWidget(self.edit_code_assistant_size)

        self.horizontalLayout_35.setStretch(0, 1)
        self.horizontalLayout_35.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_35 = QLabel(self.tab_code_setting)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setFont(font)
        self.label_35.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_35)

        self.btn_code_assisant_color = QPushButton(self.tab_code_setting)
        self.btn_code_assisant_color.setObjectName(u"btn_code_assisant_color")
        sizePolicy.setHeightForWidth(self.btn_code_assisant_color.sizePolicy().hasHeightForWidth())
        self.btn_code_assisant_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_36.addWidget(self.btn_code_assisant_color)

        self.horizontalLayout_36.setStretch(0, 1)
        self.horizontalLayout_36.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_36)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.verticalLayout_5.setStretch(6, 1)
        self.verticalLayout_5.setStretch(7, 1)
        self.verticalLayout_5.setStretch(8, 1)
        self.verticalLayout_5.setStretch(9, 1)

        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab_code_setting, "")
        self.tab_document_setting = QWidget()
        self.tab_document_setting.setObjectName(u"tab_document_setting")
        sizePolicy.setHeightForWidth(self.tab_document_setting.sizePolicy().hasHeightForWidth())
        self.tab_document_setting.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.tab_document_setting)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_36 = QLabel(self.tab_document_setting)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setFont(font)
        self.label_36.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_36)

        self.edit_document_user_prefix = QLineEdit(self.tab_document_setting)
        self.edit_document_user_prefix.setObjectName(u"edit_document_user_prefix")
        sizePolicy.setHeightForWidth(self.edit_document_user_prefix.sizePolicy().hasHeightForWidth())
        self.edit_document_user_prefix.setSizePolicy(sizePolicy)
        self.edit_document_user_prefix.setFont(font)

        self.horizontalLayout_37.addWidget(self.edit_document_user_prefix)

        self.horizontalLayout_37.setStretch(0, 1)
        self.horizontalLayout_37.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_37 = QLabel(self.tab_document_setting)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setFont(font)
        self.label_37.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_37)

        self.combo_document_user_font = QFontComboBox(self.tab_document_setting)
        self.combo_document_user_font.setObjectName(u"combo_document_user_font")
        sizePolicy.setHeightForWidth(self.combo_document_user_font.sizePolicy().hasHeightForWidth())
        self.combo_document_user_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_38.addWidget(self.combo_document_user_font)

        self.horizontalLayout_38.setStretch(0, 1)
        self.horizontalLayout_38.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_38 = QLabel(self.tab_document_setting)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setFont(font)
        self.label_38.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_38)

        self.combo_document_user_size = QComboBox(self.tab_document_setting)
        self.combo_document_user_size.setObjectName(u"combo_document_user_size")
        sizePolicy.setHeightForWidth(self.combo_document_user_size.sizePolicy().hasHeightForWidth())
        self.combo_document_user_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_39.addWidget(self.combo_document_user_size)

        self.horizontalLayout_39.setStretch(0, 1)
        self.horizontalLayout_39.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_39 = QLabel(self.tab_document_setting)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setFont(font)
        self.label_39.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_39)

        self.btn_document_user_color = QPushButton(self.tab_document_setting)
        self.btn_document_user_color.setObjectName(u"btn_document_user_color")
        sizePolicy.setHeightForWidth(self.btn_document_user_color.sizePolicy().hasHeightForWidth())
        self.btn_document_user_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_40.addWidget(self.btn_document_user_color)

        self.horizontalLayout_40.setStretch(0, 1)
        self.horizontalLayout_40.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_40)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_40 = QLabel(self.tab_document_setting)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setFont(font)
        self.label_40.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_40)

        self.edit_document_assistant_prefix = QLineEdit(self.tab_document_setting)
        self.edit_document_assistant_prefix.setObjectName(u"edit_document_assistant_prefix")
        sizePolicy.setHeightForWidth(self.edit_document_assistant_prefix.sizePolicy().hasHeightForWidth())
        self.edit_document_assistant_prefix.setSizePolicy(sizePolicy)
        self.edit_document_assistant_prefix.setFont(font)

        self.horizontalLayout_41.addWidget(self.edit_document_assistant_prefix)

        self.horizontalLayout_41.setStretch(0, 1)
        self.horizontalLayout_41.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_41 = QLabel(self.tab_document_setting)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setFont(font)
        self.label_41.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_41)

        self.edit_document_assistant_prompt = QLineEdit(self.tab_document_setting)
        self.edit_document_assistant_prompt.setObjectName(u"edit_document_assistant_prompt")
        sizePolicy.setHeightForWidth(self.edit_document_assistant_prompt.sizePolicy().hasHeightForWidth())
        self.edit_document_assistant_prompt.setSizePolicy(sizePolicy)
        self.edit_document_assistant_prompt.setFont(font)

        self.horizontalLayout_42.addWidget(self.edit_document_assistant_prompt)

        self.horizontalLayout_42.setStretch(0, 1)
        self.horizontalLayout_42.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_42 = QLabel(self.tab_document_setting)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setFont(font)
        self.label_42.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.label_42)

        self.edit_document_assistant_font = QFontComboBox(self.tab_document_setting)
        self.edit_document_assistant_font.setObjectName(u"edit_document_assistant_font")
        sizePolicy.setHeightForWidth(self.edit_document_assistant_font.sizePolicy().hasHeightForWidth())
        self.edit_document_assistant_font.setSizePolicy(sizePolicy)

        self.horizontalLayout_43.addWidget(self.edit_document_assistant_font)

        self.horizontalLayout_43.setStretch(0, 1)
        self.horizontalLayout_43.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_43 = QLabel(self.tab_document_setting)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setFont(font)
        self.label_43.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_43)

        self.edit_document_assistant_size = QComboBox(self.tab_document_setting)
        self.edit_document_assistant_size.setObjectName(u"edit_document_assistant_size")
        sizePolicy.setHeightForWidth(self.edit_document_assistant_size.sizePolicy().hasHeightForWidth())
        self.edit_document_assistant_size.setSizePolicy(sizePolicy)

        self.horizontalLayout_44.addWidget(self.edit_document_assistant_size)

        self.horizontalLayout_44.setStretch(0, 1)
        self.horizontalLayout_44.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_44 = QLabel(self.tab_document_setting)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setFont(font)
        self.label_44.setInputMethodHints(Qt.InputMethodHint.ImhHiddenText|Qt.InputMethodHint.ImhLowercaseOnly|Qt.InputMethodHint.ImhNoTextHandles|Qt.InputMethodHint.ImhPreferLowercase|Qt.InputMethodHint.ImhPreferNumbers|Qt.InputMethodHint.ImhUppercaseOnly)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.label_44)

        self.btn_document_assisant_color = QPushButton(self.tab_document_setting)
        self.btn_document_assisant_color.setObjectName(u"btn_document_assisant_color")
        sizePolicy.setHeightForWidth(self.btn_document_assisant_color.sizePolicy().hasHeightForWidth())
        self.btn_document_assisant_color.setSizePolicy(sizePolicy)

        self.horizontalLayout_45.addWidget(self.btn_document_assisant_color)

        self.horizontalLayout_45.setStretch(0, 1)
        self.horizontalLayout_45.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_45)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 1)
        self.verticalLayout_6.setStretch(5, 1)
        self.verticalLayout_6.setStretch(6, 1)
        self.verticalLayout_6.setStretch(7, 1)
        self.verticalLayout_6.setStretch(8, 1)
        self.verticalLayout_6.setStretch(9, 1)

        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab_document_setting, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_9 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.btn_export_setting = QPushButton(self.tab)
        self.btn_export_setting.setObjectName(u"btn_export_setting")
        sizePolicy.setHeightForWidth(self.btn_export_setting.sizePolicy().hasHeightForWidth())
        self.btn_export_setting.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.btn_export_setting)

        self.btn_import_chat_history = QPushButton(self.tab)
        self.btn_import_chat_history.setObjectName(u"btn_import_chat_history")
        sizePolicy.setHeightForWidth(self.btn_import_chat_history.sizePolicy().hasHeightForWidth())
        self.btn_import_chat_history.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.btn_import_chat_history)

        self.btn_import_setting = QPushButton(self.tab)
        self.btn_import_setting.setObjectName(u"btn_import_setting")
        sizePolicy.setHeightForWidth(self.btn_import_setting.sizePolicy().hasHeightForWidth())
        self.btn_import_setting.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.btn_import_setting)

        self.btn_export_chat_history = QPushButton(self.tab)
        self.btn_export_chat_history.setObjectName(u"btn_export_chat_history")
        sizePolicy.setHeightForWidth(self.btn_export_chat_history.sizePolicy().hasHeightForWidth())
        self.btn_export_chat_history.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.btn_export_chat_history)

        self.verticalSpacer_8 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_8)

        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 1)
        self.verticalLayout_7.setStretch(4, 1)

        self.horizontalLayout_46.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_46.setStretch(1, 1)

        self.gridLayout_7.addLayout(self.horizontalLayout_46, 0, 0, 1, 1)

        self.tab_setting.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tab_setting)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_default_setting = QPushButton(SettingDialog)
        self.btn_default_setting.setObjectName(u"btn_default_setting")
        sizePolicy.setHeightForWidth(self.btn_default_setting.sizePolicy().hasHeightForWidth())
        self.btn_default_setting.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_default_setting)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_apply_setting = QPushButton(SettingDialog)
        self.btn_apply_setting.setObjectName(u"btn_apply_setting")
        sizePolicy.setHeightForWidth(self.btn_apply_setting.sizePolicy().hasHeightForWidth())
        self.btn_apply_setting.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_apply_setting)

        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_close_setting = QPushButton(SettingDialog)
        self.btn_close_setting.setObjectName(u"btn_close_setting")
        sizePolicy.setHeightForWidth(self.btn_close_setting.sizePolicy().hasHeightForWidth())
        self.btn_close_setting.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_close_setting)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SettingDialog)

        self.tab_setting.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingDialog)
    # setupUi

    def retranslateUi(self, SettingDialog):
        SettingDialog.setWindowTitle(QCoreApplication.translate("SettingDialog", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u6a21\u5f0fAPI Key:", None))
        self.label_4.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u6a21\u5f0fAPI URL\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624bAPI Key\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624bAPI URL\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624bAPI key\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624bAPI URL\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("SettingDialog", u"\u672c\u5730\u6a21\u5f0fURL\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("SettingDialog", u"\u672c\u5730\u6a21\u578b\uff1a", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab_api_setting), QCoreApplication.translate("SettingDialog", u"API\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u6635\u79f0\uff1a", None))
        self.edit_chat_user_prefix.setText("")
        self.label_12.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_chat_user_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.label_10.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u5bf9\u8c61\u7684\u6635\u79f0\uff1a", None))
        self.edit_chat_assistant_prefix.setText("")
        self.label_11.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u5bf9\u8c61\u7684\u4eba\u8bbe\uff1a", None))
        self.edit_chat_assistant_prompt.setText("")
        self.label_17.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u5bf9\u8c61\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u5bf9\u8c61\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u5bf9\u8c61\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_chat_assisant_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab_chat_setting), QCoreApplication.translate("SettingDialog", u"\u804a\u5929\u8bbe\u7f6e", None))
        self.label_18.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u6635\u79f0\uff1a", None))
        self.edit_research_user_prefix.setText("")
        self.label_19.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_research_user_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.label_22.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b\u7684\u6635\u79f0\uff1a", None))
        self.edit_research_assistant_prefix.setText("")
        self.label_23.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b\u7684\u4eba\u8bbe\uff1a", None))
        self.edit_research_assistant_prompt.setText("")
        self.label_24.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_research_assisant_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab_research_setting), QCoreApplication.translate("SettingDialog", u"\u79d1\u7814\u52a9\u624b", None))
        self.label_27.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u6635\u79f0\uff1a", None))
        self.edit_code_user_prefix.setText("")
        self.label_28.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_29.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_30.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_code_user_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.label_31.setText(QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b\u7684\u6635\u79f0\uff1a", None))
        self.edit_code_assistant_prefix.setText("")
        self.label_32.setText(QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b\u7684\u4eba\u8bbe\uff1a", None))
        self.edit_code_assistant_prompt.setText("")
        self.label_33.setText(QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_34.setText(QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_35.setText(QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_code_assisant_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab_code_setting), QCoreApplication.translate("SettingDialog", u"\u4ee3\u7801\u52a9\u624b", None))
        self.label_36.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u6635\u79f0\uff1a", None))
        self.edit_document_user_prefix.setText("")
        self.label_37.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_38.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_39.setText(QCoreApplication.translate("SettingDialog", u"\u7528\u6237\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_document_user_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.label_40.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b\u7684\u6635\u79f0\uff1a", None))
        self.edit_document_assistant_prefix.setText("")
        self.label_41.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b\u7684\u4eba\u8bbe\uff1a", None))
        self.edit_document_assistant_prompt.setText("")
        self.label_42.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b\u7684\u5b57\u4f53\u6837\u5f0f\uff1a", None))
        self.label_43.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b\u7684\u5b57\u4f53\u5927\u5c0f\uff1a", None))
        self.label_44.setText(QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b\u7684\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.btn_document_assisant_color.setText(QCoreApplication.translate("SettingDialog", u"\u5f53\u524d\u989c\u8272", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab_document_setting), QCoreApplication.translate("SettingDialog", u"\u6587\u6863\u52a9\u624b", None))
        self.btn_export_setting.setText(QCoreApplication.translate("SettingDialog", u"\u5bfc\u51fa\u8bbe\u7f6e\u6587\u4ef6", None))
        self.btn_import_chat_history.setText(QCoreApplication.translate("SettingDialog", u"\u5bfc\u5165\u804a\u5929\u8bb0\u5f55", None))
        self.btn_import_setting.setText(QCoreApplication.translate("SettingDialog", u"\u5bfc\u5165\u8bbe\u7f6e\u6587\u4ef6", None))
        self.btn_export_chat_history.setText(QCoreApplication.translate("SettingDialog", u"\u5bfc\u51fa\u804a\u5929\u8bb0\u5f55", None))
        self.tab_setting.setTabText(self.tab_setting.indexOf(self.tab), QCoreApplication.translate("SettingDialog", u"\u5bfc\u5165\u5bfc\u51fa", None))
        self.btn_default_setting.setText(QCoreApplication.translate("SettingDialog", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.btn_apply_setting.setText(QCoreApplication.translate("SettingDialog", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.btn_close_setting.setText(QCoreApplication.translate("SettingDialog", u"\u5173\u95ed\u8bbe\u7f6e\u7a97\u53e3", None))
    # retranslateUi

