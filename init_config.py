# init_config.py
"""首次启动时自动生成 AI_config.env 配置文件"""

import os
import sys
import platform


isInTestMode = True


def get_platform_default_font_size():
    """根据操作系统返回合适的默认字体大小"""
    system = platform.system()
    if system == "Windows":
        return 13  # Windows 默认用 13 号
    elif system == "Darwin":  # macOS
        return 16  # macOS 用 16 号
    else:  # Linux 或其他
        return 14


def get_default_env_content():
    platform_default_size = get_platform_default_font_size()

    return f'''# ==================== API 配置 ====================
# 聊天模式 API
CHAT_MODEL=deepseek-v4-flash
CHAT_ASSISTANT_API_KEY=
CHAT_ASSISTANT_API_URL=https://api.deepseek.com

# 科研助手 API
RESEARCH_MODEL=deepseek-v4-pro
RESEARCH_ASSISTANT_API_KEY=
RESEARCH_ASSISTANT_API_URL=

# 代码助手 API
CODE_ASSISTANT_API_KEY=
CODE_ASSISTANT_API_URL=

# 多模态模型（图像助手）API
MULTIMODAL_API_KEY=
MULTIMODAL_API_URL=
MULTIMODAL_PROVIDER=qwen3-vl-plus

# 本地模式
LOCAL_API_URL=http://localhost:11434
LOCAL_MODEL=deepseek-r1:7b

# ==================== 界面文本配置 ====================
# 窗口标题
WINDOW_TITLE=雪雪的AI助手

# 输入框提示词
INPUT_PLACEHOLDER_CHAT=输入你想发送的消息～
INPUT_PLACEHOLDER_RESEARCH=把文件草稿给我，并准确描述你的要求。
INPUT_PLACEHOLDER_CODE=代码遇到了什么问题呢？
INPUT_PLACEHOLDER_MULTIMODAL=上传图片，告诉我你想怎么处理～

# 系统消息文本
SYSTEM_WELCOME_TITLE=🐱 欢迎使用雪雪AI助手！
SYSTEM_WELCOME_CONFIG_PATH=📝 首次运行已自动生成配置文件：
SYSTEM_WELCOME_FILL_KEY=🔑 请在系统设置菜单中填写你的 API Key
SYSTEM_WELCOME_NO_KEY=⚠️ 检测到 API Key 未配置
SYSTEM_WELCOME_EDIT_KEY=📝 在设置菜单中填写 CHAT_ASSISTANT_API_KEY
SYSTEM_WELCOME_GET_KEY=💡 访问 platform.deepseek.com 注册获取（新用户有免费额度）
SYSTEM_WELCOME_LOCAL_MODE=💡 可以先用【科研助理-本地模式】（需要安装 Ollama）
SYSTEM_CONFIG_UPDATED=✨ 配置已更新，新设置已生效。
SYSTEM_CONFIG_RELOAD=✨ 配置已更新，新设置已生效。

# ==================== 聊天模式 ====================
# 用户设置
USER_FONT_1=
USER_SIZE_1={platform_default_size}
USER_COLOR_1=#e56013
USER_BG_1=
USER_PREFIX_CHAT=用户：

# 助手设置
ASSISTANT_FONT_1=
ASSISTANT_SIZE_1={platform_default_size}
ASSISTANT_COLOR_1=#d663ff
ASSISTANT_BG_1=
ASSISTANT_PREFIX=聊天助手：
CHAT_ASSISTANT_PROMPT=你是AI助手，提供专业、友好的回答。请用简洁清晰的语言帮助用户。

# ==================== 科研助手 ====================
# 用户设置
RESEARCH_USER_FONT=
RESEARCH_USER_SIZE={platform_default_size}
RESEARCH_USER_COLOR=#d2d1d3
RESEARCH_USER_BG=
USER_PREFIX_RESEARCH=📊科研助手：

# 助手设置
RESEARCH_ASSISTANT_FONT=
RESEARCH_ASSISTANT_SIZE={platform_default_size}
RESEARCH_ASSISTANT_COLOR=#1e9be5
RESEARCH_ASSISTANT_BG=
RESEARCH_PREFIX_1=📊科研助理-在线模式：
RESEARCH_PREFIX_2=🔒科研助手（RAG）：
RESEARCH_PREFIX_3=💻科研助手（本地）：
RESEARCH_SYSTEM_PROMPT=科研助理模式

# ==================== 代码助手 ====================
# 用户设置
CODE_USER_FONT=
CODE_USER_SIZE={platform_default_size}
CODE_USER_COLOR=#28A745
CODE_USER_BG=
USER_PREFIX_CODE=👨‍💻用户：

# 助手设置
CODE_ASSISTANT_FONT=
CODE_ASSISTANT_SIZE={platform_default_size}
CODE_ASSISTANT_COLOR=#28A745
CODE_ASSISTANT_BG=
CODE_PREFIX=👨‍💻代码助手：
CODE_ASSISTANT_PROMPT=你是AI代码助手，帮助用户解决编程问题

# ==================== 多模态模型（图像助手）====================
# 用户设置
MULTIMODAL_USER_FONT=
MULTIMODAL_USER_SIZE={platform_default_size}
MULTIMODAL_USER_COLOR=#9b59b6
MULTIMODAL_USER_BG=
USER_PREFIX_MULTIMODAL=📸用户：

# 助手设置
MULTIMODAL_ASSISTANT_FONT=
MULTIMODAL_ASSISTANT_SIZE={platform_default_size}
MULTIMODAL_ASSISTANT_COLOR=#9b59b6
MULTIMODAL_ASSISTANT_BG=
MULTIMODAL_PREFIX=🖼️多模态和图像助手：
MULTIMODAL_SYSTEM_PROMPT=你是多模态和图像助手

# ==================== 系统消息样式 ====================
SYSTEM_FONT_1=
SYSTEM_SIZE_1={platform_default_size}
SYSTEM_COLOR_1=#999999
SYSTEM_PREFIX_1=系统
SYSTEM_STYLE_1=italic

# ==================== 输入框样式 ====================
INPUT_FONT_1=
INPUT_SIZE_1={platform_default_size}
INPUT_COLOR_1=#333333
INPUT_BG_1=#FFFFFF
INPUT_PLACEHOLDER_COLOR_1=#EAE6CA

# ==================== 功能开关 ====================
IS_STREAM_MODE=true

# ==================== 容器样式 ====================
CHAT_CONTAINER_BG=#1b1b1c
SIDEBAR_BG=#2d2d2d
INPUT_BG=#3c3c3c

# ==================== 消息背景 ====================
USER_MSG_BG=#2d2d2d
ASSISTANT_MSG_BG=#383838
SYSTEM_MSG_BG=#252525

# ==================== 边框 ====================
MESSAGE_BORDER_COLOR=#444
FOCUS_BORDER_COLOR=#9c27b0

# ==================== 时间戳 ====================
TIMESTAMP_COLOR=#888

# ==================== 代码块 ====================
CODE_BLOCK_BG=#0d0d0d
CODE_BLOCK_TEXT=#abb2bf
'''


