from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import HorizontalPipsPager

from ui.ChatBubbleComponent.FlipView import HorizontalFlipView


class EvidencesView(QWidget):
    """
    展示所有依据的翻页视图（Modal 窗口）。
    hView 和 pager 作为公开属性，供 CitationTag 在打开后直接定位到指定页。
    """

    def __init__(self, evidences: list[str]):
        super().__init__()
        self.setWindowTitle("回答依据")
        self.evidences = evidences
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # 公开属性，方便外部定位
        self.pager = HorizontalPipsPager(self)
        self.hView: HorizontalFlipView | None = None

        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)

        self.hView = HorizontalFlipView(self)
        self.hView.setBorderRadius(8)
        self.hView.addPages(self.evidences)
        root.addWidget(self.hView)

        self.pager.setPageNumber(self.hView.count())
        self.pager.currentIndexChanged.connect(self.hView.setCurrentIndex)
        self.hView.currentIndexChanged.connect(self.pager.setCurrentIndex)

        root.addWidget(self.pager, 0, Qt.AlignmentFlag.AlignCenter)


class EvidenceWidget(QWidget):
    """气泡底部的"查看依据"整体入口按钮，打开 EvidencesView 并停在第 0 页。"""

    def __init__(self, text: list[str]):
        super().__init__()

        # self.toggle_btn = PushButton("查看依据", self)
        # self.toggle_btn.setFlat(True)
        # self.toggle_btn.setToolTip("点击查看知识库检索结果。")
        # self.toggle_btn.clicked.connect(self.toggle)

        self.content = EvidencesView(text)

        # layout = QVBoxLayout(self)
        # layout.setContentsMargins(0, 5, 0, 0)
        # layout.addWidget(self.toggle_btn)

    def toggle(self):
        self.content.show()
