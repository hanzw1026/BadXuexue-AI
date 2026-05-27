# -*- coding: utf-8 -*-
"""
文档助手设置对话框
"""

import os
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QSettings
from docsSettingDialogCode import Ui_docsSettingDialog
from init_config import (
    ensure_doc_assistant_config_exists,
    load_doc_assistant_config,
    save_doc_assistant_config
)
import platform


def get_platform_default_font_size():
    system = platform.system()
    if system == "Windows":
        return 11
    elif system == "Darwin":
        return 13
    else:
        return 12


DEFAULT_FONT_SIZE = get_platform_default_font_size()


class DocsSettingDialog(QDialog):
    """文档助手设置对话框"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # 创建 UI 实例并设置界面
        self.ui = Ui_docsSettingDialog()
        self.ui.setupUi(self)
        # ===== 设置整个对话框的默认字体 =====
        from PySide6.QtGui import QFont
        import platform

        def get_font_size():
            if platform.system() == "Windows":
                return 11
            else:
                return 13

        font = QFont()
        font.setPointSize(get_font_size())
        self.setFont(font)

        self.setModal(True)
        self.setWindowTitle("文档助手设置")

        # 确保配置文件存在
        ensure_doc_assistant_config_exists()

        # 初始化界面组件
        self._init_ui()

        # 绑定信号槽
        self._init_signals()

        # 加载已保存的设置
        self.load_settings()

    def _init_ui(self):
        """初始化界面组件"""
        # 覆盖 UI 文件中硬编码的字体大小
        from PySide6.QtGui import QFont
        import platform

        def get_font_size():
            if platform.system() == "Windows":
                return 11
            else:
                return 13

        base_font = QFont()
        base_font.setPointSize(get_font_size())

        # 覆盖标题字体（原 20 号）
        title_font = QFont()
        title_font.setPointSize(get_font_size() + 2)  # 标题可以稍大一点
        self.ui.label.setFont(title_font)

        # 覆盖其他控件的字体
        for widget in [self.ui.label_2, self.ui.label_4, self.ui.label_3,
                       self.ui.label_6, self.ui.label_9, self.ui.label_8,
                       self.ui.comb_provider_sel, self.ui.comb_model_sel,
                       self.ui.edit_api_key_input, self.ui.edit_template_dir,
                       self.ui.edit_output_dir, self.ui.label_temp_value]:
            widget.setFont(base_font)

        # 覆盖 UI 文件中硬编码的标题字体（20pt → 使用默认大小）
        base_font = QFont()
        base_font.setPointSize(DEFAULT_FONT_SIZE)

        self.ui.label.setFont(base_font)  # API配置
        self.ui.label_5.setFont(base_font)  # 生成设置
        self.ui.label_7.setFont(base_font)  # 路径设置

        # 服务商下拉选项
        self.ui.comb_provider_sel.addItems([
            "通义千问 (Qwen)",
            "豆包 (Doubao)",
            "DeepSeek"
        ])

        # 初始化模型下拉选项（默认根据当前服务商）
        self._update_model_options()

        # 温度滑块
        self.ui.slider_temperature.setRange(0, 100)
        self.ui.slider_temperature.setValue(70)
        self.ui.label_temp_value.setText("0.7")

        # 模板目录（只读）
        self.ui.edit_template_dir.setReadOnly(True)
        self.ui.edit_template_dir.setText("./docs_template")

        # 输出目录
        self.ui.edit_output_dir.setText("./outputs")

        # API Key 输入框（密码模式）
        # 正确写法
        from PySide6.QtWidgets import QLineEdit
        self.ui.edit_api_key_input.setEchoMode(QLineEdit.EchoMode.Password)

    def _init_signals(self):
        """绑定信号槽"""
        self.ui.slider_temperature.valueChanged.connect(self._on_temperature_changed)
        self.ui.comb_provider_sel.currentIndexChanged.connect(self._update_model_options)
        self.ui.btn_browse_output.clicked.connect(self._browse_output_dir)
        self.ui.btn_saveSettings.clicked.connect(self.save_and_close)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def _update_model_options(self):
        """根据服务商更新模型下拉选项"""
        self.ui.comb_model_sel.clear()

        provider = self.ui.comb_provider_sel.currentText()

        if "千问" in provider:
            self.ui.comb_model_sel.addItems([
                "qwen-max", "qwen-plus", "qwen-turbo", "qwen-long"
            ])
            self.ui.comb_model_sel.setCurrentText("qwen-max")
        elif "豆包" in provider:
            self.ui.comb_model_sel.addItems([
                "doubao-pro-32k", "doubao-lite-32k"
            ])
            self.ui.comb_model_sel.setCurrentIndex(0)
        else:  # DeepSeek
            self.ui.comb_model_sel.addItems([
                "deepseek-chat", "deepseek-coder"
            ])
            self.ui.comb_model_sel.setCurrentIndex(0)

    def _on_temperature_changed(self, value):
        """温度滑块值变化"""
        temp_value = value / 100.0
        self.ui.label_temp_value.setText(f"{temp_value:.1f}")

    def _browse_output_dir(self):
        """浏览并选择输出目录"""
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "选择输出目录",
            self.ui.edit_output_dir.text()
        )
        if dir_path:
            self.ui.edit_output_dir.setText(dir_path)

    def load_settings(self):
        """从 .env 文件加载设置"""
        config = load_doc_assistant_config()

        # 服务商
        provider_map = {"qwen": 0, "doubao": 1, "deepseek": 2}
        provider_idx = provider_map.get(config.get("provider", "qwen"), 0)
        if provider_idx < self.ui.comb_provider_sel.count():
            self.ui.comb_provider_sel.setCurrentIndex(provider_idx)

        # API Key
        api_key = config.get("api_key", "")
        if api_key:
            self.ui.edit_api_key_input.setText(api_key)

        # 模型
        model = config.get("model", "qwen-max")
        idx = self.ui.comb_model_sel.findText(model)
        if idx >= 0:
            self.ui.comb_model_sel.setCurrentIndex(idx)

        # 温度
        temp = config.get("temperature", 0.7)
        self.ui.slider_temperature.setValue(int(temp * 100))

        # 目录
        output_dir = config.get("output_dir", "./outputs")
        self.ui.edit_output_dir.setText(output_dir)
        self.ui.edit_template_dir.setText(config.get("template_dir", "./docs_template"))

    def save_settings(self):
        """保存设置到 .env 文件"""
        config = {
            "provider": self._get_provider_key(),
            "api_key": self.ui.edit_api_key_input.text().strip(),
            "model": self.ui.comb_model_sel.currentText(),
            "temperature": self.ui.slider_temperature.value() / 100.0,
            "output_dir": self.ui.edit_output_dir.text(),
            "template_dir": self.ui.edit_template_dir.text()
        }
        save_doc_assistant_config(config)
        return True

    def _get_provider_key(self):
        """获取服务商的 key 值"""
        mapping = {
            "通义千问 (Qwen)": "qwen",
            "豆包 (Doubao)": "doubao",
            "DeepSeek": "deepseek"
        }
        provider_text = self.ui.comb_provider_sel.currentText()
        return mapping.get(provider_text, "qwen")

    def save_and_close(self):
        """保存设置并关闭"""
        self.save_settings()
        self.accept()

    def get_settings(self):
        """获取当前设置（供外部调用）"""
        return {
            "provider": self._get_provider_key(),
            "provider_name": self.ui.comb_provider_sel.currentText(),
            "api_key": self.ui.edit_api_key_input.text().strip(),
            "model": self.ui.comb_model_sel.currentText(),
            "temperature": self.ui.slider_temperature.value() / 100.0,
            "output_dir": self.ui.edit_output_dir.text(),
            "template_dir": self.ui.edit_template_dir.text()
        }