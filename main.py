from fileinput import filename
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QSizePolicy, QVBoxLayout, QHBoxLayout, QTextEdit
from PySide6.QtWidgets import QMessageBox, QDialog, QLabel, QProgressBar, QPushButton, QApplication
from PySide6.QtCore import QTimer, QEvent, Qt
from certifi import contents
from PySide6.QtGui import QTextCursor, QFont, QColor
import mainWindowCode
from dotenv import load_dotenv
import os
import sys
import platform
import json
import requests
import time
import socket
from openai import OpenAI
from PySide6.QtWidgets import QFileDialog
import markdown
import docx
import PyPDF2
import pandas
# import PyInstaller
import init_config
import setting_dialog_ui
import setting_dialog
import knowledge_base_dialog
import knowledge_dialog_ui
from knowledge_base_dialog import KnowledgeBaseDialog

isInTestMode = init_config.isInTestMode


def resource_path(relative_path):
    """获取打包后资源的绝对路径

    优先级：
    1. 打包后 _internal 目录（只读资源，如历史文件）
    2. 开发环境当前目录
    """
    if getattr(sys, 'frozen', False):
        # 打包后的 exe 运行，资源在 _internal 里
        exe_dir = os.path.dirname(sys.executable)
        return os.path.join(exe_dir, '_internal', relative_path)
    else:
        # 开发环境
        return os.path.join(os.path.abspath("."), relative_path)


# 确保配置文件存在（在 _internal 目录）
env_path, is_first_run, has_api_keys = init_config.ensure_config_exists()
# 加载环境变量
load_dotenv(env_path)

# 历史文件路径（在 _internal 目录）
history_file = resource_path("chat_history.json")
# 尝试读取历史文件，如果失败则使用默认配置
try:
    # 这里只是定义路径，实际读取在 LoadHistory 里
    # 如果文件存在但无法读取，LoadHistory 里会有异常处理
    pass
except Exception as e:
    if isInTestMode:
        print(f"⚠️ [调试模式] 历史文件路径异常: {e}")


def check_system_dependencies(self):
    """检查系统依赖（OCR相关）"""
    deps_status = {
        "poppler": False,
        "tesseract": False,
        "tesseract_lang_chi": False
    }

    if platform.system() == "Windows":
        # Windows 需要检查 PATH 或常见安装路径
        poppler_path = shutil.which("pdfinfo")
        tesseract_path = shutil.which("tesseract")
        deps_status["poppler"] = poppler_path is not None
        deps_status["tesseract"] = tesseract_path is not None
    else:
        # macOS/Linux
        deps_status["poppler"] = os.path.exists("/opt/homebrew/bin/pdfinfo") or \
                                 os.path.exists("/usr/bin/pdfinfo")
        deps_status["tesseract"] = os.path.exists("/opt/homebrew/bin/tesseract") or \
                                   os.path.exists("/usr/bin/tesseract")

    # 检查中文语言包
    if deps_status["tesseract"]:
        tessdata_path = "/opt/homebrew/share/tessdata/chi_sim.traineddata"
        deps_status["tesseract_lang_chi"] = os.path.exists(tessdata_path)

    return deps_status


def get_api_key_for_mode(mode):
    """根据模式获取对应的 API Key 和 URL
    优先级：
    1. 模式专用 Key
    2. 科研共用 Key（research_api / code / document）
    3. 聊天 Key（兜底）
    """
    if mode == "chat":
        key = os.getenv("CHAT_ASSISTANT_API_KEY")
        url = os.getenv("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")

    elif mode == "research_api":
        # 优先用专用，没有则用科研共用
        key = os.getenv("RESEARCH_ASSISTANT_API_KEY")
        url = os.getenv("RESEARCH_ASSISTANT_API_URL", "https://api.deepseek.com")

        # 如果科研共用也没有，用聊天的兜底
        if not key:
            key = os.getenv("CHAT_ASSISTANT_API_KEY")
            url = os.getenv("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")

    elif mode == "code":
        # 优先代码专用
        key = os.getenv("CODE_ASSISTANT_API_KEY")
        url = os.getenv("CODE_ASSISTANT_API_URL")

        # 没有专用则用科研共用
        if not key:
            key = os.getenv("RESEARCH_ASSISTANT_API_KEY")
            url = os.getenv("RESEARCH_ASSISTANT_API_URL")

        # 科研也没有则用聊天兜底
        if not key:
            key = os.getenv("CHAT_ASSISTANT_API_KEY")
            url = os.getenv("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")

    elif mode == "document":
        # 优先文档专用
        key = os.getenv("DOCUMENT_ASSISTANT_API_KEY")
        url = os.getenv("DOCUMENT_ASSISTANT_API_URL")

        if not key:
            key = os.getenv("RESEARCH_ASSISTANT_API_KEY")
            url = os.getenv("RESEARCH_ASSISTANT_API_URL")

        if not key:
            key = os.getenv("CHAT_ASSISTANT_API_KEY")
            url = os.getenv("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")

    else:  # 默认
        key = os.getenv("CHAT_ASSISTANT_API_KEY")
        url = os.getenv("CHAT_ASSISTANT_API_URL", "https://api.deepseek.com")

    # 如果 URL 没有设置，用默认
    if not url:
        url = "https://api.deepseek.com"

    return key, url


if isInTestMode:
    print(f"聊天模式的api_key/url：", get_api_key_for_mode("chat"))
    print(f"科研助手模式的api_key/url：", get_api_key_for_mode("research_api"))
    print(f"代码助手模式的api_key/url：", get_api_key_for_mode("code"))
    print(f"文档模式的api_key/url：", get_api_key_for_mode("document"))

# ---------- 科研助手 ----------
research_font_1 = os.getenv("RESEARCH_USER_FONT", ".AppleSystemUIFont")
research_size_1 = int(os.getenv("RESEARCH_USER_SIZE", 16))
research_color_1 = os.getenv("RESEARCH_USER_COLOR", "#2E86AB")  # 科研用户颜色
research_assistant_color = os.getenv("RESEARCH_ASSISTANT_COLOR", "#2E86AB")  # 科研助手颜色 ✅ 新增
research_bg_1 = os.getenv("RESEARCH_BG", "")

# ---------- 代码助手 ----------
code_font_1 = os.getenv("CODE_USER_FONT", ".AppleSystemUIFont")
code_size_1 = int(os.getenv("CODE_USER_SIZE", 16))
code_color_1 = os.getenv("CODE_USER_COLOR", "#28A745")  # 代码用户颜色
code_assistant_color = os.getenv("CODE_ASSISTANT_COLOR", "#28A745")  # 代码助手颜色 ✅ 新增
code_bg_1 = os.getenv("CODE_BG", "")

# ---------- 用户字体/颜色/前缀 ----------
user_font_1 = os.getenv("USER_FONT_1", ".AppleSystemUIFont")
user_size_1 = int(os.getenv("USER_SIZE_1", 16))
user_color_1 = os.getenv("USER_COLOR_1", "#FFB6C1")
user_bg_1 = os.getenv("USER_BG_1", "")

