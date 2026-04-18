# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KnowledgeBaseDialogV2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(4096, 2048))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.list_local_file = QListWidget(Dialog)
        self.list_local_file.setObjectName(u"list_local_file")

        self.verticalLayout_2.addWidget(self.list_local_file)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_rebuild_base_index = QPushButton(Dialog)
        self.btn_rebuild_base_index.setObjectName(u"btn_rebuild_base_index")
        sizePolicy.setHeightForWidth(self.btn_rebuild_base_index.sizePolicy().hasHeightForWidth())
        self.btn_rebuild_base_index.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_rebuild_base_index)

        self.btn_import_file = QPushButton(Dialog)
        self.btn_import_file.setObjectName(u"btn_import_file")
        sizePolicy.setHeightForWidth(self.btn_import_file.sizePolicy().hasHeightForWidth())
        self.btn_import_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.btn_import_file)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_delete_all_file = QPushButton(Dialog)
        self.btn_delete_all_file.setObjectName(u"btn_delete_all_file")
        sizePolicy.setHeightForWidth(self.btn_delete_all_file.sizePolicy().hasHeightForWidth())
        self.btn_delete_all_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btn_delete_all_file)

        self.btn_delete_slected_file = QPushButton(Dialog)
        self.btn_delete_slected_file.setObjectName(u"btn_delete_slected_file")
        sizePolicy.setHeightForWidth(self.btn_delete_slected_file.sizePolicy().hasHeightForWidth())
        self.btn_delete_slected_file.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btn_delete_slected_file)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_setting_knowledgebase = QPushButton(Dialog)
        self.btn_setting_knowledgebase.setObjectName(u"btn_setting_knowledgebase")
        sizePolicy.setHeightForWidth(self.btn_setting_knowledgebase.sizePolicy().hasHeightForWidth())
        self.btn_setting_knowledgebase.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_setting_knowledgebase)

        self.btn_close_window = QPushButton(Dialog)
        self.btn_close_window.setObjectName(u"btn_close_window")
        sizePolicy.setHeightForWidth(self.btn_close_window.sizePolicy().hasHeightForWidth())
        self.btn_close_window.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_close_window)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(1, 3)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u672c\u5730\u77e5\u8bc6\u5e93", None))
        self.btn_rebuild_base_index.setText(QCoreApplication.translate("Dialog", u"\u91cd\u5efa\u77e5\u8bc6\u5e93\u7d22\u5f15", None))
        self.btn_import_file.setText(QCoreApplication.translate("Dialog", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.btn_delete_all_file.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a\u77e5\u8bc6\u5e93", None))
        self.btn_delete_slected_file.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u9009\u4e2d\u7684\u6587\u4ef6", None))
        self.btn_setting_knowledgebase.setText(QCoreApplication.translate("Dialog", u"\u77e5\u8bc6\u5e93\u8bbe\u7f6e", None))
        self.btn_close_window.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed\u7a97\u53e3", None))
    # retranslateUi

