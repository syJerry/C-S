import json
import json
import sys
from typing import List

import logzero
from PySide6.QtCore import Qt, QTimer, Signal, QPropertyAnimation
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QFrame,
    QHBoxLayout, QToolTip, QGraphicsOpacityEffect
)
from PySide6.QtWidgets import QApplication
from json_repair import repair_json
from qfluentwidgets import CommandBar, Action, FluentIcon

from ui.Avatar import Avatar
from ui.ChatBubbleComponent.EvidenceWidget import EvidenceWidget
from ui.ChatBubbleComponent.ParagraphWidget import ParagraphWidget
from ui.ChatBubbleComponent.SmoothBreathingCircle import SmoothBreathingCircle
from ui.ChatBubbleComponent.TypewriterParagraphWidget import TypewriterParagraphWidget


# ---------------------------------------------------------------------------
# ChatBubble
# ---------------------------------------------------------------------------
class ChatBubble(QWidget):
    edit_signal = Signal(str)
    link_signal = Signal(str)

    def __init__(self, text: str, bubble_type=0,
                 evidence_text: List[str] | None = None,
                 typewriter: bool = True,
                 typewriter_interval_ms: int = 20):
        """
        聊天气泡
        :param text:                  聊天内容（AI 气泡为 JSON 字符串）
        :param bubble_type:           0=用户, 1=思考, 2=AI
        :param evidence_text:         回答依据列表
        :param typewriter:            是否启用打字机效果（仅 bubble_type==2 有效）
        :param typewriter_interval_ms: 每个字符的间隔毫秒数（默认 20 ms）
        """
        super().__init__()

        # ---- 打字机状态 ----
        self._typewriter_enabled = typewriter and (bubble_type == 2)
        self._typewriter_interval = typewriter_interval_ms
        self._tw_paragraphs: List[dict] = []  # 待输出的段落列表
        self._tw_para_idx = 0  # 当前段落索引
        self._tw_char_idx = 0  # 当前字符索引
        self._tw_widgets: List[TypewriterParagraphWidget] = []  # 已创建的段落控件
        self._tw_inner_layout: QVBoxLayout | None = None
        self._tw_evidence: List[str] = evidence_text or []
        self._tw_timer = QTimer(self)
        self._tw_timer.timeout.connect(self._typewriter_tick)
        self._tw_evidence_widget_added = False
        self._tw_evidence_text: List[str] = evidence_text or []
        self.bubble_type = bubble_type
        self.text = text
        # ---- 布局 ----
        avatar = Avatar("ui/icon/user.png" if bubble_type == 0 else "ui/icon/robot.png")
        bubble_layout = QVBoxLayout()
        bubble_layout.setSpacing(0)
        bubble_layout.setContentsMargins(0, 0, 0, 0)

        if bubble_type == 0:
            # 用户气泡：纯文本
            message = QLabel()
            message.setTextInteractionFlags(
                Qt.TextInteractionFlag.TextSelectableByMouse |
                Qt.TextInteractionFlag.TextSelectableByKeyboard |
                Qt.TextInteractionFlag.LinksAccessibleByMouse
            )
            message.setCursor(Qt.CursorShape.IBeamCursor)
            message.setTextFormat(Qt.TextFormat.MarkdownText)
            message.setText(text)
            message.setWordWrap(True)
            message.setMaximumWidth(420)
            # message.setMinimumWidth(80)
            message.setStyleSheet(
                """
                QLabel {
                    padding: 10px;
                    border-radius: 10px;
                    background-color: #C3C3C3;
                    font-size: 14px;
                }
                """
            )
            bubble_layout.addWidget(message)

        elif bubble_type == 1:
            breath = SmoothBreathingCircle()
            breath.start()
            bubble_layout.addWidget(breath)

        else:
            # AI 气泡
            paragraphs = self._parse_paragraphs(text)

            inner_frame = QFrame()
            inner_frame.setFrameShape(QFrame.Shape.NoFrame)
            inner_frame.setStyleSheet(
                """
                QFrame {
                    padding: 10px;
                    border-radius: 10px;
                    background-color: #ffffff;
                }
                """
            )
            inner_layout = QVBoxLayout(inner_frame)
            inner_layout.setSpacing(5)
            inner_layout.setContentsMargins(0, 0, 0, 0)

            ev = evidence_text or []

            if self._typewriter_enabled:
                # 打字机模式：预先创建所有 TypewriterParagraphWidget（初始为空），
                # 然后由定时器逐字填充。
                self._tw_paragraphs = paragraphs
                self._tw_inner_layout = inner_layout

                for item in paragraphs:
                    pw = TypewriterParagraphWidget(
                        citations=item.get("citations", []),
                        evidence_text=ev,
                    )
                    inner_layout.addWidget(pw)
                    self._tw_widgets.append(pw)

                self._bubble_layout_ref = bubble_layout  # 用于后续追加 EvidenceWidget
                self._inner_frame_ref = inner_frame

                # 延迟一帧后启动，确保窗口已完成布局
                QTimer.singleShot(0, self._start_typewriter)
            else:
                # 普通模式：直接渲染所有段落
                for item in paragraphs:
                    pw = ParagraphWidget(
                        paragraph=item.get("paragraph", ""),
                        citations=item.get("citations", []),
                        evidence_text=ev,
                    )
                    inner_layout.addWidget(pw)

            bubble_layout.addWidget(inner_frame)

            if ev and not self._typewriter_enabled:
                evidence_widget = EvidenceWidget(ev)
                bubble_layout.addWidget(evidence_widget)

        bubble_container = QFrame()
        bubble_container.setLayout(bubble_layout)
        bubble_container.setFrameShape(QFrame.Shape.NoFrame)
        final_layout = QVBoxLayout(self)
        final_layout.setContentsMargins(0, 0, 0, 0)
        final_layout.setSpacing(0)

        self.commandBar = CommandBar(self)
        self.opacityEffect = QGraphicsOpacityEffect(self.commandBar)
        self.commandBar.setGraphicsEffect(self.opacityEffect)
        self.opacityEffect.setOpacity(0)
        self.anim = QPropertyAnimation(self.opacityEffect, b"opacity")
        self.anim.setDuration(200)

        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(8)

        bar_layout = QHBoxLayout()
        bar_layout.setContentsMargins(0, 0, 0, 0)
        bar_layout.setSpacing(8)
        tem_label = QLabel()
        tem_label.setFixedWidth(40)

        if bubble_type == 0:
            self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
            self.setMouseTracking(True)
            self._addButton(FluentIcon.COPY, '复制', self.on_cody)
            self._addButton(FluentIcon.EDIT, '编辑', self.on_edit)
            self.commandBar.hide()
            bar_layout.addStretch()
            bar_layout.addWidget(self.commandBar)
            bar_layout.addWidget(tem_label)

            layout.addStretch()
            layout.addWidget(bubble_container)
            layout.addWidget(avatar)
            final_layout.addLayout(layout)
            final_layout.addLayout(bar_layout)

        elif bubble_type == 1:
            layout.addWidget(avatar)
            layout.addWidget(bubble_container)
            layout.addStretch()
            final_layout.addLayout(layout)
        else:
            self._addButton(FluentIcon.COPY, '复制', self.on_cody)
            self._addButton(FluentIcon.LINK, '引用', self.on_link)
            bar_layout.addWidget(tem_label)
            bar_layout.addWidget(self.commandBar)
            bar_layout.addStretch()
            layout.addWidget(avatar)
            layout.addWidget(bubble_container)
            layout.addStretch()
            final_layout.addLayout(layout)
            final_layout.addLayout(bar_layout)

    # ------------------------------------------------------------------
    # 打字机驱动
    # ------------------------------------------------------------------
    def _start_typewriter(self):
        if not self._tw_paragraphs:
            return
        self._tw_timer.start(self._typewriter_interval)

    def _typewriter_tick(self):
        """每个 tick 输出一个字符；段落结束后切换到下一段落。"""
        if self._tw_para_idx >= len(self._tw_paragraphs):
            # 所有段落均已输出完毕
            self._tw_timer.stop()
            self._on_typewriter_finished()
            return

        current_para = self._tw_paragraphs[self._tw_para_idx]
        full_text: str = current_para.get("paragraph", "")
        widget: TypewriterParagraphWidget = self._tw_widgets[self._tw_para_idx]

        if self._tw_char_idx < len(full_text):
            # 当前段落还有字符未输出
            widget.append_char(full_text[self._tw_char_idx])
            self._tw_char_idx += 1
        else:
            # 当前段落输出完毕
            widget.finish()
            self._tw_para_idx += 1
            self._tw_char_idx = 0

    def _on_typewriter_finished(self):
        """打字机全部完成后，追加 EvidenceWidget（如有）。"""
        if self._tw_evidence_text and not self._tw_evidence_widget_added:
            self._tw_evidence_widget_added = True
            evidence_widget = EvidenceWidget(self._tw_evidence_text)
            # bubble_layout 即 inner_frame 的父级 layout
            self._bubble_layout_ref.addWidget(evidence_widget)

    def on_cody(self):
        copy_text = ""
        if self.bubble_type == 0:
            copy_text = self.text
        else:
            for item in self._tw_paragraphs:
                copy_text += item.get("paragraph", "")
                copy_text += "\n"
        clipboard = QApplication.clipboard()
        clipboard.setText(copy_text)
        QToolTip.showText(QCursor.pos(), "已复制")

    def on_edit(self):
        self.edit_signal.emit(self.text)

    def on_link(self):
        link_text = ""
        for item in self._tw_paragraphs:
            link_text += item.get("paragraph", "")
            link_text += "\n"
        self.link_signal.emit(link_text)

    def enterEvent(self, event):
        self.commandBar.show()
        self.anim.stop()
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.start()
        self.anim.finished.connect(lambda: self.commandBar.hide() if self.opacityEffect.opacity() == 0 else None)
        super().leaveEvent(event)

    def _addButton(self, icon, text, func: callable):
        action = Action(icon, text, self)
        action.triggered.connect(func)
        self.commandBar.addAction(action)

    def skip_typewriter(self):
        """立即跳过剩余打字机动画，显示全部内容。"""
        self._tw_timer.stop()
        for i in range(self._tw_para_idx, len(self._tw_paragraphs)):
            widget = self._tw_widgets[i]
            remaining = self._tw_paragraphs[i].get("paragraph", "")
            if i == self._tw_para_idx:
                remaining = remaining[self._tw_char_idx:]
            widget.append_text(remaining)
            widget.finish()
        self._tw_para_idx = len(self._tw_paragraphs)
        self._tw_char_idx = 0
        self._on_typewriter_finished()

    # ------------------------------------------------------------------
    @staticmethod
    def _parse_paragraphs(text: str) -> List[dict]:
        try:
            fixed = repair_json(text)
            data = json.loads(fixed)
            print(data)
            if isinstance(data, list):
                return data
        except (json.JSONDecodeError, TypeError) as e:
            logzero.logger.info(f"JSON格式解析失败,code{e}")
            logzero.logger.info(text)
        return [{"paragraph": text, "citations": []}]


