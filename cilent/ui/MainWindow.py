# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout
)
from ui.ChatMgr import chat_mgr
from ui.VoiceWidget import VoiceWidget


# class ChatMgrLoader(QThread):
#     """在后台线程中导入耗时的 chat_mgr 模块"""
#     finished = Signal(object)  # 导入完成后传出 chat_mgr 实例
#
#     def run(self):
#         from ui.ChatMgr import chat_mgr  # 耗时导入放在这里
#         self.finished.emit(chat_mgr)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aria-你的信息安全助手")
        self.resize(900, 600)

        from ui.ChatListWidget import ChatListWidget
        from ui.ChatWidget import ChatWidget

        self.left_container = ChatListWidget()
        self.right_container = ChatWidget()
        # self.voice_mode = VoiceWidget(exit_func=self.exit_voice_mode)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.left_container, 1)
        main_layout.addWidget(self.right_container, 4)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.container = QWidget()
        self.container.setLayout(main_layout)

        self.setCentralWidget(self.container)

        self.left_container.new_chat_signal.connect(chat_mgr.on_new_chat)
        self.left_container.chat_change_signal.connect(self.right_container.on_chat_change)
        self.left_container.question_msg_signal.connect(chat_mgr.on_question_msg)
        self.left_container.delete_chat_signal.connect(chat_mgr.on_delete_chat)
        self.left_container.empty_signal.connect(self.right_container.on_empty)
        self.left_container.get_answer_signal.connect(self.right_container.on_get_answer)
        self.left_container.export_chat_signal.connect(chat_mgr.on_export_chat)
        self.right_container.launch_question_signal.connect(self.left_container.on_launch_question)

        chat_mgr.get_answer_signal.connect(self.left_container.on_get_answer)
        chat_mgr.new_chat_accomplish_signal.connect(self.left_container.on_new_chat_accomplish)
        chat_mgr.export_chat_accomplish_signal.connect(self.left_container.on_export_accomplish)

    def exit_voice_mode(self):
        self.setCentralWidget(self.container)

# def make_splash_pixmap(width=500, height=300) -> QPixmap:
#     pix = QPixmap("ui/icon/00.jpeg")
#     pix = pix.scaled(900, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation)
#     return pix


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     # ① 显示启动画面
#     splash = QSplashScreen(make_splash_pixmap(), Qt.WindowStaysOnTopHint)
#     splash.show()
#     app.processEvents()  # 确保启动画面立刻渲染出来
#
#     main_win = None  # 提前声明，防止被 GC 回收
#
#
#     def on_load_finished(chat_mgr):
#         global main_win
#         # ② 导入完成 → 创建主窗口
#         main_win = MainWindow(chat_mgr)
#         main_win.show()
#         splash.finish(main_win)  # 关闭启动画面，平滑过渡到主窗口
#
#
#     # ③ 后台线程执行耗时导入
#     loader = ChatMgrLoader()
#     loader.finished.connect(on_load_finished)
#     loader.start()
#
#     sys.exit(app.exec())
