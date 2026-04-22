from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Property
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import (
    QWidget
)


# ---------------------------------------------------------------------------
# 呼吸圆（思考动画）
# ---------------------------------------------------------------------------
class SmoothBreathingCircle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._radius = 6
        self.color = QColor(0, 0, 0)
        self.setMinimumSize(40, 40)

        self.anim = QPropertyAnimation(self, b"radius")
        self.anim.setDuration(1000)
        self.anim.setStartValue(4)
        self.anim.setEndValue(10)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.anim.setLoopCount(-1)

    def getRadius(self) -> float:
        return self._radius

    def setRadius(self, value) -> None:
        self._radius = value
        self.update()

    radius = Property(float, getRadius, setRadius)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(self.color)
        painter.setPen(self.color)
        center = self.rect().center()
        painter.drawEllipse(center, self._radius, self._radius)

    def start(self):
        self.anim.start()

    def stop(self):
        self.anim.stop()