# ---------------------------------------------------------------------------
# 本地测试入口
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    text = """
 [
      {
        "paragraph": "SQL注入攻击的基本原理是攻击者通过在用户输入字段（如表单、URL参数）中插入恶意SQL代码，利用应用程序未对输入进行有效验证或转义的漏洞，使这些恶意代码被拼接到后端SQL查询语句中并被执行。例如，若登录验证逻辑为 `SELECT * FROM users WHERE username = '...'`，攻击者输入 `admin' --` 作为用户名，会导致查询变为 `SELECT * FROM users WHERE username = 'admin' --'`，从而绕过密码验证。",
        "citations": [2, 6, 7]
      },
      {
        "paragraph": "参数化查询（又称预编译语句）通过将SQL语句结构与用户输入数据分离来防御SQL注入。在参数化查询中，SQL语句在执行前被数据库引擎预编译，用户输入作为独立参数传入，而非拼接进SQL字符串。",
        "citations": [1]
      },
      {
        "paragraph": "Web应用防火墙（WAF）通过规则匹配检测和拦截可疑请求来防御SQL注入。其优点是部署快速、无需修改源码，适合遗留系统；但缺点明显：WAF依赖黑名单或正则规则，难以应对变种攻击。",
        "citations": [9]
      },
      {
        "paragraph": "在实际系统中，应采用「纵深防御」策略组合使用参数化查询与WAF。首选方案是所有数据库交互必须使用参数化查询，WAF作为第二道防线，用于监控异常流量、记录攻击行为。",
        "citations": [1, 9]
      }
    ]"""
    evidence_text = ["测试依据一的内容", "测试依据二的内容", "测试依据三的内容", "测试依据四的内容",
                     "依据五", "依据六", "依据七", "依据八", "依据九", "依据十"]

    from PySide6.QtWidgets import QApplication, QScrollArea, QPushButton

    app = QApplication(sys.argv)

    win = QWidget()
    win.setWindowTitle("打字机效果演示")
    main_layout = QVBoxLayout(win)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    container = QWidget()
    container_layout = QVBoxLayout(container)
    container_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    # 普通模式气泡
    normal_bubble = ChatBubble(text=text, bubble_type=2, evidence_text=evidence_text,
                               typewriter=False)
    container_layout.addWidget(normal_bubble)

    # 打字机模式气泡
    tw_bubble = ChatBubble(text=text, bubble_type=2, evidence_text=evidence_text,
                           typewriter=True, typewriter_interval_ms=15)
    container_layout.addWidget(tw_bubble)

    scroll.setWidget(container)
    main_layout.addWidget(scroll)

    # 跳过按钮
    skip_btn = QPushButton("跳过动画")
    skip_btn.clicked.connect(tw_bubble.skip_typewriter)
    main_layout.addWidget(skip_btn)

    win.resize(700, 600)
    win.show()
    sys.exit(app.exec())
