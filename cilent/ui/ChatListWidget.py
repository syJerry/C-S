from PySide6.QtCore import Signal, Slot, Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QWidget, QListWidgetItem, QHBoxLayout, QLabel, \
    QMenu, QToolButton, QLineEdit, QFileDialog
from qfluentwidgets import IndeterminateProgressBar, PushButton, ToolButton, TransparentToolButton, setTheme, Theme, \
    RoundMenu, Action, MenuAnimationType, MessageBox, InfoBarIcon, TeachingTipTailPosition, TeachingTip
from qfluentwidgets import FluentIcon as FIF

from ui.ChatMgr import chat_mgr
from ui.ChatSearchDialog import ChatSearchDialog


def colored_svg(icon_path, color, size=16):
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)

    renderer = QSvgRenderer(icon_path)

    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))
    painter.end()

    return pixmap


class ChatListWidget(QWidget):
    chat_change_signal = Signal(int)
    new_chat_signal = Signal(int)
    question_msg_signal = Signal(str, int)
    delete_chat_signal = Signal(int)
    empty_signal = Signal()
    get_answer_signal = Signal(bool, str, str, list)
    export_chat_signal = Signal(int,str)

    def __init__(self):
        super().__init__()
        self.new_chat_btn = QPushButton("  新建聊天", self)
        self.new_chat_btn.setToolTip("创建新的主题聊天！")
        self.new_chat_btn.clicked.connect(self.on_new_chat)
        self.new_chat_btn.setFixedHeight(35)
        self.new_chat_btn.setIcon(FIF.LABEL.icon(Theme.DARK))

        self.search_btn = QPushButton(" 搜索聊天",self)
        self.search_btn.setToolTip("搜索聊天主题！")
        self.search_btn.setFixedHeight(35)
        self.search_btn.setIcon(FIF.SEARCH.icon(Theme.DARK))
        self.search_btn.clicked.connect(self.on_search_chat)

        self.inProgressBar = IndeterminateProgressBar(self)
        self.inProgressBar.stop()
        self.chat_list = QListWidget()
        self.chat_list.currentRowChanged.connect(self.on_chat_changed)

        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.new_chat_btn)
        self.left_layout.addWidget(self.search_btn)
        self.left_layout.addWidget(self.inProgressBar)
        self.left_layout.addWidget(self.chat_list)
        self.left_layout.setContentsMargins(10, 10, 10, 10)  # 去掉外边距
        self.left_layout.setSpacing(5)
        self.setLayout(self.left_layout)
        self.setObjectName("Panel")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.init_style()

    def on_new_chat(self):
        self.inProgressBar.start()
        self.new_chat_btn.setEnabled(False)
        self.new_chat_signal.emit(self.chat_list.count())
        print("ask for new chat")

    def on_search_chat(self):
        dialog = ChatSearchDialog(self.chat_list, self)
        dialog.exec_()

    def on_new_chat_accomplish(self):
        item = QListWidgetItem(self.chat_list)
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        icon = QLabel()
        icon.setPixmap(QPixmap("ui/icon/chat.svg").scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio,
                                                          Qt.TransformationMode.SmoothTransformation))
        label = QLabel()
        font = QFont()
        font.setPointSize(11)
        label.setFont(font)
        label.setText("新建聊天")
        label.setObjectName("chat_title")
        label.setStyleSheet("color: white;")
        more_btn = TransparentToolButton(FIF.MORE.icon(Theme.DARK), widget)
        more_btn.clicked.connect(lambda: self.show_item_menu(more_btn, item))
        layout.addWidget(icon)
        layout.addWidget(label)
        layout.addWidget(more_btn)
        widget.setLayout(layout)
        widget.setCursor(Qt.CursorShape.PointingHandCursor)

        self.chat_list.setItemWidget(item, widget)
        self.chat_list.setCurrentItem(item)
        self.new_chat_btn.setEnabled(True)
        self.inProgressBar.stop()
        print("ui draw new chat")

    def on_chat_changed(self):
        self.chat_change_signal.emit(self.chat_list.currentRow())
        print(f"change to chat [{self.chat_list.currentRow()}]")

    def on_get_answer(self, index, summary, reply, evidence_text):
        item = self.chat_list.item(index)
        widget = self.chat_list.itemWidget(item)
        label = widget.findChild(QLabel, "chat_title")
        label.setText(summary)
        if index == self.chat_list.currentRow():
            self.get_answer_signal.emit(True, summary, reply, evidence_text)
        else:
            self.get_answer_signal.emit(False, summary, reply, evidence_text)

        print(f"refresh chat[{self.chat_list.currentRow()}] summary")

    def on_launch_question(self, msg):
        self.question_msg_signal.emit(msg, self.chat_list.currentRow())
        print(f"ask for question chat[{self.chat_list.currentRow()}]")

    def on_delete_chat(self, item):
        title = "确定要删除这个聊天吗？"
        content = "删除后，这份聊天将无法恢复！如需保存请先导出！"
        w = MessageBox(title, content, self.parent())
        w.setClosableOnMaskClicked(True)
        w.setDraggable(True)
        if not w.exec():
            return
        row = self.chat_list.row(item)
        self.chat_list.takeItem(row)
        if self.chat_list.count() <= 0:
            self.empty_signal.emit()
        self.delete_chat_signal.emit(row)

    def on_export_accomplish(self,success:bool,idx,filename):
        item = self.chat_list.item(idx)
        widget = self.chat_list.itemWidget(item)
        if success:
            TeachingTip.create(
                target=widget,
                icon=InfoBarIcon.SUCCESS,
                title='聊天导出',
                content=f"聊天文件已保存至“{filename}”",
                isClosable=True,
                tailPosition=TeachingTipTailPosition.TOP,
                duration=2000,
                parent=self
            )
        else:
            TeachingTip.create(
                target=widget,
                icon=InfoBarIcon.ERROR,
                title='聊天导出',
                content=f"聊天文件导出失败！",
                isClosable=True,
                tailPosition=TeachingTipTailPosition.TOP,
                duration=2000,
                parent=self
            )

    def on_rename_chat(self, item):

        # 1️⃣ 获取 item 对应的 widget
        widget = self.chat_list.itemWidget(item)

        # 假设你的 layout 是：
        # [icon, label, more_btn]
        layout = widget.layout()
        label = layout.itemAt(1).widget()  # 中间那个 label

        old_text = label.text()

        # 2️⃣ 创建输入框
        edit = QLineEdit(old_text)
        edit.setFocus()
        edit.selectAll()
        edit.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
            }
        """)
        # 3️⃣ 替换 label → edit
        layout.replaceWidget(label, edit)
        label.hide()

        # 4️⃣ 定义保存逻辑
        def finish_edit():
            new_text = edit.text().strip()
            if new_text:
                label.setText(new_text)

            # 还原 UI
            layout.replaceWidget(edit, label)
            edit.deleteLater()
            label.show()

        # 5️⃣ 回车 / 失焦 结束编辑
        edit.editingFinished.connect(finish_edit)

    def on_export_chat(self,item):
        row = self.chat_list.row(item)
        folder = QFileDialog.getExistingDirectory(
            self,
            "选择文件夹",  # 标题
            ""
        )
        self.export_chat_signal.emit(row,folder)

    def show_item_menu(self, btn, item):
        menu = RoundMenu()
        export_action = Action(FIF.DOWNLOAD, '导出聊天')
        rename_action = Action(FIF.EDIT, "重命名")
        delete_action = Action(FIF.DELETE.icon(color="red"), '删除聊天')
        menu.addAction(export_action)
        menu.addAction(rename_action)
        menu.addAction(delete_action)

        export_action.triggered.connect(lambda: self.on_export_chat(item))
        delete_action.triggered.connect(lambda: self.on_delete_chat(item))
        rename_action.triggered.connect(lambda: self.on_rename_chat(item))

        pos = btn.mapToGlobal(btn.rect().bottomLeft())
        menu.exec(pos, aniType=MenuAnimationType.DROP_DOWN)

    def init_style(self):
        self.new_chat_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
        #Panel {
            background-color: #2B3A4D;
        }

        QPushButton {
            background-color: transparent;
            border: 1px solid rgba(255,255,255,0.4);
            padding: 8px 12px;
            border-radius: 10px;
            color: white;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: rgba(255,255,255,0.2);
        }

        QPushButton:pressed {
            background-color: rgba(255,255,255,0.5);
        }

        /* 聊天列表 */
        QListWidget {
            background-color: transparent;
            border: none;
            outline: none;
            color: white
        }

        /* 每一项 */
        QListWidget::item {
            padding: 8px;
            border-radius: 20px;
            color: white
        }

        /* 鼠标悬停 */
        QListWidget::item:hover {
            background-color: rgba(255,255,255,0.2);
        }

        /* 当前选中 */
        QListWidget::item:selected {
            background-color: rgba(255,255,255,0.5);
            color: white;
        }
        """)
