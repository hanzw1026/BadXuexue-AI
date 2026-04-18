# knowledge_base_dialog.py
"""本地知识库管理对话框 - 混合模式（按需安装依赖）"""

import os
import stat
import sys
import platform
import shutil
import subprocess
from datetime import datetime
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QFileDialog, QListWidgetItem, QApplication,
    QVBoxLayout, QProgressBar, QLabel, QTextEdit, QPushButton
)
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QDragEnterEvent, QDropEvent

from knowledge_dialog_ui import Ui_Dialog
import init_config


class UIUpdateThread(QThread):
    """独立 UI 更新线程"""
    update_signal = Signal(int, bool)  # 秒数, 闪烁状态

    def __init__(self):
        super().__init__()
        self.running = True
        self.elapsed_seconds = 0
        self.blink_state = False

    def run(self):
        import time
        while self.running:
            time.sleep(1)
            self.elapsed_seconds += 1
            self.blink_state = not self.blink_state
            self.update_signal.emit(self.elapsed_seconds, self.blink_state)

    def stop(self):
        self.running = False


class IndexProgressDialog(QDialog):
    """索引进度对话框"""

    def __init__(self, total_files, parent=None):
        super().__init__(parent)
        self.setWindowTitle("正在建立索引")
        self.setModal(True)
        self.setMinimumWidth(500)

        layout = QVBoxLayout(self)

        # 状态文字（会闪烁）
        self.label_status = QLabel("📚 正在处理文档，请稍候...")
        self.label_status.setWordWrap(True)
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_status)

        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, total_files)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # 当前文件
        self.label_current = QLabel("当前文件: --")
        self.label_current.setWordWrap(True)
        layout.addWidget(self.label_current)

        # 计时器显示
        self.label_timer = QLabel("已用时: 0 秒")
        self.label_timer.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.label_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_timer)

        # 取消按钮
        self.btn_cancel = QPushButton("取消")
        self.btn_cancel.clicked.connect(self.cancel)
        layout.addWidget(self.btn_cancel)

        # 创建并启动独立 UI 更新线程
        self.update_thread = UIUpdateThread()
        self.update_thread.update_signal.connect(self._on_update_ui)
        self.update_thread.start()

        self.is_cancelled = False

    def _on_update_ui(self, seconds, blink):
        """更新 UI（由独立线程触发）"""
        self.label_timer.setText(f"已用时: {seconds} 秒")

        if blink:
            self.label_status.setText("⏳ 正在处理文档，程序中...")
            self.label_status.setStyleSheet("color: #27ae60;")
        else:
            self.label_status.setText("📚 正在处理文档，请稍候...")
            self.label_status.setStyleSheet("color: #2c3e50;")

    def update_progress(self, current, total, filename):
        """更新进度（由 _add_files 调用）"""
        self.progress_bar.setValue(current)
        self.label_current.setText(f"当前文件: {filename}")
        QApplication.processEvents()

    def cancel(self):
        reply = QMessageBox.question(
            self, "确认取消",
            "确定要取消索引吗？\n\n已处理的文件将保留，未处理的文件需要重新添加。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.is_cancelled = True
            self.cleanup_thread()
            self.close()

    def cleanup_thread(self):
        """清理线程资源"""
        if self.update_thread and self.update_thread.isRunning():
            self.update_thread.stop()
            self.update_thread.wait(3000)
            if self.update_thread.isRunning():
                self.update_thread.terminate()
                self.update_thread.wait()

    def closeEvent(self, event):
        self.cleanup_thread()
        event.accept()


class InstallThread(QThread):
    """后台安装线程 - 全部下载到本地"""
    message = Signal(str)
    finished_signal = Signal(bool)

    def __init__(self):
        super().__init__()

    def run(self):
        try:
            pip_index = "https://pypi.tuna.tsinghua.edu.cn/simple"
            hf_endpoint = "https://hf-mirror.com"

            # 获取程序内部目录
            internal_dir = init_config.get_internal_dir()
            models_dir = os.path.join(internal_dir, "models")
            os.makedirs(models_dir, exist_ok=True)

            # 设置镜像
            os.environ["HF_ENDPOINT"] = hf_endpoint

            self.message.emit("📦 正在安装 ChromaDB...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "chromadb",
                "-i", pip_index
            ])

            self.message.emit("📦 正在安装 Sentence-Transformers...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "sentence-transformers",
                "-i", pip_index
            ])

            self.message.emit("📦 正在安装文档解析库...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "pypdf2", "python-docx",
                "-i", pip_index
            ])

            self.message.emit("📦 正在安装 OCR 支持库...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "pdf2image", "pytesseract",
                "-i", pip_index
            ])

            self.message.emit("🤖 正在下载 AI 模型（约 33 MB）...")

            # 下载模型到本地目录
            from sentence_transformers import SentenceTransformer
            model_save_path = os.path.join(models_dir, "bge-small-zh")

            # 下载并保存到指定目录
            model = SentenceTransformer('BAAI/bge-small-zh')
            model.save(model_save_path)

            # 验证模型可用
            test_vec = model.encode("测试模型是否正常")
            if len(test_vec) > 0:
                self.message.emit(f"✅ 模型下载完成，向量维度: {len(test_vec)}")
                self.message.emit(f"📁 模型已保存至: {model_save_path}")

            # ✅ 创建完整性检查文件
            self._create_install_marker(internal_dir, model_save_path)

            self.message.emit("✅ 所有组件安装完成！")
            self.finished_signal.emit(True)

        except Exception as e:
            self.message.emit(f"❌ 安装失败：{str(e)}")
            self.finished_signal.emit(False)

    def _create_install_marker(self, internal_dir, model_path):
        """创建安装标志文件，记录安装信息"""
        marker_file = os.path.join(internal_dir, ".kb_installed")

        install_info = {
            "version": "1.0",
            "install_time": datetime.now().isoformat(),
            "model_path": model_path,
            "model_name": "BAAI/bge-small-zh",
            "components": ["chromadb", "sentence-transformers", "pypdf2", "python-docx"]
        }

        import json
        with open(marker_file, 'w') as f:
            json.dump(install_info, f, indent=2)

        # 同时创建一个简单的标志文件（快速检查用）
        quick_flag = os.path.join(internal_dir, ".kb_ready")
        with open(quick_flag, 'w') as f:
            f.write("ready")

        if init_config.isInTestMode:
            print(f"✅ 已创建安装标志: {marker_file}")


class KnowledgeBaseDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        # 高DPI适配：让Qt自己控制
        if hasattr(Qt, 'AA_EnableHighDpiScaling'):
            QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, False)
            QApplication.setAttribute(Qt.AA_DisableHighDpiScaling, True)
        super().__init__(parent)
        self.setupUi(self)
        self.model = None

        # 启用拖拽
        self.setAcceptDrops(True)

        # 知识库目录
        self.kb_dir = self._get_kb_dir()
        self.documents_dir = os.path.join(self.kb_dir, "documents")
        self.chroma_dir = os.path.join(self.kb_dir, "chroma")

        # 确保 documents 目录存在
        os.makedirs(self.documents_dir, exist_ok=True)

        # 连接信号（注意 UI 中的按钮名称）
        self.btn_delete_slected_file.clicked.connect(self.delete_selected)
        self.btn_delete_all_file.clicked.connect(self.delete_all)  # 清空知识库
        self.btn_rebuild_base_index.clicked.connect(self.rebuild_index)  # 重建索引
        self.btn_import_file.clicked.connect(self.upload_files)  # 上传文件
        self.btn_close_window.clicked.connect(self.close)

        # 修复知识库权限（防止写保护）
        self.fix_knowledge_base_permissions()

        # 检查依赖是否已安装（包括模型）
        self.deps_installed = self._check_deps()

        if not self.deps_installed:
            self._ask_install_deps()
        else:
            self._init_chroma()
            self.refresh_file_list()

    def _check_deps(self):
        """快速检查依赖 - 只检查文件存在性，不加载任何模块"""

        # 1. 先检查快速标志文件
        internal_dir = init_config.get_internal_dir()
        quick_flag = os.path.join(internal_dir, ".kb_ready")

        if os.path.exists(quick_flag):
            if init_config.isInTestMode:
                print("✅ 知识库标志文件存在")
            return True

        # 2. 检查模型文件是否真的存在
        models_dir = os.path.join(internal_dir, "models")
        model_path = os.path.join(models_dir, "bge-small-zh")

        # 检查模型目录和关键文件
        if not os.path.exists(model_path):
            if init_config.isInTestMode:
                print(f"❌ 模型目录不存在: {model_path}")
            return False

        # 检查是否有模型权重文件
        model_files = ['pytorch_model.bin', 'model.safetensors', 'pytorch_model.bin.index.json']
        has_model_file = False
        for root, dirs, files in os.walk(model_path):
            for f in files:
                if any(f.endswith(ext) for ext in model_files):
                    has_model_file = True
                    break
            if has_model_file:
                break

        if not has_model_file:
            if init_config.isInTestMode:
                print(f"❌ 模型目录中没有找到权重文件: {model_path}")
            return False

        # 3. 检查 Python 包是否安装（快速导入测试）
        try:
            import chromadb
            import sentence_transformers
            if init_config.isInTestMode:
                print("✅ Python 包已安装")
        except ImportError as e:
            if init_config.isInTestMode:
                print(f"❌ Python 包缺失: {e}")
            return False

        # 所有检查通过，创建标志文件避免下次重复检查
        with open(quick_flag, 'w') as f:
            f.write("ready")

        if init_config.isInTestMode:
            print("✅ 知识库完整性检查通过，已创建标志文件")

        return True

    def _check_packages(self):
        """检查 Python 包是否安装"""
        try:
            import chromadb
            import sentence_transformers
            return True
        except ImportError:
            return False

    def _check_model_exists(self):
        """检查本地模型是否存在"""
        try:
            from sentence_transformers import SentenceTransformer

            # 尝试加载模型（会从缓存加载，不会重复下载）
            model = SentenceTransformer('BAAI/bge-small-zh',  local_files_only=True)

            # 验证模型真的可用
            test_vec = model.encode("测试")
            if test_vec is not None and len(test_vec) > 0:
                if init_config.isInTestMode:
                    print("✅ 本地模型存在且可用")
                return True
            return False

        except Exception as e:
            if init_config.isInTestMode:
                print(f"⚠️ 模型检查失败: {e}")
            return False

    def _check_deps(self):
        """检查依赖包 + 本地模型是否存在"""
        packages_ok = self._check_packages()
        model_ok = self._check_model_exists()

        if init_config.isInTestMode:
            print(f"📦 包状态: {'✅' if packages_ok else '❌'}")
            print(f"🤖 模型状态: {'✅' if model_ok else '❌'}")

        return packages_ok and model_ok

    def _get_app_dir(self):
        """获取应用程序所在目录"""
        import sys
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(os.path.abspath(__file__))

    def _cleanup_model_cache(self):
        """清理 HuggingFace 缓存中的旧模型（可选）"""
        cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
        model_cache = os.path.join(cache_dir, "models--BAAI--bge-small-zh")

        if os.path.exists(model_cache):
            import shutil
            if init_config.isInTestMode:
                print(f"🗑️ 清理旧缓存: {model_cache}")
            shutil.rmtree(model_cache)

    def _get_model_dir(self):
        """获取模型目录（统一管理）"""
        app_dir = self._get_app_dir()
        local_model_path = os.path.join(app_dir, "_model", "bge-small-zh")

        if os.path.exists(local_model_path):
            if init_config.isInTestMode:
                print(f"✅ 使用本地模型: {local_model_path}")
            return local_model_path

        # 降级：检查 HuggingFace 缓存
        cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
        model_cache = os.path.join(cache_dir, "models--BAAI--bge-small-zh")

        if os.path.exists(model_cache):
            snapshots_dir = os.path.join(model_cache, "snapshots")
            if os.path.exists(snapshots_dir):
                snapshots = [d for d in os.listdir(snapshots_dir)
                             if os.path.isdir(os.path.join(snapshots_dir, d))]
                if snapshots:
                    latest = max(snapshots, key=lambda x: os.path.getmtime(
                        os.path.join(snapshots_dir, x)))
                    return os.path.join(snapshots_dir, latest)

        return None  # 需要下载

    def _get_model(self):
        """获取模型（统一使用程序目录下的模型）"""
        self.fix_knowledge_base_permissions()
        if self.model is None:
            from sentence_transformers import SentenceTransformer

            # 获取程序目录
            app_dir = self._get_app_dir()
            model_path = os.path.join(app_dir, "_model", "bge-small-zh")

            # 检查本地模型是否存在且是 sentence-transformers 格式
            config_file = os.path.join(model_path, "sentence_bert_config.json")

            if os.path.exists(model_path) and os.path.exists(config_file):
                # 本地有完整模型，直接加载
                if init_config.isInTestMode:
                    print(f"📦 加载本地模型: {model_path}")
                os.environ["HF_HUB_OFFLINE"] = "1"
                os.environ["TRANSFORMERS_OFFLINE"] = "1"
                self.model = SentenceTransformer(model_path, device='cpu',  local_files_only=True)
            else:
                # 本地没有或格式不对，重新下载
                if init_config.isInTestMode:
                    print("📦 下载模型到本地...")

                os.environ["HF_HUB_OFFLINE"] = "0"
                os.environ["TRANSFORMERS_OFFLINE"] = "0"

                # 下载并保存为 sentence-transformers 格式
                model = SentenceTransformer('BAAI/bge-small-zh',
                                            device='cpu',
                                            local_files_only=True)

                # 保存到程序目录
                os.makedirs(model_path, exist_ok=True)
                model.save(model_path)  # 这会保存完整的配置

                # 验证保存成功
                if os.path.exists(os.path.join(model_path, "sentence_bert_config.json")):
                    if init_config.isInTestMode:
                        print(f"✅ 模型已保存: {model_path}")

                os.environ["HF_HUB_OFFLINE"] = "1"
                os.environ["TRANSFORMERS_OFFLINE"] = "1"

                self.model = model

        return self.model

    def _get_kb_dir(self):
        """获取知识库目录"""
        internal_dir = init_config.get_internal_dir()
        return os.path.join(internal_dir, "knowledge_base")

    def _ask_install_deps(self):
        """询问用户是否安装依赖"""
        # 判断缺少什么
        missing_packages = not self._check_packages()
        missing_model = not self._check_model_exists()

        missing_list = []
        if missing_packages:
            missing_list.append("• Python 依赖包（ChromaDB、Sentence-Transformers等，约150 MB）")
        if missing_model:
            missing_list.append("• BAAI/bge-small-zh 中文AI模型（约33 MB）")

        missing_text = "\n".join(missing_list)

        reply = QMessageBox.question(
            self, "安装知识库组件",
            f"📚 本地知识库需要安装以下组件：\n\n{missing_text}\n\n"
            f"首次安装需要下载，耗时约 5-10 分钟。\n"
            f"是否继续？\n\n"
            f"（安装后即可使用，之后无需再次安装）",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self._install_deps()
        else:
            self.list_local_file.addItem("⚠️ 知识库未初始化，请重启窗口后选择“是”安装依赖")
            self.btn_import_file.setEnabled(False)
            self.btn_delete_slected_file.setEnabled(False)
            self.btn_delete_all_file.setEnabled(False)
            self.btn_rebuild_base_index.setEnabled(False)

    def _install_deps(self):
        """安装依赖"""
        self.install_thread = InstallThread()
        self.install_thread.message.connect(self._on_install_message)
        self.install_thread.finished_signal.connect(self._on_install_finished)

        self.list_local_file.clear()
        self.list_local_file.addItem("📦 正在安装知识库组件...")
        self.list_local_file.addItem("⏳ 请稍候，约 5-10 分钟")
        self.btn_import_file.setEnabled(False)
        self.btn_delete_slected_file.setEnabled(False)
        self.btn_delete_all_file.setEnabled(False)
        self.btn_rebuild_base_index.setEnabled(False)

        self.install_thread.start()

    def _on_install_message(self, msg):
        """安装进度消息"""
        self.list_local_file.insertItem(0, msg)
        if init_config.isInTestMode:
            print(f"📦 {msg}")

    def _on_install_finished(self, success):
        """安装完成回调"""
        if success:
            self.deps_installed = True
            self._init_chroma()
            self.refresh_file_list()
            self.btn_import_file.setEnabled(True)
            self.btn_delete_slected_file.setEnabled(True)
            self.btn_delete_all_file.setEnabled(True)
            self.btn_rebuild_base_index.setEnabled(True)

            if self.parent():
                self.parent().DisplayMessage("system", "📚 知识库已就绪！可以上传文档了")

            # ✅ 显示安装完成信息
            QMessageBox.information(
                self, "安装完成",
                "✅ 知识库组件已全部安装完成！\n\n"
                "📁 模型已保存到本地目录\n"
                "💡 现在可以完全离线使用\n"
                "📄 支持上传 txt、pdf、docx、md 等格式\n\n"
                "⚠️ 注意：扫描版 PDF 需要额外安装 poppler 和 tesseract\n"
                "   运行：brew install poppler tesseract tesseract-lang"
            )
        else:
            self.list_local_file.clear()
            self.list_local_file.addItem("❌ 安装失败，请检查网络后重试")
            self.list_local_file.addItem("💡 或手动运行：pip install chromadb sentence-transformers")

    def _init_chroma(self):
        """初始化 Chroma 向量数据库"""
        try:
            import chromadb

            # 先修复权限
            self.fix_knowledge_base_permissions()

            os.makedirs(self.chroma_dir, exist_ok=True)

            # 尝试连接，如果失败则删除并重建
            try:
                self.chroma_client = chromadb.PersistentClient(path=self.chroma_dir)
                self.chroma_collection = self.chroma_client.get_or_create_collection(
                    name="knowledge_base",
                    metadata={"hnsw:space": "cosine"}
                )
                if init_config.isInTestMode:
                    print("✅ Chroma 已初始化")
            except Exception as e:
                if "no such table" in str(e):
                    if init_config.isInTestMode:
                        print(f"⚠️ Chroma 数据库损坏，正在重建...")
                    # 删除损坏的数据库
                    import shutil
                    shutil.rmtree(self.chroma_dir)
                    os.makedirs(self.chroma_dir, exist_ok=True)

                    # 重新创建
                    self.chroma_client = chromadb.PersistentClient(path=self.chroma_dir)
                    self.chroma_collection = self.chroma_client.get_or_create_collection(
                        name="knowledge_base",
                        metadata={"hnsw:space": "cosine"}
                    )
                    if init_config.isInTestMode:
                        print("✅ Chroma 已重建")
                else:
                    raise e

        except Exception as e:
            if init_config.isInTestMode:
                print(f"❌ Chroma 初始化失败: {e}")

    def dragEnterEvent(self, event: QDragEnterEvent):
        """拖拽进入事件"""
        if not self.deps_installed:
            event.ignore()
            return
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet("QDialog { background-color: #2a2a2a; }")

    def dragLeaveEvent(self, event):
        self.fix_knowledge_base_permissions()
        self.setStyleSheet("")

    def dropEvent(self, event: QDropEvent):
        """拖拽放下事件"""
        if not self.deps_installed:
            return

        self.setStyleSheet("")
        files = []
        folders = []

        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isfile(path):
                files.append(path)
            elif os.path.isdir(path):
                folders.append(path)

        if files:
            self._add_files(files)

        for folder in folders:
            self._add_folder(folder)

    def upload_files(self):
        """通过文件对话框上传文件"""
        if not self.deps_installed:
            QMessageBox.information(self, "提示", "知识库尚未初始化，请稍后再试")
            return

        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "选择文件", "",
            "文档 (*.txt *.docx *.pdf *.xlsx *.xls *.md);;所有文件 (*)"
        )
        if file_paths:
            self._add_files(file_paths)

    def _add_files(self, file_paths):
        """批量添加文件到知识库（带进度对话框）"""
        total = len(file_paths)
        success_count = 0

        # 创建进度对话框
        progress_dialog = IndexProgressDialog(total, self)
        progress_dialog.show()

        for i, file_path in enumerate(file_paths):
            # 检查是否取消
            if progress_dialog.is_cancelled:
                if init_config.isInTestMode:
                    print("⚠️ 用户取消了索引操作")
                break

            filename = os.path.basename(file_path)

            # 更新进度
            progress_dialog.update_progress(i + 1, total, filename)

            if self.parent():
                self.parent().DisplayMessage(
                    "system",
                    f"📚 正在添加 ({i + 1}/{total}): {filename}"
                )

            # 添加文件（内部会处理索引）
            if self._add_single_file(file_path):
                success_count += 1

            # 强制处理事件，让 UI 有机会刷新
            QApplication.processEvents()

        # 关闭进度对话框
        progress_dialog.cleanup_thread()
        progress_dialog.close()

        if self.parent():
            self.parent().DisplayMessage(
                "system",
                f"✅ 已添加 {success_count}/{total} 个文件到知识库"
            )

        self.refresh_file_list()

        QMessageBox.information(
            self, "添加完成",
            f"成功添加 {success_count} 个文件\n失败 {total - success_count} 个"
        )

    def _add_single_file(self, file_path):
        """添加单个文件到知识库"""
        try:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(self.documents_dir, file_name)

            if os.path.exists(dest_path):
                name, ext = os.path.splitext(file_name)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                dest_path = os.path.join(self.documents_dir, f"{name}_{timestamp}{ext}")

            shutil.copy2(file_path, dest_path)

            if self.deps_installed:
                self._index_document(dest_path)

            if init_config.isInTestMode:
                print(f"✅ 已添加: {file_name}")

            return True

        except Exception as e:
            if init_config.isInTestMode:
                print(f"❌ 添加失败 {file_path}: {e}")
            return False

    def _index_document(self, file_path, retry=True):
        """将文档索引到 Chroma 向量数据库（简化版）"""
        self.fix_knowledge_base_permissions()
        try:
            model = self._get_model()
            content = self._parse_document(file_path)
            if not content:
                return

            chunks = self._chunk_text(content)

            for i, chunk in enumerate(chunks):
                embedding = model.encode(chunk).tolist()
                self.chroma_collection.add(
                    ids=[f"{os.path.basename(file_path)}_{i}"],
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{"source": file_path, "chunk": i}]
                )

            if init_config.isInTestMode:
                print(f"✅ 已索引: {os.path.basename(file_path)} ({len(chunks)} 块)")

        except Exception as e:
            error_msg = str(e)
            if "readonly" in error_msg or "no such table" in error_msg:
                if retry:
                    if init_config.isInTestMode:
                        print(f"⚠️ 数据库写保护，正在重建...")
                    shutil.rmtree(self.chroma_dir)
                    self._init_chroma()
                    self._index_document(file_path, retry=False)
            else:
                if init_config.isInTestMode:
                    print(f"⚠️ 索引失败 {file_path}: {e}")

        except Exception as e:
            error_msg = str(e)
            if "readonly" in error_msg or "no such table" in error_msg:
                if retry:
                    if init_config.isInTestMode:
                        print(f"⚠️ 数据库写保护，正在重建...")
                    shutil.rmtree(self.chroma_dir)
                    self._init_chroma()
                    self._index_document(file_path, retry=False, progress_callback=progress_callback)
                else:
                    if init_config.isInTestMode:
                        print(f"❌ 索引失败（重建后仍失败）: {file_path}")
            else:
                if init_config.isInTestMode:
                    print(f"⚠️ 索引失败 {file_path}: {e}")

    def _parse_document(self, file_path):
        """解析文档内容"""
        ext = os.path.splitext(file_path)[1].lower()

        try:
            if ext == '.pdf':
                import PyPDF2
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)

                    # 1. 检测是否加密
                    if reader.is_encrypted:
                        # 2. 先尝试用空密码解密（很多“限制复制”的PDF用这个就能解开）
                        try:
                            reader.decrypt('')
                            if init_config.isInTestMode:
                                print(f"🔓 空密码解密成功: {os.path.basename(file_path)}")
                        except Exception as e:
                            # 3. 空密码失败，提示用户需要密码
                            error_msg = f"[加密PDF需要密码: {os.path.basename(file_path)}]"
                            if init_config.isInTestMode:
                                print(f"⚠️ {error_msg}")
                            return error_msg

                    # 提取文字
                    text = '\n'.join([page.extract_text() or '' for page in reader.pages])

                    # 5. 如果提取到的文字太少，可能是扫描版
                    if len(text.strip()) < 100:
                        if init_config.isInTestMode:
                            print(f"⚠️ PDF文字提取较少，可能是扫描版: {os.path.basename(file_path)}")

                        reply = QMessageBox.question(
                            self, "检测到扫描版PDF",
                            f"文件 {os.path.basename(file_path)} 可能是扫描版，\n"
                            "文字提取失败。是否使用OCR识别？\n\n"
                            f"📄 页数：{len(reader.pages)} 页\n"
                            "⏱️ 预计耗时：10-20分钟\n\n"
                            "⚠️ 请耐心等待，不要关闭程序。",
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                        )
                        if reply == QMessageBox.StandardButton.Yes:
                            return self._parse_pdf_with_ocr(file_path)

                    return text

            elif ext == '.docx':
                from docx import Document
                doc = Document(file_path)
                text = '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
                return text

            elif ext == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    return f.read()

            else:
                return ""

        except Exception as e:
            if init_config.isInTestMode:
                print(f"⚠️ 解析失败 {file_path}: {e}")
            return f"[解析失败: {os.path.basename(file_path)} - {str(e)[:50]}]"

    def _parse_pdf_with_ocr(self, file_path):
        """使用OCR解析扫描版PDF"""
        try:
            from pdf2image import convert_from_path
            import pytesseract
            import shutil

            extra_kwargs = {}
            missing_tools = []

            # ✅ macOS 路径
            if platform.system() == 'Darwin':
                tesseract_path = "/opt/homebrew/bin/tesseract"
                if os.path.exists(tesseract_path):
                    pytesseract.pytesseract.tesseract_cmd = tesseract_path
                else:
                    missing_tools.append("Tesseract (brew install tesseract tesseract-lang)")

                poppler_path = "/opt/homebrew/bin"
                if os.path.exists(poppler_path):
                    os.environ["PATH"] = poppler_path + ":" + os.environ.get("PATH", "")
                    extra_kwargs = {'poppler_path': poppler_path}
                else:
                    missing_tools.append("Poppler (brew install poppler)")

            # ✅ Windows 路径
            elif platform.system() == 'Windows':
                tesseract_paths = [
                    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
                ]
                tesseract_found = False
                for path in tesseract_paths:
                    if os.path.exists(path):
                        pytesseract.pytesseract.tesseract_cmd = path
                        tesseract_found = True
                        break
                if not tesseract_found:
                    missing_tools.append("Tesseract (下载: https://github.com/UB-Mannheim/tesseract/releases)")

                poppler_paths = [
                    r"C:\poppler\Library\bin",
                    r"C:\poppler\bin",
                ]
                poppler_found = False
                for path in poppler_paths:
                    if os.path.exists(path):
                        extra_kwargs = {'poppler_path': path}
                        poppler_found = True
                        break
                if not poppler_found:
                    missing_tools.append("Poppler (下载: https://github.com/oschwartz10612/poppler-windows/releases)")

            # ✅ Linux 路径
            elif platform.system() == 'Linux':
                tesseract_path = shutil.which("tesseract")
                if tesseract_path:
                    pytesseract.pytesseract.tesseract_cmd = tesseract_path
                else:
                    missing_tools.append("Tesseract (sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim)")

                poppler_path = shutil.which("pdfinfo")
                if poppler_path:
                    extra_kwargs = {'poppler_path': os.path.dirname(poppler_path)}
                else:
                    missing_tools.append("Poppler (sudo apt-get install poppler-utils)")

            # ✅ 如果有缺失工具，输出提示
            if missing_tools:
                print("\n" + "=" * 50)
                print("⚠️ OCR 工具缺失，扫描版 PDF 将无法识别")
                print("=" * 50)
                for tool in missing_tools:
                    print(f"  ❌ {tool}")
                print("=" * 50)
                print("💡 安装后重新运行即可启用 OCR 功能\n")
                return ""

            # 转换PDF为图片
            print(f"🔧 开始 OCR 转换: {os.path.basename(file_path)}")

            images = convert_from_path(file_path, dpi=150, **extra_kwargs)

            full_text = []
            total = len(images)
            print(f"📄 共 {total} 页，开始识别...")

            for i, image in enumerate(images):
                if self.parent():
                    self.parent().DisplayMessage(
                        "system",
                        f"📚 OCR识别中：第 {i + 1}/{total} 页"
                    )

                # ✅ 命令行实时进度输出
                print(f"   📖 正在识别第 {i + 1}/{total} 页...", end=' ')

                text = pytesseract.image_to_string(image, lang='chi_sim+eng')
                full_text.append(text)

                # 显示这一页识别到的文字数量
                text_len = len(text.strip())
                print(f"✅ 识别到 {text_len} 字符")

                QApplication.processEvents()

            print(f"\n✅ OCR 完成！共 {total} 页，总字符数: {sum(len(t) for t in full_text)}")

            return '\n'.join(full_text)

        except Exception as e:
            print(f"❌ OCR解析失败: {e}")
            if "poppler" in str(e).lower():
                print("💡 请确保 poppler 已正确安装并添加到 PATH")
            if "tesseract" in str(e).lower():
                print("💡 请确保 tesseract 已正确安装并添加到 PATH")
            return ""

    def _chunk_text(self, text, chunk_size=500, overlap=50):
        """文本切块"""
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap
        return chunks

    def _add_folder(self, folder_path):
        """添加文件夹中的所有文件"""
        supported_ext = {'.txt', '.docx', '.pdf', '.xlsx', '.xls', '.md'}
        files = []

        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in supported_ext:
                    files.append(os.path.join(root, filename))

        if files:
            self._add_files(files)
            if self.parent():
                self.parent().DisplayMessage(
                    "system",
                    f"📁 从文件夹添加了 {len(files)} 个文件"
                )

    def refresh_file_list(self):
        """刷新文件列表"""
        self.list_local_file.clear()

        if not os.path.exists(self.documents_dir):
            return

        for filename in os.listdir(self.documents_dir):
            file_path = os.path.join(self.documents_dir, filename)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                if size < 1024:
                    size_str = f"{size} B"
                elif size < 1024 * 1024:
                    size_str = f"{size / 1024:.1f} KB"
                else:
                    size_str = f"{size / (1024 * 1024):.1f} MB"

                mtime = os.path.getmtime(file_path)
                date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

                item_text = f"{filename}  ({size_str}, {date_str})"
                item = QListWidgetItem(item_text)
                item.setData(Qt.UserRole, file_path)
                self.list_local_file.addItem(item)

    def delete_selected(self):
        """删除选中的文件"""
        # 修复知识库权限（防止写保护）
        self.fix_knowledge_base_permissions()
        if not self.deps_installed:
            QMessageBox.information(self, "提示", "知识库尚未初始化")
            return

        selected_items = self.list_local_file.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "提示", "请先选择要删除的文件")
            return

        reply = QMessageBox.question(
            self, "确认删除",
            f"确定要删除选中的 {len(selected_items)} 个文件吗？\n\n"
            "删除后，这些文件将不再参与知识库检索。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        deleted_count = 0
        for item in selected_items:
            file_path = item.data(Qt.UserRole)
            file_name = os.path.basename(file_path)

            try:
                # 1. 删除物理文件
                os.remove(file_path)

                # 2. 从 Chroma 中删除对应的向量
                if self.deps_installed:
                    all_ids = self.chroma_collection.get()['ids']
                    ids_to_delete = [id for id in all_ids if id.startswith(file_name)]
                    if ids_to_delete:
                        self.chroma_collection.delete(ids=ids_to_delete)
                        if init_config.isInTestMode:
                            print(f"🗑️ 从 Chroma 删除 {len(ids_to_delete)} 个向量: {file_name}")

                deleted_count += 1

            except Exception as e:
                if init_config.isInTestMode:
                    print(f"❌ 删除失败 {file_path}: {e}")

        self.refresh_file_list()

        if self.parent():
            self.parent().DisplayMessage("system", f"🗑️ 已删除 {deleted_count} 个文件")

        QMessageBox.information(self, "删除完成", f"已删除 {deleted_count} 个文件")

    def delete_all(self):
        """清空整个知识库（删除整个 knowledge_base 文件夹）"""
        # 修复知识库权限（防止写保护）
        self.fix_knowledge_base_permissions()
        if not self.deps_installed:
            QMessageBox.information(self, "提示", "知识库尚未初始化")
            return

        reply = QMessageBox.question(
            self, "确认清空",
            "确定要清空整个知识库吗？\n\n这将删除所有已上传的文档和索引，且无法恢复。",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            # 直接删除整个 knowledge_base 文件夹
            import shutil
            shutil.rmtree(self.kb_dir)

            # 重新创建空目录
            os.makedirs(self.documents_dir, exist_ok=True)

            # 重新初始化 Chroma
            if self.deps_installed:
                self._init_chroma()

            self.refresh_file_list()

            if self.parent():
                self.parent().DisplayMessage("system", "🗑️ 知识库已清空")

            QMessageBox.information(self, "清空完成", "知识库已完全清空")

        except Exception as e:
            QMessageBox.warning(self, "清空失败", f"清空知识库失败：{e}")

    def rebuild_index(self):
        """重建知识库索引（先清空 Chroma，再重新索引所有文档）"""
        # 修复知识库权限（防止写保护）
        self.fix_knowledge_base_permissions()
        if not self.deps_installed:
            QMessageBox.information(self, "提示", "知识库尚未初始化")
            return

        reply = QMessageBox.question(
            self, "确认重建",
            "重建索引将删除现有向量数据库，并根据当前文档重新生成。\n\n"
            "这个过程可能需要几分钟，是否继续？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            # 1. 删除整个 chroma 文件夹
            import shutil
            if os.path.exists(self.chroma_dir):
                shutil.rmtree(self.chroma_dir)
                if init_config.isInTestMode:
                    print("🗑️ 已删除旧的 Chroma 数据库")

            # 2. 重新初始化 Chroma
            self._init_chroma()

            # 3. 重新索引所有文档
            doc_count = 0
            for filename in os.listdir(self.documents_dir):
                file_path = os.path.join(self.documents_dir, filename)
                if os.path.isfile(file_path):
                    if self.parent():
                        self.parent().DisplayMessage("system", f"📚 正在索引: {filename}")
                    self._index_document(file_path)
                    doc_count += 1
                    QApplication.processEvents()  # 让界面保持响应

            self.refresh_file_list()

            if self.parent():
                self.parent().DisplayMessage("system", f"📚 知识库索引已重建，共 {doc_count} 个文档")

            QMessageBox.information(self, "重建完成", f"已重建 {doc_count} 个文档的索引")

        except Exception as e:
            QMessageBox.warning(self, "重建失败", f"重建索引失败：{e}")
            if init_config.isInTestMode:
                print(f"❌ 重建失败: {e}")

    def search(self, query, top_k=3):
        """检索知识库（供外部调用）"""
        if not self.deps_installed:
            return ""

        try:
            model = self._get_model()  # 使用本地模型

            query_embedding = model.encode(query).tolist()
            results = self.chroma_collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )

            if results['documents'] and results['documents'][0]:
                return "\n\n---\n\n".join(results['documents'][0])
            return ""

        except Exception as e:
            if init_config.isInTestMode:
                print(f"⚠️ 检索失败: {e}")
            return ""

    def fix_knowledge_base_permissions(self):
        """修复知识库目录权限（仅 macOS/Linux，防止写保护问题）"""

        # 1. 只对 macOS/Linux 执行
        if platform.system() == 'Windows':
            return

        try:
            kb_dir = self._get_kb_dir()

            # 2. 确保目录存在
            if not os.path.exists(kb_dir):
                os.makedirs(kb_dir, exist_ok=True)

            # 3. 检查当前权限（直接读系统状态）
            current_perms = oct(os.stat(kb_dir).st_mode)[-3:]
            expected_perms = '755'

            # 4. 权限已经正确，直接返回（不依赖变量）
            if current_perms == expected_perms:
                if init_config.isInTestMode:
                    print(f"✅ 知识库权限已正确 (755)")
                return

            # 5. 权限不正确，进行修复
            if init_config.isInTestMode:
                print(f"⚠️ 检测到权限异常 (当前={current_perms})，正在修复...")

            # 设置根目录权限
            os.chmod(kb_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

            # 修复子目录
            for subdir in ['chroma', 'documents']:
                sub_path = os.path.join(kb_dir, subdir)
                if os.path.exists(sub_path):
                    os.chmod(sub_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

            if init_config.isInTestMode:
                print(f"✅ 知识库权限已修复为 755")

        except Exception as e:
            if init_config.isInTestMode:
                print(f"⚠️ 权限修复失败: {e}")