def get_internal_dir():
    # 获取_internal文件夹的目录路径
    if getattr(sys, 'frozen', False):
        # 打包后的exec运行
        exec_dir = os.path.dirname(sys.executable)
        return os.path.join(exec_dir, '_internal')
    else:
        # 开发环境
        return os.path.abspath(".")


def get_env_path():
    # 获取配置文件路径
    internal_dir = get_internal_dir()
    return os.path.join(internal_dir, 'AI_config.env')


def ensure_config_exists():
    """确保配置文件存在，不存在则创建默认配置

        Returns:
            tuple: (env_path, is_first_run, has_api_keys)
                - env_path: 配置文件路径
                - is_first_run: 是否首次运行（刚创建了配置）
                - has_api_keys: 是否有有效的 API Key
    """
    internal_dir = get_internal_dir()
    env_path = get_env_path()

    # 确保_internal目录存在
    os.makedirs(internal_dir, exist_ok=True)

    is_first_run = False
    has_api_keys = False

    if not os.path.exists(env_path):
        if isInTestMode:
            print(f"📝 首次运行，正在创建配置文件: {env_path}")
        try:
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(get_default_env_content())
            if isInTestMode:
                print("✅ 配置文件创建成功！")
                print("   配置文件位置: " + env_path)
            is_first_run = True
        except Exception as e:
            if isInTestMode:
                print(f"❌ 配置文件创建失败: {e}")
            return None, False, False
    else:
        if isInTestMode:
            print(f"✅ 配置文件已存在: {env_path}")

    # 检查是否有 API_KEY（检查新的命名）
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            # 检查任意一个 Key 是否非空
            keys_to_check = [
                r'CHAT_ASSISTANT_API_KEY=(.+)',
                r'RESEARCH_ASSISTANT_API_KEY=(.+)',
                r'CODE_ASSISTANT_API_KEY=(.+)',
                r'DOCUMENT_ASSISTANT_API_KEY=(.+)',
            ]
            for pattern in keys_to_check:
                match = re.search(pattern, content)
                if match:
                    key_val = match.group(1).strip()
                    if key_val and not key_val.startswith('#') and key_val != '':
                        has_api_keys = True
                        break
    except Exception:
        pass

    return env_path, is_first_run, has_api_keys


