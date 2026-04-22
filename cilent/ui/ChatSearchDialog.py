from PySide6.QtGui import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel


class ChatSearchDialog(QDialog):
    def __init__(self, chat_list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("搜索聊天")
        self.resize(400, 500)
        self.setStyleSheet("""
                QDialog {
                    background-color: #2B3A4D;
                }
            """)
        self.chat_list = chat_list  # 主列表引用

        layout = QVBoxLayout(self)

        # 🔍 搜索框
        self.search_edit = QLineEdit()
        self.search_edit.setMinimumHeight(30)
        self.search_edit.setPlaceholderText("输入关键词...")
        layout.addWidget(self.search_edit)

        # 📋 搜索结果
        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        # 事件
        self.search_edit.textChanged.connect(self.on_search)
        self.result_list.itemClicked.connect(self.on_item_clicked)

    # 🔍 搜索逻辑
    def on_search(self, text):
        self.result_list.clear()
        text = text.lower().strip()

        for i in range(self.chat_list.count()):
            item = self.chat_list.item(i)
            widget = self.chat_list.itemWidget(item)

            if not widget:
                continue

            label = widget.findChild(QLabel, "chat_title")
            content = label.text()
            if text in content.lower():
                # 创建搜索结果项
                result_item = QListWidgetItem(content)
                result_item.setData(Qt.UserRole, i)  # 保存原索引
                self.result_list.addItem(result_item)

    # 👉 点击结果 → 跳转
    def on_item_clicked(self, item):
        index = item.data(Qt.UserRole)

        # 定位到原列表
        self.chat_list.setCurrentRow(index)
        self.chat_list.scrollToItem(self.chat_list.item(index))

        self.accept()