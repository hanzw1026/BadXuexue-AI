# -*- coding: utf-8 -*-
"""
多模态助手业务逻辑模块
支持文本、图片、Office文档、PDF的混合输入
"""

import os
import re
import json
import time
import requests
from PySide6.QtWidgets import QFileDialog, QMenu, QMessageBox
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QAction
from openai import OpenAI

import init_config

isInTestMode = init_config.isInTestMode


class MultimodalHandler(QObject):
    """多模态助手处理器"""

    # 定义信号
    message_signal = Signal(str, str)  # role, content
    update_last_message_signal = Signal(str)  # 更新最后一条消息
    clear_webview_signal = Signal()

    def __init__(self, parent, web_displayer, config):
        super().__init__(parent)
        self.parent = parent
        self.web_displayer = web_displayer
        self.config = config

        # API配置
        self.api_key = config.get("MULTIMODAL_API_KEY", "")
        self.api_url = config.get("MULTIMODAL_API_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
        self.model = config.get("MULTIMODAL_PROVIDER", "qwen3-vl-plus")
        # 判断是否需要开启思考模式
        self.enable_thinking = config.get("MULTIMODAL_ENABLE_THINKING", "false").lower() == "true"
        self.temperature = 0.7

        # 多模态专用状态
        self.current_images = []  # 当前上传的图片路径列表
        self.current_files = []  # 当前上传的文件信息列表 [{"name": xx, "content": xx}]

        # 流式响应状态
        self.is_streaming = False
        self.current_full_response = ""
        self.current_placeholder_index = -1

        # 会话历史（raw_message）
        self.raw_message = []

        # 加载系统提示词
        self._load_system_prompt()

    def _load_system_prompt(self):
        """加载多模态系统提示词"""
        import os
        self.system_prompt = os.getenv("MULTIMODAL_SYSTEM_PROMPT",
                                       "你是多模态和图像助手")

    def get_api_key(self):
        """获取API Key"""
        return self.api_key

    def set_api_key(self, key):
        """设置API Key"""
        self.api_key = key

    def _read_file_content(self, file_path):
        """读取文件内容（复用main.py的逻辑）"""
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        elif file_path.endswith('.docx'):
            from docx import Document
            doc = Document(file_path)
            return '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            import pandas as pd
            df = pd.read_excel(file_path)
            return df.to_string()
        elif file_path.endswith('.pdf'):
            import PyPDF2
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                content = ''
                for page in reader.pages:
                    content += page.extract_text() + '\n'
                return content
        else:
            return ""

    def upload_file(self, file_path):
        """处理文件上传（图片/Office/PDF）"""
        print(f"🔍 upload_file 被调用，file_path={file_path}")
        print(f"🔍 当前 current_images 长度: {len(self.current_images)}")

        if not file_path:
            return None

        ext = os.path.splitext(file_path)[1].lower()

        if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
            # 图片：存储路径并生成预览
            self.current_images.append(file_path)
            print(f"🔍 图片已添加，current_images 长度: {len(self.current_images)}")
            self._add_image_preview(file_path)
            if isInTestMode:
                print(f"📸 已上传图片: {os.path.basename(file_path)}")
            return "image"
        else:
            # Office/PDF：提取文本内容
            try:
                content = self._read_file_content(file_path)
                self.current_files.append({
                    "path": file_path,
                    "name": os.path.basename(file_path),
                    "content": content
                })
                self.message_signal.emit("system", f"📎 已附加文件：{os.path.basename(file_path)}")
                if isInTestMode:
                    print(f"📄 已上传文件: {os.path.basename(file_path)}，内容长度: {len(content)}")
                return "document"
            except Exception as e:
                self.message_signal.emit("system", f"❌ 文件读取失败：{str(e)}")
                return None

    def _image_to_base64(self, image_path):
        """将本地图片转换为 Base64 编码"""
        import base64

        with open(image_path, "rb") as f:
            image_data = f.read()

        # 获取图片格式
        ext = os.path.splitext(image_path)[1].lower()
        mime_type = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.bmp': 'image/bmp',
            '.webp': 'image/webp'
        }.get(ext, 'image/jpeg')

        base64_str = base64.b64encode(image_data).decode('utf-8')
        return f"data:{mime_type};base64,{base64_str}"

    def clear_uploads(self):
        """清空当前上传的图片和文件"""
        self.current_images.clear()
        self.current_files.clear()
        if isInTestMode:
            print("🗑️ 已清空上传的图片和文件")

    def _add_image_preview(self, image_path):
        """在聊天区域添加图片预览（复用 _image_to_base64）"""
        import time

        img_src = self._image_to_base64(image_path)

        html = f'''
        <div class="message user" style="margin: 10px 0; padding: 10px; border-radius: 8px; background-color: #3a3a3a;">
            <div class="timestamp" style="font-size: 12px; color: #999; margin-bottom: 5px;">{time.strftime('%H:%M:%S')}</div>
            <div class="content">
                <b>📸 图片预览：</b><br>
                <div style="position: relative; display: inline-block;">
                    <img src="{img_src}" style="max-width: 200px; max-height: 200px; border-radius: 8px; margin-top: 5px;">
                    <span style="position: absolute; top: -5px; right: -5px; background: rgba(0,0,0,0.5); color: white; border-radius: 50%; width: 20px; height: 20px; text-align: center; cursor: pointer;"
                          onclick="this.parentElement.parentElement.remove()">✖</span>
                </div>
            </div>
        </div>
        '''

        self.message_signal.emit("user_preview", html)

    def send_message(self, user_text):
        """发送多模态消息"""
        print(f"🔍 send_message 被调用，current_images 长度: {len(self.current_images)}")
        print(f"🔍 调用栈: 检查是谁调用了 send_message")

        if not self.api_key:
            self.message_signal.emit("system", "⚠️ 请先在设置中配置多模态API Key")
            return

        # 检查是否有内容
        if not user_text.strip() and not self.current_images and not self.current_files:
            return

        # 添加用户消息到历史
        self._append_user_message(user_text)

        # 显示用户消息（不带文件内容）
        if self.current_images:
            self.message_signal.emit("user", f"📸【附带 {len(self.current_images)} 张图片】\n{user_text}")
        elif self.current_files:
            self.message_signal.emit("user", f"📎【附带 {len(self.current_files)} 个文件】\n{user_text}")
        else:
            self.message_signal.emit("user", user_text)

        # 构造API请求的content数组
        api_content = self._build_api_content(user_text)

        # 在 send_message 方法中，api_content = self._build_api_content(user_text) 后面添加
        print(f"🔍 api_content 构造完成，类型: {type(api_content)}")
        if isinstance(api_content, list):
            print(f"🔍 api_content 包含 {len(api_content)} 个元素")
            for item in api_content:
                if isinstance(item, dict) and item.get('type') == 'image_url':
                    print(f"🔍 发现图片: {item.get('image_url', {}).get('url', '')[:80]}...")

        # 调用API
        is_stream = os.getenv("IS_STREAM_MODE", "false").lower() == "true"
        if is_stream:
            self._call_stream(api_content)
        else:
            self._call_static(api_content)

        # 清空上传的图片和文件（发送后清空，避免重复）
        self.clear_uploads()

    # def _append_user_message(self, user_text):
    #     """添加用户消息到历史"""
    #     # 如果有图片或文件，存带标记的版本
    #     if self.current_images or self.current_files:
    #         # 构造标记内容（用于AI理解）
    #         marked_parts = []
    #         if self.current_images:
    #             marked_parts.append(f"【图片{len(self.current_images)}张】")
    #         if self.current_files:
    #             for f in self.current_files:
    #                 marked_parts.append(f"【文件：{f['name']}】\n{f['content']}")
    #         marked_parts.append(f"【用户要求】\n{user_text}")
    #         marked_content = "\n".join(marked_parts)
    #         self.raw_message.append({"role": "user", "content": marked_content})
    #     else:
    #         self.raw_message.append({"role": "user", "content": user_text})

    def _append_user_message(self, user_text):
        """添加用户消息到历史"""
        if self.current_images:
            # 用特殊标记包裹图片路径
            img_paths_str = "【图片路径】" + "|".join(self.current_images) + "【图片路径结束】"
            if user_text.strip():
                full_content = img_paths_str + "\n" + user_text
            else:
                full_content = img_paths_str
            self.raw_message.append({"role": "user", "content": full_content})
        else:
            self.raw_message.append({"role": "user", "content": user_text})

    def _build_api_content(self, user_text):
        """构造API请求的content数组"""
        content = []

        """构造API请求的content数组"""
        content = []

        print(f"🔍 _build_api_content: current_images = {self.current_images}")
        print(f"🔍 _build_api_content: current_files = {self.current_files}")

        # 添加图片（转为 base64 格式）
        for img_path in self.current_images:
            print(f"🔍 正在处理图片: {img_path}")
            img_base64 = self._image_to_base64(img_path)
            print(f"🔍 Base64长度: {len(img_base64)}")
            content.append({
                "type": "image_url",
                "image_url": {"url": img_base64}
            })
            if isInTestMode:
                print(f"📸 已添加图片到请求: {os.path.basename(img_path)}")

        # 添加文件内容（提取的文本）
        for file_info in self.current_files:
            content.append({
                "type": "text",
                "text": f"【文件：{file_info['name']}】\n{file_info['content']}"
            })

        # 添加用户文本（放在最后）
        if user_text:
            content.append({"type": "text", "text": user_text})

        return content

    def _call_static(self, content, retries=3):
        """非流式调用Qwen VL API"""
        import time
        from openai import OpenAI
        # ✅ 调试：打印content结构和类型
        print(f"🔍 _call_stream 收到 content，类型: {type(content)}")
        if isinstance(content, list):
            print(f"🔍 content 长度: {len(content)}")
            for i, item in enumerate(content):
                if isinstance(item, dict):
                    if item.get('type') == 'image_url':
                        url_preview = str(item.get('image_url', {}).get('url', ''))[:100]
                        print(f"🔍 图片 {i}: {url_preview}...")
                    else:
                        print(f"🔍 文本 {i}: {str(item)[:100]}...")
        else:
            print(f"🔍 content 不是列表: {str(content)[:300]}")

        for attempt in range(retries):
            try:
                client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.api_url
                )

                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": content}
                ]

                params = {
                    "model": self.model,
                    "messages": messages,
                    "stream": False,
                    "temperature": self.temperature,
                    "max_tokens": 8192
                }

                if self.enable_thinking:
                    params["extra_body"] = {
                        "enable_thinking": True
                    }

                response = client.chat.completions.create(**params)
                reply = response.choices[0].message.content

                self.message_signal.emit("assistant", reply)
                self.raw_message.append({"role": "assistant", "content": reply})

                if hasattr(self.parent, 'save_current_session'):
                    self.parent.save_current_session()

                return

            except Exception as e:
                if attempt < retries - 1:
                    self.message_signal.emit("system", f"请求失败，正在重试（{attempt + 1}/{retries}）...\n错误：{str(e)}")
                    time.sleep(1)
                else:
                    self.message_signal.emit("system", f"错误：{str(e)}，已重试{retries}次")

    def _call_stream(self, content, retries=3):
        """流式调用Qwen VL API"""
        import time
        from openai import OpenAI

        for attempt in range(retries):
            try:
                client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.api_url
                )

                # 构造消息
                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": content}
                ]

                # 构建请求参数
                params = {
                    "model": self.model,
                    "messages": messages,
                    "stream": True,
                    "temperature": self.temperature,
                    "max_tokens": 8192
                }

                # 如果开启了思考模式，添加额外参数
                if self.enable_thinking:
                    params["extra_body"] = {
                        "enable_thinking": True
                    }

                stream = client.chat.completions.create(**params)

                # 添加占位
                placeholder_index = len(self.raw_message)
                self.raw_message.append({"role": "assistant", "content": ""})

                full_response = ""
                is_first_chunk = True

                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        chunk_content = chunk.choices[0].delta.content
                        full_response += chunk_content

                        if is_first_chunk:
                            self.message_signal.emit("assistant", full_response)
                            is_first_chunk = False
                        else:
                            self.update_last_assistant_message(full_response)

                        # 处理事件循环，保持UI响应
                        from PySide6.QtWidgets import QApplication
                        QApplication.processEvents()

                # 更新历史中的完整内容
                self.raw_message[placeholder_index]["content"] = full_response

                # 保存会话
                if hasattr(self.parent, 'save_current_session'):
                    self.parent.save_current_session()

                return  # 成功，退出重试循环

            except Exception as e:
                if attempt < retries - 1:
                    error_msg = f"流式请求失败，正在重试（{attempt + 1}/{retries}）...\n错误：{str(e)}"
                    self.message_signal.emit("system", error_msg)
                    time.sleep(1)  # 等待1秒
                else:
                    self.message_signal.emit("system", f"流式错误：{str(e)}，已重试{retries}次")

    def update_last_assistant_message(self, content):
        """更新最后一条助手消息（流式刷新）"""
        # 转义HTML特殊字符
        display_content = (content
                           .replace('&', '&amp;')
                           .replace('<', '&lt;')
                           .replace('>', '&gt;')
                           .replace('\n', '<br>'))

        from datetime import datetime
        import os

        prefix = os.getenv("MULTIMODAL_PREFIX", "🖼️图像助手：")
        font_family = os.getenv("MULTIMODAL_ASSISTANT_FONT", "")
        font_size = int(os.getenv("MULTIMODAL_ASSISTANT_SIZE", "16"))
        color = os.getenv("MULTIMODAL_ASSISTANT_COLOR", "#9b59b6")
        bg = os.getenv("MULTIMODAL_ASSISTANT_BG", "")

        message_html = f'''
        <div class="message assistant" style="font-family:{font_family}; font-size:{font_size}px; color:{color}; margin:10px 0; padding:10px; border-radius:8px; {f'background-color:{bg};' if bg else ''}">
            <div class="timestamp" style="font-size:12px; color:#999; margin-bottom:5px;">{datetime.now().strftime('%H:%M:%S')}</div>
            <div class="content">
                <b>{prefix}</b> {display_content}
            </div>
        </div>
        '''

        import json
        safe_html = json.dumps(message_html)

        js = f"""
        (function() {{
            var container = document.getElementById('chat-container');
            if (!container) return;
            if (container.lastChild) {{
                container.removeChild(container.lastChild);
            }}
            var div = document.createElement('div');
            div.innerHTML = {safe_html};
            container.appendChild(div.firstElementChild);
            container.scrollTop = container.scrollHeight;
        }})();
        """

        try:
            self.web_displayer.page().runJavaScript(js)
        except Exception as e:
            if isInTestMode:
                print(f"更新消息失败: {e}")

    def clear_chat(self):
        """清空当前会话"""
        self.raw_message = []
        self.current_images.clear()
        self.current_files.clear()
        self.current_full_response = ""
        self.clear_webview_signal.emit()

    def get_raw_message(self):
        """获取原始消息列表"""
        return self.raw_message

    def set_raw_message(self, messages):
        """设置原始消息列表"""
        self.raw_message = messages

    def create_context_menu(self, position, web_view):
        """创建右键菜单（下载图片、保存文档）"""
        hit_test = web_view.page().hitTestContent(position)
        image_url = hit_test.imageUrl().toString()

        if image_url and (image_url.startswith('file://') or image_url.startswith('http')):
            menu = QMenu()
            download_action = QAction("📥 保存图片", menu)
            download_action.triggered.connect(lambda: self._download_image(image_url))
            menu.exec_(web_view.mapToGlobal(position))

    def _download_image(self, url):
        """下载图片到本地"""
        file_path, _ = QFileDialog.getSaveFileName(
            self.parent, "保存图片", "", "图片 (*.png *.jpg *.jpeg);;所有文件 (*)"
        )
        if file_path:
            try:
                # 处理本地文件路径
                if url.startswith('file://'):
                    import shutil
                    src_path = url[7:]  # 去掉 file:// 前缀
                    shutil.copy2(src_path, file_path)
                else:
                    # HTTP下载
                    import urllib.request
                    urllib.request.urlretrieve(url, file_path)
                QMessageBox.information(self.parent, "下载成功", f"图片已保存到:\n{file_path}")
            except Exception as e:
                QMessageBox.warning(self.parent, "下载失败", f"保存图片失败：{str(e)}")