def get_config_message(is_first_run, has_api_keys):
    """获取配置相关的系统提示消息

        Returns:
            str: 要显示的系统消息
    """
    if is_first_run:
        msg = "🐱 欢迎使用雪雪AI助手！\n\n"
        msg += "📝 首次运行已自动生成配置文件：\n"
        msg += f"   {get_env_path()}\n\n"
        msg += "🔑 需要在系统设置菜单中填写你的API_KEY和API_URL，默认会使用Deepseek的URL\n"
        msg += "💡 如果暂时没有 API Key，可以：\n"
        msg += "   - 访问 platform.deepseek.com 注册获取（新用户有免费额度）\n"
        msg += "   - 或者使用本地模式（需要安装 Ollama）\n\n"
        msg += "✨ 填写完成后，重启程序即可使用全部功能～"
        return msg
    elif not has_api_keys:
        msg = "⚠️ 检测到 API Key 未配置\n\n"
        msg += "🔑 请编辑配置文件填写你的 DeepSeek API Key：\n"
        msg += f"   {get_env_path()}\n\n"
        msg += "🔑 需要在系统设置菜单中填写你的API_KEY和API_URL，默认会使用Deepseek的URL\n"
        msg += "💡 如果暂时没有 API Key，可以：\n"
        msg += "   - 访问 platform.deepseek.com 注册获取（新用户有免费额度）\n"
        msg += "   - 或者使用本地模式（需要安装 Ollama）\n\n"
        msg += "✨ 填写完成后重启程序即可～"
        return msg
    else:
        return None


def get_doc_assistant_env_path():
    """获取文档助手配置文件路径"""
    internal_dir = get_internal_dir()
    return os.path.join(internal_dir, 'AI_doc_assistant.env')


def get_default_doc_assistant_env_content():
    """获取文档助手默认配置内容"""
    return '''# ==================== 文档助手配置 ====================
# 服务商选择：qwen / doubao / deepseek
DOC_ASSISTANT_PROVIDER=qwen

# API Key（根据选择的服务商填写）
DOC_ASSISTANT_API_KEY=

# 模型名称
DOC_ASSISTANT_MODEL=qwen-max

# 温度参数（0-1，越高越随机）
DOC_ASSISTANT_TEMPERATURE=0.7

# 输出目录
DOC_ASSISTANT_OUTPUT_DIR=./outputs

# 模板目录
DOC_ASSISTANT_TEMPLATE_DIR=./docs_template
'''


def ensure_doc_assistant_config_exists():
    """确保文档助手配置文件存在，不存在则创建"""
    env_path = get_doc_assistant_env_path()
    internal_dir = get_internal_dir()
    os.makedirs(internal_dir, exist_ok=True)

    is_first_run = False

    if not os.path.exists(env_path):
        try:
            with open(env_path, 'w', encoding='utf-8') as f:
                f.write(get_default_doc_assistant_env_content())
            is_first_run = True
            if isInTestMode:
                print(f"📝 首次运行，正在创建文档助手配置文件: {env_path}")
        except Exception as e:
            if isInTestMode:
                print(f"❌ 文档助手配置文件创建失败: {e}")
            return None, False

    return env_path, is_first_run


def load_doc_assistant_config():
    """加载文档助手配置，返回字典"""
    import re
    env_path = get_doc_assistant_env_path()

    # 确保文件存在
    ensure_doc_assistant_config_exists()

    config = {
        "provider": "qwen",
        "api_key": "",
        "model": "qwen-max",
        "temperature": 0.7,
        "output_dir": "./outputs",
        "template_dir": "./docs_template"
    }

    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()

        patterns = {
            "provider": r'DOC_ASSISTANT_PROVIDER=(.+)',
            "api_key": r'DOC_ASSISTANT_API_KEY=(.+)',
            "model": r'DOC_ASSISTANT_MODEL=(.+)',
            "temperature": r'DOC_ASSISTANT_TEMPERATURE=(.+)',
            "output_dir": r'DOC_ASSISTANT_OUTPUT_DIR=(.+)',
            "template_dir": r'DOC_ASSISTANT_TEMPLATE_DIR=(.+)',
        }

        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                value = match.group(1).strip()
                if value and not value.startswith('#'):
                    if key == "temperature":
                        try:
                            config[key] = float(value)
                        except:
                            pass
                    else:
                        config[key] = value
    except Exception as e:
        if isInTestMode:
            print(f"⚠️ 加载文档助手配置失败: {e}")

    return config


def save_doc_assistant_config(config):
    """保存文档助手配置到 .env 文件"""
    env_path = get_doc_assistant_env_path()

    content = f'''# ==================== 文档助手配置 ====================
# 服务商选择：qwen / doubao / deepseek
DOC_ASSISTANT_PROVIDER={config.get("provider", "qwen")}

# API Key（根据选择的服务商填写）
DOC_ASSISTANT_API_KEY={config.get("api_key", "")}

# 模型名称
DOC_ASSISTANT_MODEL={config.get("model", "qwen-max")}

# 温度参数（0-1，越高越随机）
DOC_ASSISTANT_TEMPERATURE={config.get("temperature", 0.7)}

# 输出目录
DOC_ASSISTANT_OUTPUT_DIR={config.get("output_dir", "./outputs")}

# 模板目录
DOC_ASSISTANT_TEMPLATE_DIR={config.get("template_dir", "./docs_template")}
'''

    try:
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(content)
        if isInTestMode:
            print(f"✅ 文档助手配置已保存: {env_path}")
        return True
    except Exception as e:
        if isInTestMode:
            print(f"❌ 保存文档助手配置失败: {e}")
        return False