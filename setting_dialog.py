# setting_dialog.py
"""系统设置对话框"""

import os
import re
from PySide6.QtWidgets import QDialog, QMessageBox, QColorDialog, QFileDialog, QApplication
from PySide6.QtCore import Qt

from setting_dialog_ui import Ui_SettingDialog
import init_config


class SettingDialog(QDialog, Ui_SettingDialog):
    def __init__(self, parent=None):
        # 高DPI适配：让Qt自己控制
        if hasattr(Qt, 'AA_EnableHighDpiScaling'):
            QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
            QApplication.setAttribute(Qt.AA_DisableHighDpiScaling, True)

        super().__init__(parent)
        self.setupUi(self)
        self.color_values = {}

        self.init_font_sizes()
        self.connect_signals()

        # 加载配置到变量
        self.load_config_to_vars()

        # 窗口显示后刷新 UI
        from PySide6.QtCore import QTimer
        QTimer.singleShot(100, self.refresh_ui)

    def refresh_ui(self):
        """刷新所有 UI 控件（窗口显示后调用）"""
        from PySide6.QtGui import QFont
        from PySide6.QtCore import QTimer

        if init_config.isInTestMode:
            print("🔄 刷新设置窗口 UI...")

        # 延迟一点执行，确保控件完全准备好
        QTimer.singleShot(50, self._do_refresh_ui)

    def _refresh_font_combo(self, combo_box, target_family):
        """刷新字体下拉框，选中目标字体"""
        from PySide6.QtGui import QFont

        if not target_family:
            combo_box.setCurrentIndex(0)
            return

        # 直接创建字体并设置
        target_font = QFont(target_family)
        combo_box.setCurrentFont(target_font)

        if init_config.isInTestMode:
            current = combo_box.currentFont().family()
            if current != target_family:
                print(f"   ⚠️ 字体 '{target_family}' 未精确匹配，当前: '{current}'")

        # 如果没设置成功，手动匹配
        if combo_box.currentFont().family() != target_family:
            for i in range(combo_box.count()):
                item_text = combo_box.itemText(i)
                if target_family in item_text or item_text == target_family:
                    combo_box.setCurrentIndex(i)
                    if init_config.isInTestMode:
                        print(f"   ✅ 手动匹配字体: '{item_text}'")
                    return

    def _do_refresh_ui(self):
        """实际执行 UI 刷新"""
        from PySide6.QtGui import QFont

        # ========== 1. API 设置 ==========
        self.edit_chat_api_key.setText(self.chat_api_key)
        self.edit_research_api_key.setText(self.research_api_key)
        self.edit_document_api_key.setText(self.document_api_key)
        self.edit_chat_api_url.setText(self.chat_api_url)
        self.edit_research_api_url.setText(self.research_api_url)
        self.edit_document_api_url.setText(self.document_api_url)
        self.edit_local_api_url.setText(self.local_api_url)
        self.edit_local_model.setText(self.local_model)

        # ========== 2. 聊天模式 ==========
        self.edit_chat_user_prefix.setText(self.user_prefix_chat)
        self.edit_chat_assistant_prefix.setText(self.assistant_prefix)
        self.edit_chat_assistant_prompt.setText(self.chat_assistant_prompt)

        # 字体大小
        idx = self.combo_chat_user_size.findText(self.user_size)
        if idx >= 0:
            self.combo_chat_user_size.setCurrentIndex(idx)
        idx = self.combo_chat_assistant_size.findText(self.assistant_size)
        if idx >= 0:
            self.combo_chat_assistant_size.setCurrentIndex(idx)

        # 字体
        self._refresh_font_combo(self.combo_chat_user_font, self.user_font)
        self._refresh_font_combo(self.combo_chat_assisant_font, self.assistant_font)

        # 颜色
        self.color_values["chat_user"] = self.user_color
        self.btn_chat_user_color.setStyleSheet(f"background-color: {self.user_color};")
        self.color_values["chat_assistant"] = self.assistant_color
        self.btn_chat_assisant_color.setStyleSheet(f"background-color: {self.assistant_color};")

        # ========== 3. 科研助手模式 ==========
        self.edit_research_user_prefix.setText(self.research_user_prefix)
        self.edit_research_assistant_prefix.setText(self.research_assistant_prefix)
        self.edit_research_assistant_prompt.setText(self.research_system_prompt)

        idx = self.combo_research_user_size.findText(self.research_user_size)
        if idx >= 0:
            self.combo_research_user_size.setCurrentIndex(idx)
        idx = self.edit_research_assistant_size.findText(self.research_assistant_size)
        if idx >= 0:
            self.edit_research_assistant_size.setCurrentIndex(idx)

        self._refresh_font_combo(self.combo_research_user_font, self.research_user_font)
        self._refresh_font_combo(self.edit_research_assistant_font, self.research_assistant_font)

        self.color_values["research_user"] = self.research_user_color
        self.btn_research_user_color.setStyleSheet(f"background-color: {self.research_user_color};")
        self.color_values["research_assistant"] = self.research_assistant_color
        self.btn_research_assisant_color.setStyleSheet(f"background-color: {self.research_assistant_color};")

        # ========== 4. 代码助手模式 ==========
        self.edit_code_user_prefix.setText(self.code_user_prefix)
        self.edit_code_assistant_prefix.setText(self.code_assistant_prefix)
        self.edit_code_assistant_prompt.setText(self.code_assistant_prompt)

        idx = self.combo_code_user_size.findText(self.code_user_size)
        if idx >= 0:
            self.combo_code_user_size.setCurrentIndex(idx)
        idx = self.edit_code_assistant_size.findText(self.code_assistant_size)
        if idx >= 0:
            self.edit_code_assistant_size.setCurrentIndex(idx)

        self._refresh_font_combo(self.edit_code_user_font, self.code_user_font)
        self._refresh_font_combo(self.edit_code_assistant_font, self.code_assistant_font)

        self.color_values["code_user"] = self.code_user_color
        self.btn_code_user_color.setStyleSheet(f"background-color: {self.code_user_color};")
        self.color_values["code_assistant"] = self.code_assistant_color
        self.btn_code_assisant_color.setStyleSheet(f"background-color: {self.code_assistant_color};")

        # ========== 5. 文档助手模式 ==========
        self.edit_document_user_prefix.setText(self.document_user_prefix)
        self.edit_document_assistant_prefix.setText(self.document_assistant_prefix)
        self.edit_document_assistant_prompt.setText(self.document_assistant_prompt)

        idx = self.combo_document_user_size.findText(self.document_user_size)
        if idx >= 0:
            self.combo_document_user_size.setCurrentIndex(idx)
        idx = self.edit_document_assistant_size.findText(self.document_assistant_size)
        if idx >= 0:
            self.edit_document_assistant_size.setCurrentIndex(idx)

        self._refresh_font_combo(self.combo_document_user_font, self.document_user_font)
        self._refresh_font_combo(self.edit_document_assistant_font, self.document_assistant_font)

        self.color_values["document_user"] = self.document_user_color
        self.btn_document_user_color.setStyleSheet(f"background-color: {self.document_user_color};")
        self.color_values["document_assistant"] = self.document_assistant_color
        self.btn_document_assisant_color.setStyleSheet(f"background-color: {self.document_assistant_color};")

        if init_config.isInTestMode:
            print("✅ 设置窗口 UI 刷新完成")

    def init_font_sizes(self):
        """初始化字体大小下拉框（10-30）"""
        sizes = [str(i) for i in range(10, 31)]

        # 聊天设置页
        self.combo_chat_user_size.addItems(sizes)
        self.combo_chat_assistant_size.addItems(sizes)

        # 科研助手页
        self.combo_research_user_size.addItems(sizes)
        self.edit_research_assistant_size.addItems(sizes)

        # 代码助手页
        self.combo_code_user_size.addItems(sizes)
        self.edit_code_assistant_size.addItems(sizes)

        # 文档助手页
        self.combo_document_user_size.addItems(sizes)
        self.edit_document_assistant_size.addItems(sizes)

    def connect_signals(self):
        """连接所有信号"""
        # 按钮
        self.btn_apply_setting.clicked.connect(self.apply_settings)
        self.btn_close_setting.clicked.connect(self.reject)
        self.btn_default_setting.clicked.connect(self.reset_to_default)

        # 导入导出
        self.btn_export_setting.clicked.connect(self.export_settings)
        self.btn_import_setting.clicked.connect(self.import_settings)
        self.btn_export_chat_history.clicked.connect(self.export_chat_history)
        self.btn_import_chat_history.clicked.connect(self.import_chat_history)

        # 颜色按钮
        self.btn_chat_user_color.clicked.connect(lambda: self.choose_color("chat_user"))
        self.btn_chat_assisant_color.clicked.connect(lambda: self.choose_color("chat_assistant"))
        self.btn_research_user_color.clicked.connect(lambda: self.choose_color("research_user"))
        self.btn_research_assisant_color.clicked.connect(lambda: self.choose_color("research_assistant"))
        self.btn_code_user_color.clicked.connect(lambda: self.choose_color("code_user"))
        self.btn_code_assisant_color.clicked.connect(lambda: self.choose_color("code_assistant"))
        self.btn_document_user_color.clicked.connect(lambda: self.choose_color("document_user"))
        self.btn_document_assisant_color.clicked.connect(lambda: self.choose_color("document_assistant"))

    def choose_color(self, target):
        """打开颜色选择器"""
        color = QColorDialog.getColor()
        if color.isValid():
            color_hex = color.name()
            self.color_values[target] = color_hex

            # 更新按钮背景色
            btn = getattr(self, f"btn_{target}_color", None)
            if btn:
                btn.setStyleSheet(f"background-color: {color_hex};")

    def find_font_by_family(self, combo_box, target_family):
        """通过字体家族名在 QFontComboBox 中查找并选中"""
        from PySide6.QtGui import QFont

        if init_config.isInTestMode:
            print(f"🔍 查找字体: target_family='{target_family}'")
            print(f"   下拉框共有 {combo_box.count()} 个字体")

        # 如果是空，选中第一项（系统默认）
        if not target_family:
            if init_config.isInTestMode:
                print(f"   ⚠️ target_family 为空，选中第一项")
            combo_box.setCurrentIndex(0)
            return

        # 先尝试精确匹配
        for i in range(combo_box.count()):
            item_text = combo_box.itemText(i)
            temp_font = QFont(item_text)
            actual_family = temp_font.family()

            # 精确匹配 actual_family
            if actual_family == target_family:
                if init_config.isInTestMode:
                    print(f"   ✅ 精确匹配 actual_family: '{actual_family}' == '{target_family}' 索引 {i}")
                combo_box.setCurrentIndex(i)
                return

            # 精确匹配 item_text
            if item_text == target_family:
                if init_config.isInTestMode:
                    print(f"   ✅ 精确匹配 item_text: '{item_text}' 索引 {i}")
                combo_box.setCurrentIndex(i)
                return

        # 再尝试包含匹配（target_family 是 actual_family 的一部分）
        for i in range(combo_box.count()):
            item_text = combo_box.itemText(i)
            temp_font = QFont(item_text)
            actual_family = temp_font.family()

            if init_config.isInTestMode and i < 5:
                print(f"   [{i}] item_text='{item_text}' -> actual_family='{actual_family}'")

            # target_family 包含在 actual_family 中（如 "Heiti" 在 "Heiti SC" 中）
            if target_family in actual_family:
                if init_config.isInTestMode:
                    print(f"   ✅ 包含匹配: '{target_family}' in actual_family='{actual_family}' 索引 {i}")
                combo_box.setCurrentIndex(i)
                return

            # actual_family 包含在 target_family 中（如 "Heiti SC" 包含 "Heiti"）
            if actual_family in target_family:
                if init_config.isInTestMode:
                    print(f"   ✅ 包含匹配: actual_family='{actual_family}' in '{target_family}' 索引 {i}")
                combo_box.setCurrentIndex(i)
                return

        # 最后，尝试查找显示名中包含 target_family 的
        for i in range(combo_box.count()):
            item_text = combo_box.itemText(i)
            if target_family in item_text:
                if init_config.isInTestMode:
                    print(f"   ✅ item_text 包含匹配: '{target_family}' in '{item_text}' 索引 {i}")
                combo_box.setCurrentIndex(i)
                return

        # 找不到匹配的字体，选第一项
        if init_config.isInTestMode:
            print(f"   ❌ 未找到匹配字体，选中第一项")
        combo_box.setCurrentIndex(0)

    def load_config_to_vars(self):
        """加载配置到变量（不直接操作 UI）"""
        env_path = init_config.get_env_path()
        self.config = {}

        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        self.config[key] = value.strip().strip('"')

        if init_config.isInTestMode:
            print(f"📖 已加载配置，共 {len(self.config)} 项")

        # ===== API 设置 =====
        self.chat_api_key = self.config.get("CHAT_ASSISTANT_API_KEY", "")
        self.research_api_key = self.config.get("RESEARCH_ASSISTANT_API_KEY", "")
        self.document_api_key = self.config.get("DOCUMENT_ASSISTANT_API_KEY", "")
        self.chat_api_url = self.config.get("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")
        self.research_api_url = self.config.get("RESEARCH_ASSISTANT_API_URL", "https://api.deepseek.com")
        self.document_api_url = self.config.get("DOCUMENT_ASSISTANT_API_URL", "https://api.deepseek.com")
        self.local_api_url = self.config.get("LOCAL_API_URL", "http://localhost:11434")
        self.local_model = self.config.get("LOCAL_MODEL", "deepseek-r1:7b")

        # ===== 聊天模式 =====
        self.user_prefix_chat = self.config.get("USER_PREFIX_CHAT", "用户：")
        self.assistant_prefix = self.config.get("ASSISTANT_PREFIX", "助手：")
        self.chat_assistant_prompt = self.config.get("CHAT_ASSISTANT_PROMPT", "你是AI助手，提供专业、友好的回答。")

        self.user_font = self.config.get("USER_FONT_1", "")
        self.assistant_font = self.config.get("ASSISTANT_FONT_1", "")
        self.user_size = self.config.get("USER_SIZE_1", "16")
        self.assistant_size = self.config.get("ASSISTANT_SIZE_1", "16")
        self.user_color = self.config.get("USER_COLOR_1", "#3C3C3C")
        self.assistant_color = self.config.get("ASSISTANT_COLOR_1", "#0078D7")

        # ===== 科研助手模式 =====
        self.research_user_prefix = self.config.get("USER_PREFIX_RESEARCH", "📊用户：")
        self.research_assistant_prefix = self.config.get("RESEARCH_PREFIX_1", "📊科研助手：")
        self.research_system_prompt = self.config.get("RESEARCH_SYSTEM_PROMPT", "科研助理模式")

        self.research_user_font = self.config.get("RESEARCH_USER_FONT", "")
        self.research_assistant_font = self.config.get("RESEARCH_ASSISTANT_FONT", "")
        self.research_user_size = self.config.get("RESEARCH_USER_SIZE", "16")
        self.research_assistant_size = self.config.get("RESEARCH_ASSISTANT_SIZE", "16")
        self.research_user_color = self.config.get("RESEARCH_USER_COLOR", "#2E86AB")
        self.research_assistant_color = self.config.get("RESEARCH_ASSISTANT_COLOR", "#2E86AB")

        # ===== 代码助手模式 =====
        self.code_user_prefix = self.config.get("USER_PREFIX_CODE", "👨‍💻用户：")
        self.code_assistant_prefix = self.config.get("CODE_PREFIX", "👨‍💻代码助手：")
        self.code_assistant_prompt = self.config.get("CODE_ASSISTANT_PROMPT", "你是代码助手，帮助用户解决编程问题。")

        self.code_user_font = self.config.get("CODE_USER_FONT", "")
        self.code_assistant_font = self.config.get("CODE_ASSISTANT_FONT", "")
        self.code_user_size = self.config.get("CODE_USER_SIZE", "16")
        self.code_assistant_size = self.config.get("CODE_ASSISTANT_SIZE", "16")
        self.code_user_color = self.config.get("CODE_USER_COLOR", "#28A745")
        self.code_assistant_color = self.config.get("CODE_ASSISTANT_COLOR", "#28A745")

        # ===== 文档助手模式（共用科研配置）=====
        self.document_user_prefix = self.config.get("DOCUMENT_USER_PREFIX", "📊用户：")
        self.document_assistant_prefix = self.config.get("DOCUMENT_ASSISTANT_PREFIX", "📊文档助手：")
        self.document_assistant_prompt = self.config.get("DOCUMENT_ASSISTANT_PROMPT", "文档助手模式")

        self.document_user_font = self.config.get("DOCUMENT_USER_FONT", "")
        self.document_assistant_font = self.config.get("DOCUMENT_ASSISTANT_FONT", "")
        self.document_user_size = self.config.get("DOCUMENT_USER_SIZE", "16")
        self.document_assistant_size = self.config.get("DOCUMENT_ASSISTANT_SIZE", "16")
        self.document_user_color = self.config.get("DOCUMENT_USER_COLOR", "#2E86AB")
        self.document_assistant_color = self.config.get("DOCUMENT_ASSISTANT_COLOR", "#2E86AB")

        if init_config.isInTestMode:
            print(f"   📝 科研用户前缀: {self.research_user_prefix}")
            print(f"   📝 代码用户前缀: {self.code_user_prefix}")

    def save_config(self):
        """保存配置到 env 文件"""
        from PySide6.QtGui import QFont

        # ===== 先定义 env_path =====
        env_path = init_config.get_env_path()

        if init_config.isInTestMode:
            print(f"📝 保存配置到: {env_path}")

        # ===== 获取所有字体名称 =====
        # 聊天模式
        user_font_name = self.combo_chat_user_font.currentFont().family()
        assistant_font_name = self.combo_chat_assisant_font.currentFont().family()

        # 科研模式（用户 + 助手）
        research_user_font_name = self.combo_research_user_font.currentFont().family()
        research_assistant_font_name = self.edit_research_assistant_font.currentFont().family()

        # 代码模式（用户 + 助手）
        code_user_font_name = self.edit_code_user_font.currentFont().family()
        code_assistant_font_name = self.edit_code_assistant_font.currentFont().family()

        # 文档模式（共用科研字体）
        doc_user_font_name = self.combo_document_user_font.currentFont().family()
        doc_assistant_font_name = self.edit_document_assistant_font.currentFont().family()

        if init_config.isInTestMode:
            print(f"📝 保存字体: 聊天用户={user_font_name}, 聊天助手={assistant_font_name}")
            print(f"   科研用户={research_user_font_name}, 科研助手={research_assistant_font_name}")
            print(f"   代码用户={code_user_font_name}, 代码助手={code_assistant_font_name}")

        # ===== 读取原有内容 =====
        lines = []
        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

        # ===== 构建新配置 =====
        new_config = {
            # API
            "CHAT_ASSISTANT_API_KEY": self.edit_chat_api_key.text().strip(),
            "CHAT_ASSISTANT_API_URL": self.edit_chat_api_url.text().strip(),
            "RESEARCH_ASSISTANT_API_KEY": self.edit_research_api_key.text().strip(),
            "RESEARCH_ASSISTANT_API_URL": self.edit_research_api_url.text().strip(),
            "DOCUMENT_ASSISTANT_API_KEY": self.edit_document_api_key.text().strip(),
            "DOCUMENT_ASSISTANT_API_URL": self.edit_document_api_url.text().strip(),
            "LOCAL_API_URL": self.edit_local_api_url.text().strip(),
            "LOCAL_MODEL": self.edit_local_model.text().strip(),

            # ===== 聊天模式 =====
            "USER_PREFIX_CHAT": self.edit_chat_user_prefix.text().strip(),
            "USER_FONT_1": f'"{user_font_name}"',
            "USER_SIZE_1": self.combo_chat_user_size.currentText(),
            "USER_COLOR_1": self.color_values.get("chat_user", "#3C3C3C"),

            "ASSISTANT_PREFIX": self.edit_chat_assistant_prefix.text().strip(),
            "ASSISTANT_FONT_1": f'"{assistant_font_name}"',
            "ASSISTANT_SIZE_1": self.combo_chat_assistant_size.currentText(),
            "ASSISTANT_COLOR_1": self.color_values.get("chat_assistant", "#0078D7"),
            "CHAT_ASSISTANT_PROMPT": self.edit_chat_assistant_prompt.text().strip(),

            # ===== 科研助手模式 =====
            "USER_PREFIX_RESEARCH": self.edit_research_user_prefix.text().strip(),
            "RESEARCH_USER_FONT": f'"{research_user_font_name}"',
            "RESEARCH_USER_SIZE": self.combo_research_user_size.currentText(),
            "RESEARCH_USER_COLOR": self.color_values.get("research_user", "#2E86AB"),

            "RESEARCH_PREFIX_1": self.edit_research_assistant_prefix.text().strip(),
            "RESEARCH_ASSISTANT_FONT": f'"{research_assistant_font_name}"',
            "RESEARCH_ASSISTANT_SIZE": self.edit_research_assistant_size.currentText(),
            "RESEARCH_ASSISTANT_COLOR": self.color_values.get("research_assistant", "#2E86AB"),
            "RESEARCH_SYSTEM_PROMPT": self.edit_research_assistant_prompt.text().strip(),

            # ===== 代码助手模式 =====
            "USER_PREFIX_CODE": self.edit_code_user_prefix.text().strip(),
            "CODE_USER_FONT": f'"{code_user_font_name}"',
            "CODE_USER_SIZE": self.combo_code_user_size.currentText(),
            "CODE_USER_COLOR": self.color_values.get("code_user", "#28A745"),

            "CODE_PREFIX": self.edit_code_assistant_prefix.text().strip(),
            "CODE_ASSISTANT_FONT": f'"{code_assistant_font_name}"',
            "CODE_ASSISTANT_SIZE": self.edit_code_assistant_size.currentText(),
            "CODE_ASSISTANT_COLOR": self.color_values.get("code_assistant", "#28A745"),
            "CODE_ASSISTANT_PROMPT": self.edit_code_assistant_prompt.text().strip(),

            # ===== 文档助手模式 =====
            "DOCUMENT_USER_PREFIX": self.edit_document_user_prefix.text().strip(),
            "DOCUMENT_ASSISTANT_PREFIX": self.edit_document_assistant_prefix.text().strip(),
            "DOCUMENT_ASSISTANT_PROMPT": self.edit_document_assistant_prompt.text().strip(),
            "DOCUMENT_USER_FONT": f'"{doc_user_font_name}"',
            "DOCUMENT_ASSISTANT_FONT": f'"{doc_assistant_font_name}"',
            "DOCUMENT_USER_SIZE": self.combo_document_user_size.currentText(),
            "DOCUMENT_ASSISTANT_SIZE": self.edit_document_assistant_size.currentText(),
            "DOCUMENT_USER_COLOR": self.color_values.get("document_user", "#2E86AB"),
            "DOCUMENT_ASSISTANT_COLOR": self.color_values.get("document_assistant", "#2E86AB"),
        }

        # ===== 写回文件 =====
        updated_keys = set()
        with open(env_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.strip().startswith('#') or not line.strip():
                    f.write(line)
                else:
                    written = False
                    for key, value in new_config.items():
                        if line.startswith(f"{key}="):
                            f.write(f"{key}={value}\n")
                            updated_keys.add(key)
                            written = True
                            break
                    if not written:
                        f.write(line)

            # 添加新配置项
            for key, value in new_config.items():
                if key not in updated_keys:
                    f.write(f"{key}={value}\n")

        if init_config.isInTestMode:
            print(f"✅ 配置已保存到 {env_path}")

    def apply_settings(self):
        """应用设置"""
        self.save_config()

        # 通知主窗口重新加载配置（会更新人设但不删除聊天记录）
        if self.parent():
            self.parent().reload_config()

        QMessageBox.information(self, "设置已保存", "配置已生效。")
        self.accept()

    def reset_to_default(self):
        """恢复默认设置（保留 API Key 和 URL，不清除聊天记录）"""
        reply = QMessageBox.question(
            self, "确认恢复默认",
            "确定要恢复所有设置为默认值吗？\n\n注意：API Key、URL 和聊天记录不会被清除。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            # 从 init_config 的默认模板中解析默认值
            default_content = init_config.get_default_env_content()
            default_config = {}

            for line in default_content.split('\n'):
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    default_config[key] = value.strip().strip('"')

            # 保存当前 API 配置
            current_chat_key = self.edit_chat_api_key.text()
            current_research_key = self.edit_research_api_key.text()
            current_doc_key = self.edit_document_api_key.text()
            current_chat_url = self.edit_chat_api_url.text()
            current_research_url = self.edit_research_api_url.text()
            current_doc_url = self.edit_document_api_url.text()
            current_local_url = self.edit_local_api_url.text()
            current_local_model = self.edit_local_model.text()

            # ===== 恢复聊天设置到默认值 =====
            self.edit_chat_user_prefix.setText(default_config.get("USER_PREFIX_CHAT", "用户："))
            self.edit_chat_assistant_prefix.setText(default_config.get("ASSISTANT_PREFIX", "助手："))
            self.edit_chat_assistant_prompt.setText(default_config.get("CHAT_ASSISTANT_PROMPT", "你是AI助手，提供专业、友好的回答。"))

            # 字体（恢复为空字符串，使用系统默认）
            self._reset_font_to_default(self.combo_chat_user_font)
            self._reset_font_to_default(self.combo_chat_assisant_font)

            # 字体大小
            user_size = default_config.get("USER_SIZE_1", "16")
            idx = self.combo_chat_user_size.findText(user_size)
            if idx >= 0:
                self.combo_chat_user_size.setCurrentIndex(idx)

            assistant_size = default_config.get("ASSISTANT_SIZE_1", "16")
            idx = self.combo_chat_assistant_size.findText(assistant_size)
            if idx >= 0:
                self.combo_chat_assistant_size.setCurrentIndex(idx)

            # 颜色
            user_color = default_config.get("USER_COLOR_1", "#3C3C3C")
            self.color_values["chat_user"] = user_color
            self.btn_chat_user_color.setStyleSheet(f"background-color: {user_color};")

            assistant_color = default_config.get("ASSISTANT_COLOR_1", "#0078D7")
            self.color_values["chat_assistant"] = assistant_color
            self.btn_chat_assisant_color.setStyleSheet(f"background-color: {assistant_color};")

            # ===== 恢复科研助手设置 =====
            self.edit_research_user_prefix.setText(default_config.get("USER_PREFIX_RESEARCH", "📊用户："))
            self.edit_research_assistant_prefix.setText(default_config.get("RESEARCH_PREFIX_1", "📊科研助手："))
            self.edit_research_assistant_prompt.setText(default_config.get("RESEARCH_SYSTEM_PROMPT", "科研助理模式"))

            # 字体（恢复为空字符串）
            self._reset_font_to_default(self.combo_research_user_font)
            self._reset_font_to_default(self.edit_research_assistant_font)

            # 字体大小
            research_user_size = default_config.get("RESEARCH_USER_SIZE", "16")
            idx = self.combo_research_user_size.findText(research_user_size)
            if idx >= 0:
                self.combo_research_user_size.setCurrentIndex(idx)

            research_assistant_size = default_config.get("RESEARCH_ASSISTANT_SIZE", "16")
            idx = self.edit_research_assistant_size.findText(research_assistant_size)
            if idx >= 0:
                self.edit_research_assistant_size.setCurrentIndex(idx)

            # 颜色（使用新的变量名）
            research_user_color = default_config.get("RESEARCH_USER_COLOR", "#2E86AB")
            self.color_values["research_user"] = research_user_color
            self.btn_research_user_color.setStyleSheet(f"background-color: {research_user_color};")

            research_assistant_color = default_config.get("RESEARCH_ASSISTANT_COLOR", "#2E86AB")
            self.color_values["research_assistant"] = research_assistant_color
            self.btn_research_assisant_color.setStyleSheet(f"background-color: {research_assistant_color};")

            # ===== 恢复代码助手设置 =====
            self.edit_code_user_prefix.setText(default_config.get("USER_PREFIX_CODE", "👨‍💻用户："))
            self.edit_code_assistant_prefix.setText(default_config.get("CODE_PREFIX", "👨‍💻代码助手："))
            self.edit_code_assistant_prompt.setText(default_config.get("CODE_ASSISTANT_PROMPT", "你是代码助手，帮助用户解决编程问题。"))

            # 字体（恢复为空字符串）
            self._reset_font_to_default(self.edit_code_user_font)
            self._reset_font_to_default(self.edit_code_assistant_font)

            # 字体大小
            code_user_size = default_config.get("CODE_USER_SIZE", "16")
            idx = self.combo_code_user_size.findText(code_user_size)
            if idx >= 0:
                self.combo_code_user_size.setCurrentIndex(idx)

            code_assistant_size = default_config.get("CODE_ASSISTANT_SIZE", "16")
            idx = self.edit_code_assistant_size.findText(code_assistant_size)
            if idx >= 0:
                self.edit_code_assistant_size.setCurrentIndex(idx)

            # 颜色（使用新的变量名）
            code_user_color = default_config.get("CODE_USER_COLOR", "#28A745")
            self.color_values["code_user"] = code_user_color
            self.btn_code_user_color.setStyleSheet(f"background-color: {code_user_color};")

            code_assistant_color = default_config.get("CODE_ASSISTANT_COLOR", "#28A745")
            self.color_values["code_assistant"] = code_assistant_color
            self.btn_code_assisant_color.setStyleSheet(f"background-color: {code_assistant_color};")

            # ===== 恢复文档助手设置 =====
            self.edit_document_user_prefix.setText(default_config.get("DOCUMENT_USER_PREFIX", "📊用户："))
            self.edit_document_assistant_prefix.setText(default_config.get("DOCUMENT_ASSISTANT_PREFIX", "📊文档助手："))
            self.edit_document_assistant_prompt.setText(default_config.get("DOCUMENT_ASSISTANT_PROMPT", "文档助手模式"))

            # 字体（恢复为空字符串）
            self._reset_font_to_default(self.combo_document_user_font)
            self._reset_font_to_default(self.edit_document_assistant_font)

            # 字体大小
            doc_user_size = default_config.get("DOCUMENT_USER_SIZE", "16")
            idx = self.combo_document_user_size.findText(doc_user_size)
            if idx >= 0:
                self.combo_document_user_size.setCurrentIndex(idx)

            doc_assistant_size = default_config.get("DOCUMENT_ASSISTANT_SIZE", "16")
            idx = self.edit_document_assistant_size.findText(doc_assistant_size)
            if idx >= 0:
                self.edit_document_assistant_size.setCurrentIndex(idx)

            # 颜色
            doc_user_color = default_config.get("DOCUMENT_USER_COLOR", "#2E86AB")
            self.color_values["document_user"] = doc_user_color
            self.btn_document_user_color.setStyleSheet(f"background-color: {doc_user_color};")

            doc_assistant_color = default_config.get("DOCUMENT_ASSISTANT_COLOR", "#2E86AB")
            self.color_values["document_assistant"] = doc_assistant_color
            self.btn_document_assisant_color.setStyleSheet(f"background-color: {doc_assistant_color};")

            # ===== 恢复 API 设置（保留当前值）=====
            self.edit_chat_api_key.setText(current_chat_key)
            self.edit_research_api_key.setText(current_research_key)
            self.edit_document_api_key.setText(current_doc_key)
            self.edit_chat_api_url.setText(current_chat_url)
            self.edit_research_api_url.setText(current_research_url)
            self.edit_document_api_url.setText(current_doc_url)
            self.edit_local_api_url.setText(current_local_url)
            self.edit_local_model.setText(current_local_model)

            QMessageBox.information(self, "已恢复", "已恢复默认设置（API Key、URL 和聊天记录已保留），点击应用保存。")

    def _reset_font_to_default(self, combo_box):
        """将字体下拉框重置为默认（第一项，系统默认字体）"""
        combo_box.setCurrentIndex(0)
        if init_config.isInTestMode:
            print(f"   🔄 字体已重置为系统默认: {combo_box.currentText()}")

    def export_settings(self):
        """导出设置文件"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "导出设置", "", "配置文件 (*.env);;所有文件 (*)"
        )
        if file_path:
            env_path = init_config.get_env_path()
            import shutil
            shutil.copy2(env_path, file_path)
            QMessageBox.information(self, "导出成功", f"设置已导出到:\n{file_path}")

    def import_settings(self):
        """导入设置文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "导入设置", "", "配置文件 (*.env);;所有文件 (*)"
        )
        if file_path:
            env_path = init_config.get_env_path()
            import shutil
            shutil.copy2(file_path, env_path)
            # 重新加载配置到变量（注意方法名是 load_config_to_vars）
            self.load_config_to_vars()
            # 刷新 UI 显示
            self.refresh_ui()
            QMessageBox.information(self, "导入成功", "设置已导入，点击应用保存。")

    def export_chat_history(self):
        """导出聊天记录"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "导出聊天记录", "", "JSON文件 (*.json);;所有文件 (*)"
        )
        if file_path:
            internal_dir = init_config.get_internal_dir()
            history_path = os.path.join(internal_dir, "chat_history.json")
            if os.path.exists(history_path):
                import shutil
                shutil.copy2(history_path, file_path)
                QMessageBox.information(self, "导出成功", f"聊天记录已导出到:\n{file_path}")
            else:
                QMessageBox.warning(self, "无记录", "没有找到聊天记录文件。")

    def import_chat_history(self):
        """导入聊天记录"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "导入聊天记录", "", "JSON文件 (*.json);;所有文件 (*)"
        )
        if file_path:
            internal_dir = init_config.get_internal_dir()
            history_path = os.path.join(internal_dir, "chat_history.json")
            import shutil
            shutil.copy2(file_path, history_path)
            QMessageBox.information(self, "导入成功", "聊天记录已导入，重启程序后生效。")