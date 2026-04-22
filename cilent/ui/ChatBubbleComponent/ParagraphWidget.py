import html
from typing import List

import markdown
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QToolTip
)

from ui.ChatBubbleComponent.EvidenceWidget import EvidencesView


class ParagraphWidget(QWidget):
    """
    单段落：HTML 富文本，行内引用标签直接嵌入文字末尾。
    引用标签以 <a href="cite://N"> 形式渲染，点击触发 linkActivated 信号。
    """

    def __init__(self, paragraph: str, citations: List[int],
                 evidence_text: List[str], parent=None):
        super().__init__(parent)

        self._evidence_text = evidence_text
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

        html_body = self._md_to_html(paragraph)

        badge_html = ""
        for idx in citations:
            display_num = idx + 1
            if 0 <= idx < len(evidence_text):
                preview = html.escape(evidence_text[idx][:200])
                if len(evidence_text[idx]) > 200:
                    preview += "…"
            else:
                preview = ""
            badge_html += (
                f"""
                <a href="cite://{idx}" 
                style="
                background-color:#E3E6E9;
                color:#575859;
                padding:40px 40px;
                border-radius:999px;
                text-decoration:none;
                font-size:12px;
                margin-left:6px;"
                >[{display_num}]</a>&nbsp;"""
            )

        if badge_html:
            if html_body.rstrip().endswith("</p>"):
                html_body = html_body.rstrip()[:-4] + badge_html + "</p>"
            else:
                html_body += badge_html

        self.label.setText(html_body)
        self.label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.TextSelectableByKeyboard |
            Qt.TextInteractionFlag.LinksAccessibleByMouse
        )
        self.setCursor(Qt.CursorShape.IBeamCursor)

        self.label.linkActivated.connect(self._on_link_activated)
        self.label.linkHovered.connect(self._on_link_hovered)
        outer.addWidget(self.label)

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

    @staticmethod
    def _md_to_html(text: str) -> str:
        return markdown.markdown(text)