user_prefix_chat = os.getenv("USER_PREFIX_CHAT", "用户")
user_prefix_research = os.getenv("USER_PREFIX_RESEARCH", "用户")
user_prefix_code = os.getenv("USER_PREFIX_CODE", "用户")

# ---------- 猫娘姐姐 ----------
assistant_font_1 = os.getenv("ASSISTANT_FONT_1", ".AppleSystemUIFont")
assistant_size_1 = int(os.getenv("ASSISTANT_SIZE_1", 16))
assistant_color_1 = os.getenv("ASSISTANT_COLOR_1", "#D8BFD8")
assistant_prefix_1 = os.getenv("ASSISTANT_PREFIX", "助手：")
assistant_bg_1 = os.getenv("ASSISTANT_BG_1", "")
chat_assistant_prompt = os.getenv("CHAT_ASSISTANT_PROMPT", "")

# ---------- 科研助理 ----------
research_font_1 = os.getenv("RESEARCH_FONT", ".AppleSystemUIFont")
research_size_1 = int(os.getenv("RESEARCH_SIZE", 16))
research_color_1 = os.getenv("RESEARCH_COLOR", "#2E86AB")
research_bg_1 = os.getenv("RESEARCH_BG", "")

research_prefix_1 = os.getenv("RESEARCH_PREFIX_1", "📊科研助理-在线模式：")
research_prefix_2 = os.getenv("RESEARCH_PREFIX_2", "📊科研助理-脱敏模式：")
research_prefix_3 = os.getenv("RESEARCH_PREFIX_3", "📊科研助理-本地模式：")

# ---------- 代码助手 ----------
code_font_1 = os.getenv("CODE_FONT", ".AppleSystemUIFont")
code_size_1 = int(os.getenv("CODE_SIZE", 16))
code_color_1 = os.getenv("CODE_COLOR", "#28A745")
code_prefix_1 = os.getenv("CODE_PREFIX", "👨‍💻代码助手：")
code_bg_1 = os.getenv("CODE_BG", "")
code_assistant_prompt = os.getenv("CODE_ASSISTANT_PROMPT", "")

# ---------- 系统消息 ----------
system_font_1 = os.getenv("SYSTEM_FONT_1", ".AppleSystemUIFont")
system_size_1 = int(os.getenv("SYSTEM_SIZE_1", 16))
system_color_1 = os.getenv("SYSTEM_COLOR_1", "#999999")
system_prefix_1 = os.getenv("SYSTEM_PREFIX_1", "系统")
system_style = os.getenv("SYSTEM_STYLE_1", "italic")

# ---------- 输入框 ----------
input_font_1 = os.getenv("INPUT_FONT_1", ".AppleSystemUIFont")
input_size_1 = int(os.getenv("INPUT_SIZE_1", 16))
input_color_1 = os.getenv("INPUT_COLOR_1", "#333333")
input_bg_1 = os.getenv("INPUT_BG_1", "#FFFFFF")
input_placeholder_color_1 = os.getenv("INPUT_PLACEHOLDER_COLOR_1", "#999999")

# ---------- 其他 ----------
is_stream_mode = os.getenv("IS_STREAM_MODE", "false").lower() == "true"
research_system_prompt = os.getenv("RESEARCH_SYSTEM_PROMPT", "科研助理模式")

# 容器样式
chat_container_bg = os.getenv("CHAT_CONTAINER_BG", "#1b1b1c")
sidebar_bg = os.getenv("SIDEBAR_BG", "#2d2d2d")
input_bg = os.getenv("INPUT_BG", "#3c3c3c")

# 消息背景
user_msg_bg = os.getenv("USER_MSG_BG", "#2d2d2d")
assistant_msg_bg = os.getenv("ASSISTANT_MSG_BG", "#383838")
system_msg_bg = os.getenv("SYSTEM_MSG_BG", "#252525")

# 边框
message_border_color = os.getenv("MESSAGE_BORDER_COLOR", "#444")
focus_border_color = os.getenv("FOCUS_BORDER_COLOR", "#9c27b0")

# 时间戳
timestamp_color = os.getenv("TIMESTAMP_COLOR", "#888")

# 代码块
code_block_bg = os.getenv("CODE_BLOCK_BG", "#0d0d0d")
code_block_text = os.getenv("CODE_BLOCK_TEXT", "#abb2bf")


class MainWindowWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowWidget, self).__init__(parent)
        # 保存配置状态（用于后续显示系统消息）
        self.is_first_run = is_first_run
        self.has_api_keys = has_api_keys

        self.ui0 = mainWindowCode.Ui_mainWindow()
        self.ui0.setupUi(self)

        self.current_mode = "chat"  # 默认进入聊天模式
        self.stream_mode = is_stream_mode  # 是否流式传输
        self.current_file_content = None  # 存储上传文件的内容
        self.is_calculating = False  # 是否正在计算
        # 知识库引用（懒加载）
        self.kb_dialog = None

        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QWidget {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }
            QTextEdit, QLineEdit {
                background-color: #3c3c3c;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 4px;
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #4a4a4a;
                border: 1px solid #666;
                border-radius: 4px;
                padding: 6px;
                color: #e0e0e0;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
            QListWidget {
                background-color: #2d2d2d;
                border: 1px solid #444;
                color: #e0e0e0;
            }
        """)

        # 初始化系统信息框
        self.update_system_info("normal")

        # 初始聊天信息显示框
        self.web_displayer = self.ui0.web_chat_display
        self.init_web_template()  # 用 HTML 模板初始化
        self.webview_ready = False
        self.web_displayer.loadFinished.connect(self.on_webview_loaded)
        self.pending_messages = []

        # 窗口标题
        window_title = os.getenv("WINDOW_TITLE", "雪雪的AI助手")
        self.setWindowTitle(window_title)

        # 输入框提示词
        input_placeholder = os.getenv("INPUT_PLACEHOLDER_CHAT", "输入你想发送的消息～")
        self.ui0.text_message_input.setPlaceholderText(input_placeholder)

        # 系统消息文本
        welcome_title = os.getenv("SYSTEM_WELCOME_TITLE", "🐱 欢迎使用雪雪AI助手！")

        # 根据聊天模式加载历史消息
        self.local_exist_history_files = {"chat": "chat_history.json",
                                          "research_api": "research_api_history.json",
                                          "research_desensitize": "research_desensitize_history.json",
                                          "research_local": "research_local_history.json",
                                          "code": "code_history.json"}
        self.history_file = self.local_exist_history_files[self.current_mode]
        self.LoadHistory()  # LoadHistory里会给self.raw_message 赋值
        # 如果LoadHistory没赋值，再给默认值
        if not hasattr(self, 'raw_message') or not self.raw_message:
            self.raw_message = self.GetDefaultMessageForMode(self.current_mode)

        # 根据聊天模式加载输入框默认提示词
        self.input_placeholder_presets = {"chat": "输入你想发送的消息～",
                                          "research_api": "把文件草稿给我，并准确描述你的要求。",
                                          "research_desensitize": "把文件草稿给我，并准确描述你的要求。",
                                          "research_local": "把文件草稿给我，并准确描述你的要求。",
                                          "code": "代码遇到了什么问题呢？"}
        self.input_placeholder = self.input_placeholder_presets[self.current_mode]
        self.ui0.text_message_input.setPlaceholderText(self.input_placeholder)

        # 输入框字体
        input_font = QFont(user_font_1, user_size_1)
        self.ui0.text_message_input.setFont(input_font)

        self.mode_buttons = {
            "chat": self.ui0.btn_mode_sel_1,
            "research_api": self.ui0.btn_mode_sel_2,
            "research_desensitize": self.ui0.btn_mode_sel_3,
            "research_local": self.ui0.btn_mode_sel_4,
            "code": self.ui0.btn_mode_sel_5,
            "setting": self.ui0.btn_sys_setting
        }

        self.UpdateModeButtonStyle()

        # 安装事件过滤器
        self.ui0.text_message_input.mousePressEvent = self.OnInputClick
        # 绑定按钮
        self.ui0.btn_send_message.clicked.connect(self.SendMessageFunc)
        self.ui0.btn_clear_message.clicked.connect(self.ClearChat)
        self.ui0.btn_mode_sel_1.clicked.connect(lambda: self.SwitchMode("chat"))
        self.ui0.btn_mode_sel_2.clicked.connect(lambda: self.SwitchMode("research_api"))
        self.ui0.btn_mode_sel_3.clicked.connect(lambda: self.SwitchMode("research_desensitize"))
        self.ui0.btn_mode_sel_4.clicked.connect(lambda: self.SwitchMode("research_local"))
        self.ui0.btn_mode_sel_5.clicked.connect(lambda: self.SwitchMode("code"))
        self.ui0.btn_upload_file.clicked.connect(self.UploadFile)
        self.current_file_path = None  # 记录当前上传的文件
        self.ui0.btn_sys_setting.clicked.connect(self.open_setting_dialog)
        self.ui0.btn_loacl_knowledge_base.clicked.connect(self.open_knowledge_base)

        # 添加网络检测定时器
        self.network_timer = QTimer()
        self.network_timer.timeout.connect(self.check_network)
        self.network_timer.start(30000)  # 每30秒检测一次

    def search_knowledge_base(self, query, top_k=3):
        """从知识库检索相关内容"""
        try:
            if self.kb_dialog is None:
                self.kb_dialog = KnowledgeBaseDialog(self)

            if not self.kb_dialog.deps_installed:
                return ""

            result = self.kb_dialog.search(query, top_k)
            if init_config.isInTestMode and result:
                print(f"📚 检索到 {len(result)} 字符")
                print(f"   内容预览: {result[:200]}...")
            return result
        except Exception as e:
            if init_config.isInTestMode:
                print(f"⚠️ 知识库检索失败: {e}")
            return ""

    def open_knowledge_base(self):
        """打开本地知识库窗口（带等待提示）"""
        from knowledge_base_dialog import KnowledgeBaseDialog

        # 创建等待对话框
        wait_dialog = QDialog(self)
        wait_dialog.setWindowTitle("请稍候")
        wait_dialog.setModal(True)
        wait_dialog.setFixedSize(400, 200)

        layout = QVBoxLayout(wait_dialog)

        # 提示文字
        label = QLabel("📚 正在加载知识库...\n\n打开知识库界面需要初始化解析模型，请耐心等待。")
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # 无限进度条（表示程序在工作）
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)  # 0-0 表示忙碌状态，会一直滚动
        layout.addWidget(progress_bar)

        # 取消按钮
        cancel_btn = QPushButton("取消")
        cancel_btn.clicked.connect(wait_dialog.reject)
        layout.addWidget(cancel_btn)

        wait_dialog.show()
        QApplication.processEvents()

        try:
            # 创建知识库对话框（这会触发模型加载和索引检查）
            dialog = KnowledgeBaseDialog(self)
            wait_dialog.accept()
            dialog.exec()
        except Exception as e:
            wait_dialog.accept()
            QMessageBox.warning(self, "错误", f"加载知识库失败：{e}")

    def open_setting_dialog(self):
        """打开设置窗口"""
        from setting_dialog import SettingDialog
        dialog = SettingDialog(self)
        dialog.exec()

    def on_webview_loaded(self):
        self.webview_ready = True
        js = "console.log('WebView已就绪');"
        self.web_displayer.page().runJavaScript(js)

        # 显示配置相关的系统消息
        config_msg = init_config.get_config_message(self.is_first_run, self.has_api_keys)
        if config_msg:
            self.DisplayMessage("system", config_msg)

        # 把暂存的消息发出去
        for msg in self.pending_messages:
            self.add_message_to_webview(msg)
        self.pending_messages = []

    def add_message_to_webview(self, html_content):
        if not self.webview_ready:
            self.pending_messages.append(html_content)
            return

        import json
        # 用 json.dumps 来保护字符串，这样就不会被特殊字符弄坏啦～
        safe_content = json.dumps(html_content)
        js_code = f"""
            (function() {{
                try {{
                    var container = document.getElementById('chat-container');
                    if (!container) {{
                        console.error('chat-container 还没准备好');
                        return false;
                    }}
                    var div = document.createElement('div');
                    div.innerHTML = {safe_content};
                    var nodeToAdd = div.firstElementChild || div;
                    container.appendChild(nodeToAdd);
                    container.scrollTop = container.scrollHeight;
                    return true;
                }} catch(e) {{
                    console.error('添加消息失败:', e);
                    return false;
                }}
            }})();
            """
        self.web_displayer.page().runJavaScript(js_code)

    def check_network(self):
        """检测网络连接状态"""
        try:
            # 尝试连接 DeepSeek 的 API 地址
            socket.create_connection(("api.deepseek.com", 443), timeout=5)
            # 网络正常，恢复之前的状态
            # 如果当前没有在忙碌，就设为正常状态
            if self.current_mode in ["research_api", "research_local", "code", "research_desensitize"]:
                # 如果是科研/代码模式，保持忙碌状态？这里需要判断是否正在计算
                # 简单处理：如果不在计算中，就设为正常
                if not hasattr(self, 'is_calculating') or not self.is_calculating:
                    self.update_system_info("normal")
            else:
                self.update_system_info("normal")
        except OSError:
            # 网络异常，显示离线状态
            self.update_system_info("offline")

    def UploadFile(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "所有文件 (*);;图片 (*.png *.jpg *.jpeg *.gif);;文档 (*.pdf *.docx *.txt);;表格 (*.xlsx *.xls)")

        if not file_path:
            return

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # 在聊天框里显示文件上传成功的系统消息
        self.DisplayMessage("system", f"已上传文件：{file_name} ({file_size} 字节)\n你可以输入指令让我处理这个文件。")

        # 保存文件路径
        self.current_file_path = file_path

    def UpdateModeButtonStyle(self):
        # 首先把所有按钮都恢复到默认样式
        default_style = ""  # 留空就是用系统默认
        for btn in self.mode_buttons.values():
            btn.setStyleSheet(default_style)

        # 然后给当前模式按钮加高亮
        if self.current_mode in self.mode_buttons:
            current_button = self.mode_buttons[self.current_mode]
            current_button.setStyleSheet("""
                                            QPushButton {
                                            background-color: #3CB371;
                                            border: 1px solid #A5D6A5;
                                            border-radius: 4px;
                                            }
                                            QPushButton:hover {
                                                background-color: #C8E6C8;
                                            }
                                                """)

    def SwitchMode(self, mode):
        if mode == self.current_mode:
            return
        else:
            # 保存当前模式的历史
            self.SaveHistory()
            # 切换模式
            self.current_mode = mode
            # 根据模式选择历史文件
            self.current_mode = mode
            self.history_file = self.local_exist_history_files[mode]  # 直接映射
            # 清空显示
            self.clear_webview()
            # 加载新模式的历史消息
            self.LoadHistory()
            # 显示系统消息
            if len(self.raw_message) > 0 and self.raw_message[0]["role"] == "system":
                self.DisplayMessage("system", self.raw_message[0]["content"])
            # 切换输入框提示词
            self.input_placeholder = self.input_placeholder_presets[mode]
            self.ui0.text_message_input.setPlainText(self.input_placeholder)

            self.UpdateModeButtonStyle()
            self.update_system_info("normal")

    def OnInputClick(self, event):
        # 先执行原来的mousePressEvent，保持光标正常
        QTextEdit.mousePressEvent(self.ui0.text_message_input, event)
        # 然后判断是否清空
        current_text = self.ui0.text_message_input.toPlainText()
        if current_text == self.input_placeholder:
            self.ui0.text_message_input.clear()

    def EventFilter(self, obj, event):
        if obj == self.ui0.text_message_input:
            # 获得焦点时
            if event.type() == QEvent.FocusIn:
                current_text = self.ui0.text_message_input.toPlainText()
                # 如果当前是提示词才清空
                if current_text == self.input_placeholder:
                    self.ui0.text_message_input.clear()
            # 失去焦点时：
            elif event.type() == QEvent.FocusOut:
                current_text = self.ui0.text_message_input.toPlainText()
                # 如果内容是空的，恢复提示词
                if not current_text.strip():
                    self.ui0.text_message_input.setPlainText(self.input_placeholder)
        return super().eventFilter(obj, event)

    def GetDefaultMessageForMode(self, mode):
        if mode == "chat":
            return [{"role": "system", "content": chat_assistant_prompt}]  # 这里用的是变量
        elif mode == "research_api":
            return [{"role": "system", "content": research_system_prompt}]
        elif mode == "research_desensitize":
            return [{"role": "system", "content": research_system_prompt}]
        elif mode == "research_local":
            return [{"role": "system", "content": research_system_prompt}]
        elif mode == "code":
            return [{"role": "system", "content": code_assistant_prompt}]
        else:
            return [{"role": "system", "content": "模式切换状态读取失败，尝试输入你需要发送的消息。"}]

    def SaveHistory(self):
        # 保存前也过滤一次信息，删掉文档内容
        filtered = []
        for msg in self.raw_message:
            if msg["role"] == "user" and "【文件内容开始】" in msg["content"]:
                import re
                cleaned = re.sub(r'【文件内容开始】.*?【文件内容结束】', '', msg["content"], flags=re.DOTALL)
                if cleaned.strip():
                    msg["content"] = cleaned
                    filtered.append(msg)
            else:
                filtered.append(msg)

        if isInTestMode:
            print(f"SaveHistory: 正在保存 {len(self.raw_message)} 条消息到 {self.history_file}")

        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(self.raw_message, f, ensure_ascii=False, indent=2)

        except PermissionError as e:
            if isInTestMode:
                print(f"⚠️ SaveHistory: 无法保存历史文件（权限不足）: {e}")
            self.DisplayMessage("system", "⚠️ 无法保存聊天记录（权限不足）\n\n聊天记录将不会保留，但当前会话正常使用。")

        except Exception as e:
            if isInTestMode:
                print(f"⚠️ SaveHistory: 保存失败: {e}")
            self.DisplayMessage("system", f"⚠️ 保存聊天记录失败: {e}")

    def LoadHistory(self):
        if isInTestMode:
            print(f"LoadHistory: 开始加载 {self.history_file}")
        # 如果没有json聊天记录文件，则新建一个
        if not (os.path.exists(self.history_file)):
            self.CreateEmptyHistoryFile()
            self.raw_message = self.GetDefaultMessageForMode(self.current_mode)
            # 显示默认系统消息
            if self.raw_message and self.raw_message[0]["role"] == "system":
                self.DisplayMessage("system", self.raw_message[0]["content"])
            return

        # 文件在，则尝试读取内容
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                # 如果文件是空的，就不新建文件，但也显示默认消息
                if not content:
                    self.raw_message = self.GetDefaultMessageForMode(self.current_mode)
                    self.DisplayMessage("system", self.raw_message[0]["content"])
                    return
                # 文件有内容，正常加载
                self.raw_message = json.loads(content)

                # 过滤掉标记之间的文件内容
                filtered_messages = []
                for msg in self.raw_message:
                    if msg["role"] == "user" and "【文件内容开始】" in msg["content"]:
                        # 提取标记外的部分
                        import re
                        content = msg["content"]
                        # 删除标记及其之间的内容
                        cleaned = re.sub(r'【文件内容开始】.*?【文件内容结束】', '', content, flags=re.DOTALL)
                        if cleaned.strip():
                            msg["content"] = cleaned
                            filtered_messages.append(msg)
                        # 如果清理后为空，就不加这条消息
                    else:
                        filtered_messages.append(msg)

                self.raw_message = filtered_messages

                # 清空WebView，准备显示历史消息
                self.clear_webview()
                # 显示过滤后的历史（从第一条开始）
                for msg in self.raw_message:
                    self.DisplayMessage(msg["role"], msg["content"])

        except json.JSONDecodeError as e:
            # JSON 解析失败（文件损坏）
            if isInTestMode:
                print(f"⚠️ LoadHistory: JSON解析失败，将使用默认配置: {e}")
            self.raw_message = self.GetDefaultMessageForMode(self.current_mode)
            self.DisplayMessage("system", self.raw_message[0]["content"])

        except PermissionError as e:
            # 权限不足（熊孩子的电脑！）
            if isInTestMode:
                print(f"⚠️ LoadHistory: 无法读取历史文件（权限不足），将使用默认配置: {e}")
            self.raw_message = self.GetDefaultMessageForMode(self.current_mode)
            self.DisplayMessage("system", f"⚠️ 无法读取历史记录文件（权限不足）\n\n{self.raw_message[0]['content']}")

        except Exception as e:
            # 其他未知错误
            if isInTestMode:
                print(f"⚠️ LoadHistory: 未知错误，将使用默认配置: {e}")
            self.raw_message = self.GetDefaultMessageForMode(self.current_mode)
            self.DisplayMessage("system", f"⚠️ 读取历史记录失败\n\n{self.raw_message[0]['content']}")

    def CreateEmptyHistoryFile(self):
        if isInTestMode:
            print(f"CreateEmptyHistoryFile: 创建空文件 {self.history_file}")
        # 创建一个空的json文件，只写一个空对象占位
        if os.path.exists(self.history_file):
            return
        else:
            with open(self.history_file, "w", encoding="utf-8") as f:
                # 写一个空列表占位，实际不会用到
                json.dump([], f)

    def GetDefaultMessage(self):
        # 返回系统的默认提示
        return [
            {"role": "system", "content": "等待你发来第一条消息～"}
        ]

    def CallbackStaticMode(self, mode="chat", retries=5):
        for attempt in range(retries):
            try:
                api_key, api_url = get_api_key_for_mode(mode)
                client = OpenAI(api_key=api_key,
                                base_url=api_url)
                response = client.chat.completions.create(model="deepseek-chat",
                                                          messages=self.raw_message,
                                                          stream=False,
                                                          timeout=30)  # 添加一个超时设置，防止卡死
                reply = response.choices[0].message.content

                self.DisplayMessage("assistant", reply)
                self.raw_message.append({"role": "assistant", "content": reply})
                self.SaveHistory()
                # 恢复正常状态
                self.update_system_info("normal")
                return  # 代码执行成功就返回
            except Exception as e:
                if attempt < retries - 1:
                    self.DisplayMessage("system", f"请求失败，正在重试（{attempt + 1}/{retries}）...")
                    QApplication.processEvents()
                    time.sleep(1)  # 等待1秒再试
                else:
                    self.update_system_info("normal")  # 出错也恢复
                    self.DisplayMessage("system", f"错误：{str(e)}，已重试{retries}次")

    def UpdateLastAssistantMessage(self, content):
        """更新最后一条助手消息 - 极简安全版"""
        from datetime import datetime
        import json

        # 根据当前模式选择前缀
        if self.current_mode == "code":
            prefix = code_prefix_1
            font_family = code_font_1
            font_size = code_size_1
            color = code_assistant_color
            bg = code_bg_1
        elif self.current_mode.startswith("research"):
            if self.current_mode == "research_api":
                prefix = research_prefix_1
            elif self.current_mode == "research_desensitize":
                prefix = research_prefix_2
            else:  # research_local
                prefix = research_prefix_3
            font_family = research_font_1
            font_size = research_size_1
            color = research_assistant_color
            bg = research_bg_1
        else:  # chat模式
            prefix = assistant_prefix_1
            font_family = assistant_font_1
            font_size = assistant_size_1
            color = assistant_color_1
            bg = assistant_bg_1

        # 极简处理：只转义HTML特殊字符，防止XSS和格式错误
        display_content = (content
                           .replace('&', '&amp;')
                           .replace('<', '&lt;')
                           .replace('>', '&gt;')
                           .replace('"', '&quot;')
                           .replace("'", '&#39;')
                           .replace('\n', '<br>'))  # 保留换行

        # 构造最简单的消息HTML
        message_html = f"""
        <div class="message assistant" style="font-family:{font_family}; font-size:{font_size}px; color:{color}; margin:10px 0; padding:10px; border-radius:8px; {f'background-color:{bg};' if bg else ''}">
            <div class="timestamp" style="font-size:12px; color:#999; margin-bottom:5px;">{datetime.now().strftime('%H:%M:%S')}</div>
            <div class="content">
                <b>{prefix}</b> {display_content}
            </div>
        </div>
        """

        # 使用json.dumps确保字符串安全传递给JavaScript
        safe_html = json.dumps(message_html)

        js = f"""
        (function() {{
            var container = document.getElementById('chat-container');
            if (!container) return;

            // 删除最后一条消息
            if (container.lastChild) {{
                container.removeChild(container.lastChild);
            }}

            // 添加新消息
            var div = document.createElement('div');
            div.innerHTML = {safe_html};
            container.appendChild(div.firstElementChild);

            // 滚动到底部
            container.scrollTop = container.scrollHeight;
        }})();
        """

        try:
            self.web_displayer.page().runJavaScript(js)
        except Exception as e:
            if isInTestMode:
                print(f"更新消息失败: {e}")
            # 如果JavaScript执行失败，至少尝试用普通方式显示
            self.DisplayMessage("assistant", content)

    def CallbackStreamMode(self, mode="chat", retries=5):
        for attempt in range(retries):
            try:
                api_key, api_url = get_api_key_for_mode(mode)
                client = OpenAI(api_key=api_key, base_url=api_url)
                stream = client.chat.completions.create(model="deepseek-chat",
                                                        messages=self.raw_message,
                                                        stream=True,
                                                        timeout=30,
                                                        max_tokens=8192)
                placeholder_index = len(self.raw_message)
                self.raw_message.append({"role": "assistant", "content": ""})

                full_response = ""
                is_first_chunk = True
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        if is_first_chunk:
                            self.DisplayMessage("assistant", full_response)
                            is_first_chunk = False
                        else:
                            self.UpdateLastAssistantMessage(full_response)
                        QApplication.processEvents()

                self.raw_message[placeholder_index]["content"] = full_response
                self.SaveHistory()
                return

            except Exception as e:
                if attempt < retries - 1:
                    self.DisplayMessage("system", f"流式请求失败，正在重试（{attempt + 1}/{retries}）...")
                    QApplication.processEvents()
                    time.sleep(1)
                else:
                    self.DisplayMessage("system", f"流式错误：{str(e)}，已重试{retries}次")

    def CallbackLocalMode(self):
        try:
            # 获取用户最后一条信息
            user_message = self.raw_message[-1]["content"]

            # 如果是科研模式，自动加个系统提示
            # 如果是科研模式（任何 research 开头）
            if self.current_mode == "research_local":
                full_prompt = f"{research_system_prompt}\n\n用户数据：\n{user_message}"
            else:
                full_prompt = user_message

            # 调用本地Ollama
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "deepseek-r1:7b",
                    "prompt": full_prompt,  # 这里用 full_prompt，不是 user_message
                    "stream": False
                }
            )

            if response.status_code == 200:
                reply = response.json()["response"]
                self.DisplayMessage("assistant", reply)
                self.raw_message.append({"role": "assistant", "content": reply})
                self.SaveHistory()
            else:
                self.DisplayMessage("system", f"本地模型调用失败：{response.status_code}")
            # 恢复正常状态
            self.update_system_info("normal")

        except Exception as e:
            # 恢复正常状态
            self.update_system_info("normal")
            self.DisplayMessage("system", f"本地模型错误：{str(e)}")

    def SendMessageFunc(self):
        # 首先获取用户输入
        user_text = self.ui0.text_message_input.toPlainText().strip()

        # 如果有上传的文件，自动附加文件内容
        if hasattr(self, 'current_file_path') and self.current_file_path:
            file_path = self.current_file_path
            file_name = os.path.basename(file_path)
            # 把文件内容加到 raw_message 里

            try:
                # 根据文件类型读取内容
                if file_path.endswith('.txt'):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    user_text = f"【上传了TXT文件】\n文件名：{file_name}\n大小：{file_size} 字节\n\n【用户要求】\n{user_text}"
                    self.current_file_content = file_content

                elif file_path.endswith('.docx'):
                    from docx import Document
                    doc = Document(file_path)
                    content = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    user_text = f"【上传了Word文档】\n文件名：{file_name}\n大小：{file_size} 字节\n\n【用户要求】\n{user_text}"
                    self.current_file_content = content

                elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                    import pandas as pd
                    df = pd.read_excel(file_path)
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    rows, cols = df.shape
                    content = df.to_string()
                    user_text = f"【上传了Excel文件】\n文件名：{file_name}\n大小：{file_size} 字节\n行数：{rows}，列数：{cols}\n\n【用户要求】\n{user_text}"
                    self.current_file_content = content

                elif file_path.endswith('.pdf'):
                    import PyPDF2
                    with open(file_path, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        content = ''
                        for page in reader.pages:
                            content += page.extract_text() + '\n'
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    user_text = f"【上传了PDF文件】\n文件名：{file_name}\n大小：{file_size} 字节\n\n【用户要求】\n{user_text}"
                    self.current_file_content = content

                # 加标记存文件内容
                marked_content = f"【文件内容开始】\n{self.current_file_content}\n【文件内容结束】"
                self.raw_message.append({"role": "user", "content": marked_content})

                # 清除已上传的文件标记
                delattr(self, 'current_file_path')
                delattr(self, 'current_file_content')

            except Exception as e:
                self.DisplayMessage("system", f"文件读取失败：{str(e)}")
                return

        # 如果发送到消息是提示词或者新内容，不发送
        if not user_text or user_text == self.input_placeholder:
            return

        # 显示用户消息
        self.DisplayMessage("user", user_text)
        # 发完后清空
        self.ui0.text_message_input.clear()
        # 恢复提示词
        self.ui0.text_message_input.setPlainText(self.input_placeholder)
        # 添加到历史消息中
        self.raw_message.append({"role": "user", "content": user_text})

        # 调用API之前
        if (self.current_mode in ["research_api", "research_local", "code", "research_desensitize"]) and is_stream_mode:
            self.is_calculating = True
            self.update_system_info("busy")
            QApplication.processEvents()

        # 调用API
        if self.current_mode == "chat":
            if is_stream_mode:
                self.CallbackStreamMode("chat")
            else:
                self.CallbackStaticMode("chat")
        elif self.current_mode == "research_api":
            # 从知识库检索相关内容
            kb_context = self.search_knowledge_base(user_text)

            # 如果有检索结果，拼接到用户消息中
            if kb_context:
                enhanced_text = f"""【知识库资料】
            {kb_context}

            【用户问题】
            {user_text}

            请基于以上知识库资料回答用户的问题。如果资料中没有相关信息，请用自己的知识回答。"""
            else:
                enhanced_text = user_text

            # 用增强后的文本替换原始用户消息
            # 注意：需要临时替换 raw_message 中的最后一条用户消息
            self.raw_message[-1]["content"] = enhanced_text

            # 调用 API
            if is_stream_mode:
                self.CallbackStreamMode("research_api")
            else:
                self.CallbackStaticMode("research_api")

            # 恢复原始用户消息（用于保存历史）
            self.raw_message[-1]["content"] = user_text
        elif self.current_mode == "research_desensitize":
            self.DisplayMessage("system", "脱敏模式正在开发中...")
        elif self.current_mode == "research_local":
            self.CallbackLocalMode()
        elif self.current_mode == "code":
            if is_stream_mode:
                self.CallbackStreamMode("code")
            else:
                self.CallbackStaticMode("code")

        self.is_calculating = False
        self.update_system_info("normal")

    def clear_webview(self):
        js = "document.getElementById('chat-container').innerHTML = '';"
        self.web_displayer.page().runJavaScript(js)

    def ClearChat(self):
        global isInTestMode
        self.clear_webview()
        if isInTestMode:
            os.remove(self.history_file)
        self.raw_message = self.GetDefaultMessageForMode(self.current_mode)

    def init_web_template(self):
        """初始化HTML模板"""
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                html, body {
                    height: 100%;
                    overflow: hidden;  /* 防止body滚动 */
                }
                body { 
                    font-family: 'Microsoft YaHei', sans-serif; 
                    padding: 0; 
                    margin: 0; 
                    background-color: #1b1b1c;
                    color: #e0e0e0;
                    height: 100%;
                    display: flex;
                    flex-direction: column;
                }
                #chat-container { 
                    flex: 1;
                    overflow-y: auto;  /* 关键！让这个容器可以滚动 */
                    padding: 10px;
                    background-color: #1b1b1c;
                    /* 喵～添加平滑滚动效果 */
                    scroll-behavior: smooth;
                }
                .message { 
                    margin: 10px 0; 
                    padding: 10px; 
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    word-wrap: break-word;
                }
                .user { 
                    background: #3a3a3a; 
                    margin-left: 20%; 
                    border-left: 4px solid #696969;
                }
                .assistant { 
                    background: #2a2a2a; 
                    margin-right: 20%; 
                    border-left: 4px solid #9c27b0;
                }
                .system { 
                    background: #252525; 
                    color: #666; 
                    font-style: italic;
                    border-left: 4px solid #ff9800;
                }
                .timestamp { 
                    font-size: 12px; 
                    color: #999; 
                    margin-bottom: 5px; 
                }
                .code-block { 
                    background: #0d0d0d; 
                    color: #abb2bf; 
                    padding: 10px; 
                    border-radius: 5px;
                    font-family: 'Consolas', monospace;
                    white-space: pre-wrap;
                    margin: 10px 0;
                    overflow-x: auto;
                }
            </style>
        </head>
        <body>
            <div id="chat-container"></div>

            <script>
            // 全局安全的添加消息函数
            function safeAddMessage(html) {
                try {
                    var container = document.getElementById('chat-container');
                    if (!container) {
                        console.error('chat-container not found');
                        return false;
                    }
                    var div = document.createElement('div');
                    div.innerHTML = html;
                    container.appendChild(div.firstElementChild);
                    container.scrollTop = container.scrollHeight;
                    return true;
                } catch(e) {
                    console.error('添加消息失败:', e);
                    return false;
                }
            }
            </script>
        </body>
        </html>
        """
        self.web_displayer.setHtml(html_template)

    # 统一显示消息，样式从环境变量读取
    def DisplayMessage(self, role, content):
        if isInTestMode:
            print(f"DEBUG: content type: {type(content)}, content preview: {content[:100]}")

        # 首先转义尖括号（但保留Markdown渲染后的HTML标签）
        if not (self.current_mode.startswith("research") or self.current_mode == "code"):
            content = content.replace('&lt;', '&lt;').replace('&gt;', '&gt;')

        # ---------- Markdown 渲染 ----------
        if self.current_mode.startswith("research") or self.current_mode == "code" or self.current_mode == "chat":
            try:
                import markdown
                md = markdown.Markdown(extensions=['extra', 'nl2br', 'tables'])
                content = md.convert(content)
            except Exception as e:
                print(f"Markdown渲染失败: {e}")
                content = content.replace('&lt;', '&lt;').replace('&gt;', '&gt;')

        # 根据角色选择配置
        if role == "user":
            if self.current_mode.startswith("research"):
                font_family = research_font_1
                font_size = research_size_1
                color = research_color_1
                bg = research_bg_1
                prefix = user_prefix_research
                # 输入框字体
                input_font = QFont(font_family, font_size)
                self.ui0.text_message_input.setFont(input_font)
            elif self.current_mode == "code":
                font_family = code_font_1
                font_size = code_size_1
                color = code_color_1
                bg = code_bg_1
                prefix = user_prefix_code
                # 输入框字体
                input_font = QFont(font_family, font_size)
                self.ui0.text_message_input.setFont(input_font)
            else:
                font_family = user_font_1
                font_size = user_size_1
                color = user_color_1
                bg = user_bg_1
                prefix = user_prefix_chat
                # 输入框字体
                input_font = QFont(font_family, font_size)
                self.ui0.text_message_input.setFont(input_font)

        elif role == "assistant":
            if self.current_mode == "research_api":
                font_family = research_font_1
                font_size = research_size_1
                color = research_assistant_color
                prefix = research_prefix_1
                bg = research_bg_1
            elif self.current_mode == "research_desensitize":
                font_family = research_font_1
                font_size = research_size_1
                color = research_assistant_color
                prefix = research_prefix_2
                bg = research_bg_1
            elif self.current_mode == "research_local":
                font_family = research_font_1
                font_size = research_size_1
                color = research_assistant_color
                prefix = research_prefix_3
                bg = research_bg_1
            elif self.current_mode == "code":
                font_family = code_font_1
                font_size = code_size_1
                color = code_assistant_color
                prefix = code_prefix_1
                bg = code_bg_1
            else:
                font_family = assistant_font_1
                font_size = assistant_size_1
                color = assistant_color_1
                prefix = assistant_prefix_1
                bg = assistant_bg_1

        else:  # system
            font_family = system_font_1  # ✅ 添加系统字体
            font_size = system_size_1  # ✅ 添加系统字号
            color = system_color_1  # ✅ 添加系统颜色
            prefix = system_prefix_1  # ✅ 添加系统前缀
            bg = ""  # 系统消息无背景

        # 对于代码模式，特殊处理代码块
        if self.current_mode == "code" and "```" in content and not content.startswith('<'):
            content = content.replace('```', '')
            content = f'<pre style="font-family:Consolas, monospace; background:#2d2d2d; padding:10px; border-radius:5px; margin:10px 0; color:#e0e0e0; white-space:pre-wrap;">{content}</pre>'

        # 构造消息的 HTML
        message_html = f"""
        <div class="message {role}" style="font-family:{font_family}; font-size:{font_size}px; color:{color}; margin:10px 0; padding:10px; border-radius:8px; {f'background-color:{bg};' if bg else ''}">
            <div class="timestamp" style="font-size:12px; color:#999; margin-bottom:5px;">{time.strftime('%H:%M:%S')}</div>
            <div class="content">
                <b>{prefix}</b> {content}
            </div>
        </div>
        """

        if not self.webview_ready:
            self.pending_messages.append(message_html)
            if isInTestMode:
                print(f"WebView未就绪，消息暂存，当前暂存数: {len(self.pending_messages)}")
            return

        self.add_message_to_webview(message_html)

    def format_code_for_web(self, html_content):
        """格式化代码块为WebView友好的格式"""
        import re

        # 将 ```language\ncode``` 转换为带样式的代码块
        def replace_code_block(match):
            language = match.group(1) or "plaintext"
            code = match.group(2)
            # 转义HTML特殊字符
            code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

            # 检查是否是命令行输出
            lines = code.split('\n')
            formatted_lines = []
            for line in lines:
                if line.strip().startswith('$') or '❯' in line:
                    # 命令行提示符样式
                    formatted_lines.append(f'<span style="color: #98c379;">{line}</span>')
                elif 'error' in line.lower() or 'failed' in line.lower() or '❌' in line:
                    # 错误信息样式
                    formatted_lines.append(f'<span style="color: #e06c75;">{line}</span>')
                elif 'warning' in line.lower() or '⚠️' in line:
                    # 警告信息样式
                    formatted_lines.append(f'<span style="color: #e5c07b;">{line}</span>')
                else:
                    # 普通输出
                    formatted_lines.append(line)

            code = '<br>'.join(formatted_lines)

            return f'''
            <div class="code-block" style="background:#282c34; color:#abb2bf; padding:15px; border-radius:8px; font-family:'Consolas', 'Monaco', monospace; margin:15px 0; border-left:4px solid #61afef;">
                <div style="display:flex; justify-content:space-between; margin-bottom:10px; padding-bottom:5px; border-bottom:1px solid #3e4451;">
                    <span style="color:#98c379;">{language}</span>
                    <span style="color:#61afef; cursor:pointer;" onclick="copyToClipboard(this)">📋 复制</span>
                </div>
                <pre style="margin:0; white-space:pre-wrap; word-wrap:break-word; font-size:13px; line-height:1.5;">{code}</pre>
            </div>
            '''

        pattern = r'```(\w*)\n(.*?)```'
        return re.sub(pattern, replace_code_block, html_content, flags=re.DOTALL | re.MULTILINE)

    def update_system_info(self, status="normal", message=None):
        """更新左上角的系统信息框
        status: "normal" 正常状态（黑底白字）
                "busy"   忙碌状态（黄底黑字）
                "offline" 离线状态（红底白字）
        """
        # 根据状态设置颜色
        if status == "normal":
            bg_color = "#000000"  # 黑色
            text_color = "#FFFFFF"  # 白色

            # 模式信息
            mode_names = {
                "chat": "💬 聊天模式",
                "research_api": "📊 科研助手-在线",
                "research_desensitize": "🔒 科研助手-脱敏",
                "research_local": "💻 科研助手-本地",
                "code": "👨‍💻 代码助手",
            }
            mode_name = mode_names.get(self.current_mode, self.current_mode)

            # 流式状态
            if (self.current_mode not in ["research_local"]) and is_stream_mode:
                status_text = "🟢 流式传输（实时）"
                note = "消息会逐字出现"
            else:
                status_text = "🟡 静态模式"
                note = "AI正在计算，请勿重复发送"

            info = f"""
            <b>{mode_name}</b><br>
            {status_text}<br>
            <small>{note}</small>
            """

        elif status == "busy":
            bg_color = "#FFF9C4"  # 浅黄色
            text_color = "#000000"  # 黑色

            if message:
                info = message
            else:
                info = """
                <b>⏳ AI模型正在计算</b><br>
                <small style="color:#666;">请勿重复发送消息</small>
                """

        else:  # offline 状态
            bg_color = "#FF4444"  # 红色
            text_color = "#FFFFFF"  # 白色

            if message:
                info = message
            else:
                info = """
                <b>⚠️ 网络连接已断开</b><br>
                <small>请检查网络后重试</small>
                """

        # 设置样式和内容
        self.ui0.list_system_info.setStyleSheet(f"""
            QTextBrowser {{
                background-color: {bg_color};
                color: {text_color};
                border: none;
                padding: 8px;
                font-size: 14px;
            }}
        """)
        self.ui0.list_system_info.setHtml(info)

    def reload_config(self):
        """重新加载配置（设置更改后调用，即时生效）"""
        from dotenv import load_dotenv

        # 重新加载环境变量
        env_path = init_config.get_env_path()
        load_dotenv(env_path, override=True)

        # 更新全局变量
        global user_font_1, user_size_1, user_color_1, user_bg_1
        global user_prefix_chat, user_prefix_research, user_prefix_code
        global assistant_font_1, assistant_size_1, assistant_color_1, assistant_bg_1
        global assistant_prefix_1, chat_assistant_prompt
        global research_font_1, research_size_1, research_color_1, research_bg_1
        global research_prefix_1, research_prefix_2, research_prefix_3
        global code_font_1, code_size_1, code_color_1, code_bg_1
        global code_prefix_1, code_assistant_prompt
        global system_font_1, system_size_1, system_color_1, system_prefix_1, system_style
        global input_font_1, input_size_1, input_color_1, input_bg_1, input_placeholder_color_1
        global is_stream_mode, research_system_prompt

        # ===== 聊天模式 =====
        user_font_1 = os.getenv("USER_FONT_1", "").strip('"')
        user_size_1 = int(os.getenv("USER_SIZE_1", 16))
        user_color_1 = os.getenv("USER_COLOR_1", "#3C3C3C")
        user_bg_1 = os.getenv("USER_BG_1", "")

        user_prefix_chat = os.getenv("USER_PREFIX_CHAT", "用户：")

        assistant_font_1 = os.getenv("ASSISTANT_FONT_1", "").strip('"')
        assistant_size_1 = int(os.getenv("ASSISTANT_SIZE_1", 16))
        assistant_color_1 = os.getenv("ASSISTANT_COLOR_1", "#0078D7")
        assistant_bg_1 = os.getenv("ASSISTANT_BG_1", "")
        assistant_prefix_1 = os.getenv("ASSISTANT_PREFIX", "助手：")
        chat_assistant_prompt = os.getenv("CHAT_ASSISTANT_PROMPT", "")

        # ===== 科研助手模式 =====
        user_prefix_research = os.getenv("USER_PREFIX_RESEARCH", "📊用户：")

        research_font_1 = os.getenv("RESEARCH_USER_FONT", "").strip('"')
        research_size_1 = int(os.getenv("RESEARCH_USER_SIZE", 16))
        research_color_1 = os.getenv("RESEARCH_USER_COLOR", "#2E86AB")  # 科研用户颜色
        research_assistant_color = os.getenv("RESEARCH_ASSISTANT_COLOR", "#2E86AB")  # ✅ 科研助手颜色
        research_bg_1 = os.getenv("RESEARCH_BG", "")

        research_prefix_1 = os.getenv("RESEARCH_PREFIX_1", "📊科研助手：")
        research_prefix_2 = os.getenv("RESEARCH_PREFIX_2", "🔒科研助手（脱敏）：")
        research_prefix_3 = os.getenv("RESEARCH_PREFIX_3", "💻科研助手（本地）：")
        research_system_prompt = os.getenv("RESEARCH_SYSTEM_PROMPT", "科研助理模式")

        # ===== 代码助手模式 =====
        user_prefix_code = os.getenv("USER_PREFIX_CODE", "👨‍💻用户：")

        code_font_1 = os.getenv("CODE_USER_FONT", "").strip('"')
        code_size_1 = int(os.getenv("CODE_USER_SIZE", 16))
        code_color_1 = os.getenv("CODE_USER_COLOR", "#28A745")  # 代码用户颜色
        code_assistant_color = os.getenv("CODE_ASSISTANT_COLOR", "#28A745")  # ✅ 代码助手颜色
        code_bg_1 = os.getenv("CODE_BG", "")

        code_prefix_1 = os.getenv("CODE_PREFIX", "👨‍💻代码助手：")
        code_assistant_prompt = os.getenv("CODE_ASSISTANT_PROMPT", "")

        # 系统消息
        system_font_1 = os.getenv("SYSTEM_FONT_1", "").strip('"')
        system_size_1 = int(os.getenv("SYSTEM_SIZE_1", 16))
        system_color_1 = os.getenv("SYSTEM_COLOR_1", "#999999")
        system_prefix_1 = os.getenv("SYSTEM_PREFIX_1", "系统")
        system_style = os.getenv("SYSTEM_STYLE_1", "italic")

        input_font_1 = os.getenv("INPUT_FONT_1", "").strip('"')
        input_size_1 = int(os.getenv("INPUT_SIZE_1", 16))
        input_color_1 = os.getenv("INPUT_COLOR_1", "#333333")
        input_bg_1 = os.getenv("INPUT_BG_1", "#FFFFFF")
        input_placeholder_color_1 = os.getenv("INPUT_PLACEHOLDER_COLOR_1", "#999999")

        is_stream_mode = os.getenv("IS_STREAM_MODE", "false").lower() == "true"

        # 更新输入框字体
        input_font = QFont(input_font_1, input_size_1)
        self.ui0.text_message_input.setFont(input_font)

        # 更新输入框提示词
        self.input_placeholder = self.input_placeholder_presets.get(self.current_mode, "输入你想发送的消息～")
        self.ui0.text_message_input.setPlaceholderText(self.input_placeholder)

        # ===== 更新当前模式的人设 =====
        new_system_prompt = ""
        if self.current_mode == "chat":
            new_system_prompt = chat_assistant_prompt
        elif self.current_mode == "research_api":
            new_system_prompt = research_system_prompt
        elif self.current_mode == "code":
            new_system_prompt = code_assistant_prompt
        else:
            new_system_prompt = research_system_prompt

        # 更新 raw_message 中的第一条 system 消息
        if len(self.raw_message) > 0 and self.raw_message[0]["role"] == "system":
            self.raw_message[0]["content"] = new_system_prompt
        else:
            self.raw_message.insert(0, {"role": "system", "content": new_system_prompt})

        # 更新系统信息框
        self.update_system_info("normal")

        # ===== 重新渲染聊天窗口 =====
        self.clear_webview()
        for msg in self.raw_message:
            self.DisplayMessage(msg["role"], msg["content"])

        # 滚动到底部
        QTimer.singleShot(100, lambda: self.web_displayer.page().runJavaScript(
            "var c=document.getElementById('chat-container');if(c)c.scrollTop=c.scrollHeight;"
        ))

        # 发送系统通知
        self.DisplayMessage("system", "✨ 配置已更新，新设置已生效。")

        if init_config.isInTestMode:
            print(f"✅ 配置已重新加载")
            print(f"   聊天用户颜色: {user_color_1}, 聊天助手颜色: {assistant_color_1}")
            print(f"   科研用户颜色: {research_color_1}, 科研助手颜色: {research_assistant_color}")
            print(f"   代码用户颜色: {code_color_1}, 代码助手颜色: {code_assistant_color}")


if __name__ == "__main__":
    # === 高DPI适配：让Qt自己处理，Windows不要插手 ===
    if platform.system() == 'Windows':
        # 1. 告诉 Windows：不要虚拟化DPI，我自己处理
        try:
            from ctypes import windll

            windll.user32.SetProcessDPIAware()
        except:
            pass

        # 2. 告诉 Qt：启用高DPI缩放（Qt6 默认已启用，但显式设置更保险）
        from PySide6.QtCore import Qt

        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

        # 3. 关键：告诉 Qt 的缩放策略为“PassThrough”（按实际DPI缩放，不要四舍五入）
        QApplication.setHighDpiScaleFactorRoundingPolicy(
            Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
        )

    app = QApplication([])
    window = MainWindowWidget()
    window.show()
    app.exec()
