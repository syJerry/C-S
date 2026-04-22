import json
import os
from datetime import datetime
from time import sleep
from typing import List

import logzero
from PySide6.QtCore import Signal, QObject, Slot, QThread

from chat.Chat import Chat


class ChatWorker(QObject):
    get_answer_signal = Signal(int, str, str, list)
    new_chat_accomplish_signal = Signal()

    def __init__(self, chats: List[Chat]):
        super().__init__()
        self.chats = chats

    @Slot(int)
    def on_new_chat(self, chat_count):
        sleep(1.0)
        new_chat = Chat(chat_count)
        # self.current_chat_index = chat_count
        self.chats.append(new_chat)
        self.new_chat_accomplish_signal.emit()

    @Slot(int)
    def on_delete_chat(self, index):
        del self.chats[index]
        logzero.logger.info(f"删除完成，聊天列表长度{len(self.chats)}")

    @Slot(str, int)
    def on_question_msg(self, chat_message, index):
        answer = self.chats[index].generate(chat_message)
        summary = ""
        if self.chats[index].summary != "":
            summary = self.chats[index].summary
        reply = answer.get("answer")
        evidence_text = answer.get("basis")[1]
        self.get_answer_signal.emit(index, summary, reply, evidence_text)


class ChatMgr(QObject):
    get_answer_signal = Signal(int, str, str, list)
    new_chat_accomplish_signal = Signal()
    export_chat_accomplish_signal = Signal(bool,int,str)

    worker_new_chat_signal = Signal(int)
    worker_delete_chat_signal = Signal(int)
    worker_get_answer_signal = Signal(str, int)

    def __init__(self, /):
        super().__init__()
        self.chats: List[Chat] = []
        # self.current_chat_index = -1
        self.thread = QThread()
        self.worker = ChatWorker(self.chats)
        self.worker.moveToThread(self.thread)
        self.thread.start()

        self.worker_new_chat_signal.connect(self.worker.on_new_chat)
        self.worker.new_chat_accomplish_signal.connect(self.on_worker_chat_accomplished)

        self.worker_get_answer_signal.connect(self.worker.on_question_msg)
        self.worker.get_answer_signal.connect(self.on_worker_get_answer)

        self.worker_delete_chat_signal.connect(self.worker.on_delete_chat)

    def history(self, index: int):
        if index < 0 or index >= len(self.chats):
            return []
        return self.chats[index].history

    def on_new_chat(self, chat_count):
        self.worker_new_chat_signal.emit(chat_count)

    def on_delete_chat(self, index):
        self.worker_delete_chat_signal.emit(index)

    def on_worker_chat_accomplished(self):
        self.new_chat_accomplish_signal.emit()
        print(f"creat chat {len(self.chats)}")

    def on_question_msg(self, chat_message, index):
        self.worker_get_answer_signal.emit(chat_message, index)

    def on_worker_get_answer(self, idx, summary, reply, evidence_text):
        self.get_answer_signal.emit(idx, summary, reply, evidence_text)

    def on_export_chat(self, idx, folder):
        history = self.history(idx)

        # if not history:
        #     return

        filename = f"chat_{idx}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(folder, filename)

        try:

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=4)
            self.export_chat_accomplish_signal.emit(True,idx,file_path)
            logzero.logger.info(f"导出成功: {file_path}")

        except Exception as e:
            self.export_chat_accomplish_signal.emit(False,idx,"")
            logzero.logger.info("导出失败:", e)


chat_mgr = ChatMgr()
