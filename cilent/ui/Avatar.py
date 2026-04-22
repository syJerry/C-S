from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt


class Avatar(QLabel):
    def __init__(self, icon_path, color="#ffffff"):
        super().__init__()

        size = 40
        icon_size = 22

        self.setFixedSize(size, size)

        pix = QPixmap(size, size)
        pix.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pix)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 画圆形背景
        # painter.setBrush(QColor(color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, size, size)

        # 加载 icon
        icon = QPixmap(icon_path).scaled(
            icon_size,
            icon_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        # 计算居中位置
        x = (size - icon.width()) // 2
        y = (size - icon.height()) // 2

        painter.drawPixmap(x, y, icon)

        painter.end()

        self.setPixmap(pix)