# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DocsSettingDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_docsSettingDialog(object):
    def setupUi(self, docsSettingDialog):
        if not docsSettingDialog.objectName():
            docsSettingDialog.setObjectName(u"docsSettingDialog")
        docsSettingDialog.resize(720, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(docsSettingDialog.sizePolicy().hasHeightForWidth())
        docsSettingDialog.setSizePolicy(sizePolicy)
        docsSettingDialog.setMinimumSize(QSize(500, 400))
        docsSettingDialog.setMaximumSize(QSize(4096, 4096))
        self.gridLayout = QGridLayout(docsSettingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(docsSettingDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(docsSettingDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.comb_provider_sel = QComboBox(docsSettingDialog)
        self.comb_provider_sel.setObjectName(u"comb_provider_sel")
        sizePolicy1.setHeightForWidth(self.comb_provider_sel.sizePolicy().hasHeightForWidth())
        self.comb_provider_sel.setSizePolicy(sizePolicy1)
        self.comb_provider_sel.setFont(font1)

        self.horizontalLayout.addWidget(self.comb_provider_sel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(docsSettingDialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comb_model_sel = QComboBox(docsSettingDialog)
        self.comb_model_sel.setObjectName(u"comb_model_sel")
        sizePolicy1.setHeightForWidth(self.comb_model_sel.sizePolicy().hasHeightForWidth())
        self.comb_model_sel.setSizePolicy(sizePolicy1)
        self.comb_model_sel.setFont(font1)

        self.horizontalLayout_4.addWidget(self.comb_model_sel)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(docsSettingDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.edit_api_key_input = QLineEdit(docsSettingDialog)
        self.edit_api_key_input.setObjectName(u"edit_api_key_input")
        sizePolicy1.setHeightForWidth(self.edit_api_key_input.sizePolicy().hasHeightForWidth())
        self.edit_api_key_input.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.edit_api_key_input)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(6, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.line = QFrame(docsSettingDialog)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setSizeIncrement(QSize(0, 0))
        self.line.setBaseSize(QSize(0, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(docsSettingDialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(docsSettingDialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.slider_temperature = QSlider(docsSettingDialog)
        self.slider_temperature.setObjectName(u"slider_temperature")
        sizePolicy1.setHeightForWidth(self.slider_temperature.sizePolicy().hasHeightForWidth())
        self.slider_temperature.setSizePolicy(sizePolicy1)
        self.slider_temperature.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_6.addWidget(self.slider_temperature)

        self.label_temp_value = QLabel(docsSettingDialog)
        self.label_temp_value.setObjectName(u"label_temp_value")
        sizePolicy1.setHeightForWidth(self.label_temp_value.sizePolicy().hasHeightForWidth())
        self.label_temp_value.setSizePolicy(sizePolicy1)
        self.label_temp_value.setFont(font1)
        self.label_temp_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_temp_value)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(docsSettingDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setBaseSize(QSize(0, 3))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(docsSettingDialog)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(docsSettingDialog)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.edit_template_dir = QLineEdit(docsSettingDialog)
        self.edit_template_dir.setObjectName(u"edit_template_dir")
        sizePolicy1.setHeightForWidth(self.edit_template_dir.sizePolicy().hasHeightForWidth())
        self.edit_template_dir.setSizePolicy(sizePolicy1)
        self.edit_template_dir.setFont(font1)
        self.edit_template_dir.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.edit_template_dir)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(docsSettingDialog)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.edit_output_dir = QLineEdit(docsSettingDialog)
        self.edit_output_dir.setObjectName(u"edit_output_dir")
        sizePolicy1.setHeightForWidth(self.edit_output_dir.sizePolicy().hasHeightForWidth())
        self.edit_output_dir.setSizePolicy(sizePolicy1)
        self.edit_output_dir.setFont(font1)
        self.edit_output_dir.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.edit_output_dir)

        self.btn_browse_output = QPushButton(docsSettingDialog)
        self.btn_browse_output.setObjectName(u"btn_browse_output")
        sizePolicy1.setHeightForWidth(self.btn_browse_output.sizePolicy().hasHeightForWidth())
        self.btn_browse_output.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.btn_browse_output)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 5)
        self.horizontalLayout_9.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_9 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_cancel = QPushButton(docsSettingDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.btn_cancel)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.btn_saveSettings = QPushButton(docsSettingDialog)
        self.btn_saveSettings.setObjectName(u"btn_saveSettings")
        sizePolicy.setHeightForWidth(self.btn_saveSettings.sizePolicy().hasHeightForWidth())
        self.btn_saveSettings.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.btn_saveSettings)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(2, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalLayout_4.setStretch(0, 4)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout_4.setStretch(4, 3)
        self.verticalLayout_4.setStretch(6, 1)

        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(docsSettingDialog)

        QMetaObject.connectSlotsByName(docsSettingDialog)
    # setupUi

    def retranslateUi(self, docsSettingDialog):
        docsSettingDialog.setWindowTitle(QCoreApplication.translate("docsSettingDialog", u"\u6587\u6863\u52a9\u624b\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("docsSettingDialog", u"API\u914d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("docsSettingDialog", u"\u670d\u52a1\u5546\u9009\u62e9\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("docsSettingDialog", u"\u6a21\u578b\u9009\u62e9\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("docsSettingDialog", u"API KEY\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("docsSettingDialog", u"\u751f\u6210\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("docsSettingDialog", u"\u968f\u673a\u6027\u63a7\u5236\uff1a", None))
        self.label_temp_value.setText(QCoreApplication.translate("docsSettingDialog", u"0.0", None))
        self.label_7.setText(QCoreApplication.translate("docsSettingDialog", u"\u8def\u5f84\u8bbe\u7f6e ", None))
        self.label_9.setText(QCoreApplication.translate("docsSettingDialog", u"\u9ed8\u8ba4\u6a21\u677f\u6587\u4ef6\u5939\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("docsSettingDialog", u"\u5f53\u524d\u8f93\u51fa\u6587\u4ef6\u5939\uff1a", None))
        self.btn_browse_output.setText(QCoreApplication.translate("docsSettingDialog", u"\u6d4f\u89c8", None))
        self.btn_cancel.setText(QCoreApplication.translate("docsSettingDialog", u"\u53d6\u6d88", None))
        self.btn_saveSettings.setText(QCoreApplication.translate("docsSettingDialog", u"\u786e\u5b9a", None))
    # retranslateUi

