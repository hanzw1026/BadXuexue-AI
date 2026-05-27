# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DocumentAssistantWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_DocumentAssistantWindow(object):
    def setupUi(self, DocumentAssistantWindow):
        if not DocumentAssistantWindow.objectName():
            DocumentAssistantWindow.setObjectName(u"DocumentAssistantWindow")
        DocumentAssistantWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DocumentAssistantWindow.sizePolicy().hasHeightForWidth())
        DocumentAssistantWindow.setSizePolicy(sizePolicy)
        DocumentAssistantWindow.setMinimumSize(QSize(1366, 768))
        DocumentAssistantWindow.setMaximumSize(QSize(4096, 4096))
        self.gridLayout = QGridLayout(DocumentAssistantWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DocumentAssistantWindow)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.list_templates = QListWidget(DocumentAssistantWindow)
        self.list_templates.setObjectName(u"list_templates")

        self.verticalLayout.addWidget(self.list_templates)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 18)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(DocumentAssistantWindow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.web_template_preview = QWebEngineView(DocumentAssistantWindow)
        self.web_template_preview.setObjectName(u"web_template_preview")
        self.web_template_preview.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.web_template_preview)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 18)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(DocumentAssistantWindow)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.web_output_preview = QWebEngineView(DocumentAssistantWindow)
        self.web_output_preview.setObjectName(u"web_output_preview")
        self.web_output_preview.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.web_output_preview)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 18)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(4, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_settings = QPushButton(DocumentAssistantWindow)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_settings)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_upload_template = QPushButton(DocumentAssistantWindow)
        self.btn_upload_template.setObjectName(u"btn_upload_template")
        sizePolicy.setHeightForWidth(self.btn_upload_template.sizePolicy().hasHeightForWidth())
        self.btn_upload_template.setSizePolicy(sizePolicy)
        self.btn_upload_template.setFont(font)

        self.verticalLayout_5.addWidget(self.btn_upload_template)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_delete_template = QPushButton(DocumentAssistantWindow)
        self.btn_delete_template.setObjectName(u"btn_delete_template")
        sizePolicy.setHeightForWidth(self.btn_delete_template.sizePolicy().hasHeightForWidth())
        self.btn_delete_template.setSizePolicy(sizePolicy)
        self.btn_delete_template.setFont(font)

        self.verticalLayout_5.addWidget(self.btn_delete_template)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.edit_prompt = QTextEdit(DocumentAssistantWindow)
        self.edit_prompt.setObjectName(u"edit_prompt")

        self.horizontalLayout_2.addWidget(self.edit_prompt)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.combo_format = QComboBox(DocumentAssistantWindow)
        self.combo_format.setObjectName(u"combo_format")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_format.sizePolicy().hasHeightForWidth())
        self.combo_format.setSizePolicy(sizePolicy1)
        self.combo_format.setFont(font)

        self.verticalLayout_4.addWidget(self.combo_format)

        self.btn_clear = QPushButton(DocumentAssistantWindow)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setFont(font)

        self.verticalLayout_4.addWidget(self.btn_clear)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.btn_generate = QPushButton(DocumentAssistantWindow)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.btn_generate.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_generate)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(4, 10)
        self.horizontalLayout_2.setStretch(6, 2)
        self.horizontalLayout_2.setStretch(8, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.setStretch(0, 5)
        self.verticalLayout_6.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)


        self.retranslateUi(DocumentAssistantWindow)

        QMetaObject.connectSlotsByName(DocumentAssistantWindow)
    # setupUi

    def retranslateUi(self, DocumentAssistantWindow):
        DocumentAssistantWindow.setWindowTitle(QCoreApplication.translate("DocumentAssistantWindow", u"\u6587\u6863\u5de5\u4f5c\u52a9\u624b", None))
        self.label.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u6a21\u677f\u6587\u4ef6\u5217\u8868", None))
        self.label_2.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u6a21\u677f\u6587\u4ef6\u9884\u89c8", None))
        self.label_3.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u8f93\u51fa\u6587\u4ef6\u9884\u89c8", None))
        self.btn_settings.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u52a9\u624b\u8bbe\u7f6e", None))
        self.btn_upload_template.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u4e0a\u4f20\u6587\u6863\u6a21\u677f", None))
        self.btn_delete_template.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u5220\u9664\u9009\u4e2d\u6a21\u677f", None))
        self.btn_clear.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u6e05\u9664\u8f93\u5165\u6846\u4e2d\u7684\u5185\u5bb9", None))
        self.btn_generate.setText(QCoreApplication.translate("DocumentAssistantWindow", u"\u751f\u6210\u6587\u6863", None))
    # retranslateUi

