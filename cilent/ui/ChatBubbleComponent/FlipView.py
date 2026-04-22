from typing import List

from PySide6.QtCore import Qt, Signal, QSize, Property, QRectF, QPropertyAnimation
from PySide6.QtGui import QPainter, QColor, QWheelEvent
from PySide6.QtWidgets import QWidget, QStackedWidget, QTextBrowser, QVBoxLayout, QSizePolicy

from qfluentwidgets import ToolButton, isDarkTheme, drawIcon, SmoothScrollBar, FluentIcon, FluentStyleSheet


class ScrollButton(ToolButton):
    """ Scroll button """

    def _postInit(self):
        self._opacity = 0
        self.opacityAni = QPropertyAnimation(self, b'opacity', self)
        self.opacityAni.setDuration(150)

    def getOpacity(self):
        return self._opacity

    def setOpacity(self, o: float):
        self._opacity = o
        self.update()

    def isTransparent(self):
        return self._opacity == 0

    def fadeIn(self):
        self.opacityAni.setStartValue(self._opacity)
        self.opacityAni.setEndValue(1)
        self.opacityAni.start()

    def fadeOut(self):
        self.opacityAni.setStartValue(self._opacity)
        self.opacityAni.setEndValue(0)
        self.opacityAni.start()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setOpacity(self._opacity)

        # draw background
        if not isDarkTheme():
            painter.setBrush(QColor(252, 252, 252, 217))
        else:
            painter.setBrush(QColor(44, 44, 44, 245))

        painter.drawRoundedRect(self.rect(), 4, 4)

        # draw icon
        if isDarkTheme():
            color = QColor(255, 255, 255)
            opacity = 0.773 if self.isHover or self.isPressed else 0.541
        else:
            color = QColor(0, 0, 0)
            opacity = 0.616 if self.isHover or self.isPressed else 0.45

        painter.setOpacity(self._opacity * opacity)

        s = 6 if self.isPressed else 8
        w, h = self.width(), self.height()
        x, y = (w - s) / 2, (h - s) / 2
        drawIcon(self._icon, painter, QRectF(x, y, s, s), fill=color.name())

    opacity = Property(float, getOpacity, setOpacity)


