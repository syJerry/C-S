from typing import List

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QTextEdit, QPushButton, QHBoxLayout, QSizePolicy
from qfluentwidgets import StateToolTip, LineEdit

from ui.ChatBubble import ChatBubble


class ChatInput(QTextEdit):
    def __init__(self, send_callback, parent=None):
        super().__init__(parent)
        self.send_callback = send_callback
        self.textChanged.connect(self.update_height)

        self.min_height = 50
        self.max_height = 120
        self.setFont(QFont("Microsoft YaHei", 14))
        self.setFixedHeight(self.min_height)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return and not (event.modifiers() & Qt.KeyboardModifier.ShiftModifier):
            self.send_callback()
        else:
            super().keyPressEvent(event)

    def update_height(self):
        doc = self.document()
        doc_height = doc.size().height() + doc.documentMargin() * 2

        new_height = int(doc_height)

        new_height = max(self.min_height, new_height)
        new_height = min(self.max_height, new_height)

        self.setFixedHeight(new_height)


class ChatWidget(QWidget):
    launch_question_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_widget)
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_layout.addStretch()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.chat_widget)

        self.input = ChatInput(self.on_send)
        self.input.setEnabled(False)
        self.input.setPlaceholderText("有问题，尽管问。")
        self.send_btn = QPushButton()
        self.send_btn.clicked.connect(self.on_send)
        self.send_btn.setEnabled(False)
        self.stateTooltip = None

        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input)
        self.input_layout.addWidget(self.send_btn)
        self.input_layout.setContentsMargins(10, 0, 10, 0)  # 去掉外边距
        self.input_layout.setSpacing(0)  # 去掉组件间距
        self.input_widget = QWidget()
        self.input_widget.setObjectName("input")
        self.input_widget.setLayout(self.input_layout)
        self.input_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.input_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.init_style()
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.scroll)
        right_layout.addWidget(self.input_widget)

        self.setLayout(right_layout)

    def on_send(self):
        if self.send_btn.isEnabled():
            self.send_btn.setEnabled(False)
        else:
            return
        if not self.stateTooltip:
            self.stateTooltip = StateToolTip('正在等待Aria回复', '等待是为了更好的重逢~~', self)
            self.stateTooltip.move(10, 30)
            self.stateTooltip.show()
        msg = self.input.toPlainText().strip()
        if not msg:
            self.send_btn.setEnabled(True)
            return
        user_bubble = ChatBubble(msg, bubble_type=0)
        user_bubble.edit_signal.connect(self.on_edit)

        think_bubble = ChatBubble("",bubble_type=1)
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, user_bubble)
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, think_bubble)
        self.launch_question_signal.emit(msg)
        self.input.clear()
        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )
        print("send accomplish!")

    def on_get_answer(self, draw:bool,summary:str, reply:str, evidence_text:List[str]):
        if self.stateTooltip:
            self.stateTooltip.setContent('Aria依据回复啦 😆')
            self.stateTooltip.setState(True)
            self.stateTooltip = None
        if not draw:
            return
        ai_bubble = ChatBubble(
            reply,
            bubble_type=2,
            evidence_text=evidence_text
        )
        ai_bubble.link_signal.connect(self.on_link)
        count = self.chat_layout.count()
        if count > 1:  # 至少要保留最后那个输入区域
            item = self.chat_layout.takeAt(count - 2)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, ai_bubble)
        self.scroll.verticalScrollBar().setValue(
            self.scroll.verticalScrollBar().maximum()
        )
        self.send_btn.setEnabled(True)

        print("ui draw answer accomplish")

    def on_chat_change(self, index:int):
        self.send_btn.setEnabled(True)
        self.input.setEnabled(True)
        self.input.clear()
        while self.chat_layout.count() > 1:
            item = self.chat_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self.load_history_of_chat(index)
        print("ui draw changed chat accomplish")

    def on_empty(self):
        self.input.setEnabled(False)
        self.send_btn.setEnabled(False)

    def on_edit(self,text:str):
        self.input.setText(text)

    def on_link(self,text:str):
        self.input.setText(text)

    def load_history_of_chat(self, index:int):
        from ui.ChatMgr import chat_mgr
        for d in chat_mgr.history(index):
            msg = d.get("user")
            user_bubble = ChatBubble(msg, bubble_type=0)
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, user_bubble)

            reply = d.get("assistant")
            evidence_text = d.get("basis")[0]
            ai_bubble = ChatBubble(
                reply,
                bubble_type=2,
                evidence_text=evidence_text
            )
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, ai_bubble)
            self.scroll.verticalScrollBar().setValue(
                self.scroll.verticalScrollBar().maximum()
            )

    def init_style(self):
        self.input_widget.setStyleSheet(
            """
            #input {
                background-color: #ffffff;
                border: 1px solid rgba(0,0,0,0.4);
                border-radius: 25px;
            }
            """
        )
        self.input.setStyleSheet(
            """
                QTextEdit {
                    border: none;
                    background: transparent;
                    padding: 6px;
                }   
            """
        )
        self.send_btn.setFixedSize(36, 36)
        self.send_btn.setIcon(QIcon("ui/icon/send.png"))
        self.send_btn.setIconSize(QSize(25,25))
        self.send_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_btn.setStyleSheet("""
        QPushButton {
            border-radius: 18px;
            background-color: #E3E3E3;
            border: 1px solid rgba(0,0,0,0.4);
        }
        QPushButton:hover {
            background-color: #C3C3C3;
        }
        QPushButton:disabled {
            background-color: #F0F0F0;
            border: 1px solid rgba(0,0,0,0.2);
        }
        """)
