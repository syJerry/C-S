import html
from typing import List

import markdown
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QToolTip
)

from ui.ChatBubbleComponent.EvidenceWidget import EvidencesView


# ---------------------------------------------------------------------------
# 打字机段落：支持逐字符追加，完成后渲染引用徽章
# ---------------------------------------------------------------------------
class TypewriterParagraphWidget(QWidget):
    """
    支持打字机效果的段落控件。
    - 先以纯文本逐字符追加，实时渲染 Markdown → HTML
    - 调用 finish() 后附加引用徽章并锁定内容
    """

    def __init__(self, citations: List[int], evidence_text: List[str], parent=None):
        super().__init__(parent)

        self._citations = citations
        self._evidence_text = evidence_text
        self._raw_text = ""  # 累积的纯文本
        self._finished = False
        self._view: EvidencesView | None = None

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        self.label = QLabel()
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setOpenExternalLinks(False)
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(420)
        self.label.setStyleSheet(
            """
            QLabel {
                padding: 0px;
                font-size: 14px;
                background: transparent;
            }
            """
        )

        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.TextSelectableByKeyboard |
            Qt.TextInteractionFlag.LinksAccessibleByMouse
        )
        self.setCursor(Qt.CursorShape.IBeamCursor)

        self.label.linkActivated.connect(self._on_link_activated)
        self.label.linkHovered.connect(self._on_link_hovered)
        outer.addWidget(self.label)

    # ------------------------------------------------------------------
    # 打字机追加接口
    # ------------------------------------------------------------------
    def append_char(self, char: str):
        """追加一个字符，实时更新显示（不带引用徽章）。"""
        if self._finished:
            return
        self._raw_text += char
        self.label.setText(markdown.markdown(self._raw_text))

    def append_text(self, text: str):
        """批量追加文本（多字符），实时更新显示。"""
        if self._finished:
            return
        self._raw_text += text
        self.label.setText(markdown.markdown(self._raw_text))

    def finish(self):
        """段落输出完毕：渲染引用徽章并锁定。"""
        if self._finished:
            return
        self._finished = True

        html_body = markdown.markdown(self._raw_text)
        badge_html = self._build_badges()

        if badge_html:
            if html_body.rstrip().endswith("</p>"):
                html_body = html_body.rstrip()[:-4] + badge_html + "</p>"
            else:
                html_body += badge_html

        self.label.setText(html_body)

    # ------------------------------------------------------------------
    # 内部
    # ------------------------------------------------------------------
    def _build_badges(self) -> str:
        badge_html = ""
        for idx in self._citations:
            display_num = idx + 1
            if 0 <= idx < len(self._evidence_text):
                preview = html.escape(self._evidence_text[idx][:200])
                if len(self._evidence_text[idx]) > 200:
                    preview += "…"
            else:
                preview = ""
            badge_html += (
                f"""<a href="cite://{idx}" """
                f"""style="background-color:#E3E6E9;color:#575859;"""
                f"""padding:40px 40px;border-radius:999px;"""
                f"""text-decoration:none;font-size:12px;margin-left:6px;">"""
                f"""[{display_num}]</a>&nbsp;"""
            )
        return badge_html

    def _on_link_activated(self, link: str):
        if link.startswith("cite://"):
            try:
                idx = int(link[len("cite://"):])
            except ValueError:
                return
            self._view = EvidencesView(self._evidence_text)
            if 0 <= idx < len(self._evidence_text):
                self._view.hView.setCurrentIndex(idx)
                self._view.pager.setCurrentIndex(idx)
            self._view.show()

    def _on_link_hovered(self, link: str):
        if link.startswith("cite://"):
            try:
                idx = int(link[len("cite://"):])
            except ValueError:
                return
            if 0 <= idx < len(self._evidence_text):
                text = self._evidence_text[idx][:200]
                if len(self._evidence_text[idx]) > 200:
                    text += "…"
                QToolTip.showText(QCursor.pos(), text)
            else:
                QToolTip.hideText()
        else:
            QToolTip.hideText()