class MarkdownPage(QTextBrowser):
    """ A single Markdown page rendered via QTextBrowser """

    def __init__(self, markdown: str = "", parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setOpenExternalLinks(True)
        self.setFrameShape(QTextBrowser.NoFrame)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMarkdown(markdown)

    def setContent(self, markdown: str):
        self.setMarkdown(markdown)


class FlipView(QWidget):
    """ Flip view — displays a list of Markdown strings, one page at a time.

    Constructors
    ------------
    * FlipView(`parent`: QWidget = None)
    * FlipView(`orient`: Qt.Orientation, `parent`: QWidget = None)
    """

    currentIndexChanged = Signal(int)

    def __init__(self, orientation: Qt.Orientation = Qt.Horizontal, parent=None):
        # Support both FlipView() and FlipView(Qt.Orientation, parent)
        if isinstance(orientation, QWidget):
            # called as FlipView(parent)
            parent = orientation
            orientation = Qt.Horizontal

        super().__init__(parent)
        self.orientation = orientation
        self._postInit()

    def _postInit(self):
        self.isHover = False
        self._currentIndex = -1
        self._pageSize = QSize(480, 270)
        self._borderRadius = 0

        # Stacked widget holds one MarkdownPage per item
        self.stack = QStackedWidget(self)
        self.stack.setFixedSize(self._pageSize)

        # Scroll buttons
        if self.isHorizontal():
            self.preButton = ScrollButton(FluentIcon.CARE_LEFT_SOLID, self)
            self.nextButton = ScrollButton(FluentIcon.CARE_RIGHT_SOLID, self)
            self.preButton.setFixedSize(16, 38)
            self.nextButton.setFixedSize(16, 38)
        else:
            self.preButton = ScrollButton(FluentIcon.CARE_UP_SOLID, self)
            self.nextButton = ScrollButton(FluentIcon.CARE_DOWN_SOLID, self)
            self.preButton.setFixedSize(38, 16)
            self.nextButton.setFixedSize(38, 16)

        self.preButton.clicked.connect(self.scrollPrevious)
        self.nextButton.clicked.connect(self.scrollNext)

        self.setMinimumSize(self._pageSize)
        self._updateButtonPositions()

    # ------------------------------------------------------------------ #
    #  Orientation helpers
    # ------------------------------------------------------------------ #

    def isHorizontal(self):
        return self.orientation == Qt.Horizontal

    # ------------------------------------------------------------------ #
    #  Page size / border radius properties
    # ------------------------------------------------------------------ #

    def getPageSize(self) -> QSize:
        return self._pageSize

    def setPageSize(self, size: QSize):
        if size == self._pageSize:
            return
        self._pageSize = size
        self.stack.setFixedSize(size)
        self.setMinimumSize(size)
        self._updateButtonPositions()

    def getBorderRadius(self) -> int:
        return self._borderRadius

    def setBorderRadius(self, radius: int):
        self._borderRadius = radius
        # Apply via stylesheet to every page
        style = (
            f"QTextBrowser {{ border-radius: {radius}px; }}"
            if radius > 0 else ""
        )
        for i in range(self.stack.count()):
            self.stack.widget(i).setStyleSheet(style)

    pageSize = Property(QSize, getPageSize, setPageSize)
    borderRadius = Property(int, getBorderRadius, setBorderRadius)

    # ------------------------------------------------------------------ #
    #  Content management
    # ------------------------------------------------------------------ #

    def count(self) -> int:
        return self.stack.count()

    def addPage(self, markdown: str):
        """ Add a single Markdown page. """
        self.addPages([markdown])

    def addPages(self, pages: List[str]):
        """ Add multiple Markdown pages. """
        if not pages:
            return

        for md in pages:
            page = MarkdownPage(md, self.stack)
            if self._borderRadius > 0:
                page.setStyleSheet(
                    f"QTextBrowser {{ border-radius: {self._borderRadius}px; }}"
                )
            self.stack.addWidget(page)

        if self._currentIndex < 0:
            self._currentIndex = 0
            self.stack.setCurrentIndex(0)

    def setPageContent(self, index: int, markdown: str):
        """ Replace the Markdown content of an existing page. """
        if not 0 <= index < self.count():
            return
        self.stack.widget(index).setContent(markdown)

    def pageContent(self, index: int) -> str:
        """ Return the raw Markdown string for *index*. """
        if not 0 <= index < self.count():
            return ""
        return self.stack.widget(index).toMarkdown()

    # ------------------------------------------------------------------ #
    #  Navigation
    # ------------------------------------------------------------------ #

    def currentIndex(self) -> int:
        return self._currentIndex

    def setCurrentIndex(self, index: int):
        """ Navigate to *index*. """
        if not 0 <= index < self.count() or index == self._currentIndex:
            return

        self._currentIndex = index
        self.stack.setCurrentIndex(index)

        # update button visibility
        if index == 0:
            self.preButton.fadeOut()
        elif self.preButton.isTransparent() and self.isHover:
            self.preButton.fadeIn()

        if index == self.count() - 1:
            self.nextButton.fadeOut()
        elif self.nextButton.isTransparent() and self.isHover:
            self.nextButton.fadeIn()

        self.currentIndexChanged.emit(index)

    def scrollPrevious(self):
        self.setCurrentIndex(self._currentIndex - 1)

    def scrollNext(self):
        self.setCurrentIndex(self._currentIndex + 1)

    # ------------------------------------------------------------------ #
    #  Qt event overrides
    # ------------------------------------------------------------------ #

    def resizeEvent(self, e):
        super().resizeEvent(e)
        # Keep the stack centred inside the widget
        sw, sh = self._pageSize.width(), self._pageSize.height()
        self.stack.move(
            int((self.width() - sw) / 2),
            int((self.height() - sh) / 2),
        )
        self._updateButtonPositions()

    def enterEvent(self, e):
        super().enterEvent(e)
        self.isHover = True
        if self._currentIndex > 0:
            self.preButton.fadeIn()
        if self._currentIndex < self.count() - 1:
            self.nextButton.fadeIn()

    def leaveEvent(self, e):
        super().leaveEvent(e)
        self.isHover = False
        self.preButton.fadeOut()
        self.nextButton.fadeOut()

    def wheelEvent(self, e: QWheelEvent):
        e.accept()
        if e.angleDelta().y() < 0:
            self.scrollNext()
        else:
            self.scrollPrevious()

    # ------------------------------------------------------------------ #
    #  Internal helpers
    # ------------------------------------------------------------------ #

    def _updateButtonPositions(self):
        w, h = self.width() or self._pageSize.width(), self.height() or self._pageSize.height()
        bw, bh = self.preButton.width(), self.preButton.height()

        if self.isHorizontal():
            self.preButton.move(2, int(h / 2 - bh / 2))
            self.nextButton.move(w - bw - 2, int(h / 2 - bh / 2))
        else:
            self.preButton.move(int(w / 2 - bw / 2), 2)
            self.nextButton.move(int(w / 2 - bw / 2), h - bh - 2)

        # Always keep buttons on top of the stack widget
        self.preButton.raise_()
        self.nextButton.raise_()


class HorizontalFlipView(FlipView):
    """ Horizontal flip view """

    def __init__(self, parent=None):
        super().__init__(Qt.Horizontal, parent)


class VerticalFlipView(FlipView):
    """ Vertical flip view """

    def __init__(self, parent=None):
        super().__init__(Qt.Vertical, parent)
