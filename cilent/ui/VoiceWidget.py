import os
import wave
import tempfile
from dataclasses import dataclass
from typing import Callable, Any, Optional, Union

from PySide6.QtCore import Qt, QBuffer, QByteArray, QIODevice, QThread, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
)
from PySide6.QtMultimedia import QAudioFormat, QAudioSource, QMediaDevices


@dataclass
class IntentResult:
    code: int
    param: Any = None


class FunctionWorker(QThread):
    finished_ok = Signal(object)
    finished_error = Signal(str)

    def __init__(self, func: Callable, *args):
        super().__init__()
        self.func = func
        self.args = args

    def run(self):
        try:
            self.finished_ok.emit(self.func(*self.args))
        except Exception as e:
            self.finished_error.emit(str(e))


class VoiceWidget(QWidget):
    """
    视障人士语音控制界面。

    你需要传入：
    1. asr_func(audio_path) -> str
       语音识别接口，输入 wav 文件路径，返回识别文本。

    2. intent_func(text) -> dict / tuple / IntentResult
       大模型意图识别接口，返回功能序号和参数。
       支持格式：
       {"code": 2, "param": "什么是SQL注入"}
       (2, "什么是SQL注入")
       IntentResult(2, "什么是SQL注入")

    3. tts_func(text)
       语音播报接口。

    4. 业务回调：
       new_chat_func()
       switch_chat_by_index_func(index)
       search_chat_func(keyword)
       send_func(text)
       get_chat_content_func(start_from)
       exit_func()
    """
    voice_new_chat_signal = Signal()
    voice_switch_chat_signal = Signal(int)
    voice_send_signal = Signal(str)
    voice_get_chat_content_signal = Signal(int)
    voice_get_chat_list_signal = Signal()

    def __init__(
            self,
            asr_func: Callable[[str], str],
            intent_func: Callable[[str], Union[dict, tuple, IntentResult]],
            tts_func: Callable[[str], None],
            new_chat_func: Callable[[], None],
            switch_chat_by_index_func: Callable[[int], None],
            search_chat_func: Callable[[str], None],
            send_func: Callable[[str], None],
            get_chat_content_func: Callable[[int], str],
            exit_func: Callable[[], None],
            parent=None,
    ):
        super().__init__(parent)

        self.asr_func = asr_func
        self.intent_func = intent_func
        self.tts_func = tts_func

        self.exit_func = exit_func

        self.audio_source: Optional[QAudioSource] = None
        self.audio_buffer: Optional[QBuffer] = None
        self.audio_data: Optional[QByteArray] = None
        self.recording = False

        self.current_audio_path = None
        self.worker = None

        self.content = None

        self.guide_text = (
            "已进入语音控制模式。"
            "本界面适配视障用户."
            "点击话筒后开始录音，再次点击结束录音。"
            "你可以说：新建聊天；切换到第一个聊天；切换到关于 SQL 注入的聊天；"
            "输入什么是 SQL 注入攻击；阅读全部聊天内容；阅读最近三条聊天内容。"
            "系统会识别你的语音，并自动执行对应操作。"
            "按退出按钮或键盘 ESC 可以返回之前的界面。"
        )

        self._init_ui()
        self._init_audio()

    def _init_ui(self):
        self.setWindowTitle("语音控制模式")
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(30)

        self.title_label = QLabel("语音控制模式")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 32px; font-weight: bold;")

        self.status_label = QLabel("点击话筒开始语音输入")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 22px;")

        self.mic_button = QPushButton("🎙")
        self.mic_button.setFixedSize(260, 260)
        self.mic_button.setAccessibleName("语音输入话筒按钮")
        self.mic_button.setAccessibleDescription("点击开始录音，再次点击结束录音")
        self.mic_button.setStyleSheet("""
            QPushButton {
                font-size: 110px;
                border-radius: 130px;
                background-color: #2f80ed;
                color: white;
            }
            QPushButton:hover {
                background-color: #1c6ed6;
            }
        """)
        self.mic_button.clicked.connect(self.toggle_recording)

        self.exit_button = QPushButton("退出语音控制")
        self.exit_button.setFixedHeight(60)
        self.exit_button.setAccessibleName("退出语音控制按钮")
        self.exit_button.setStyleSheet("font-size: 22px;")
        self.exit_button.clicked.connect(self.exit_voice_mode)

        layout.addWidget(self.title_label)
        layout.addWidget(self.mic_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)
        layout.addWidget(self.exit_button)

    def _init_audio(self):
        fmt = QAudioFormat()
        fmt.setSampleRate(16000)
        fmt.setChannelCount(1)
        fmt.setSampleFormat(QAudioFormat.Int16)

        device = QMediaDevices.defaultAudioInput()
        if not device.isFormatSupported(fmt):
            fmt = device.preferredFormat()

        self.audio_format = fmt
        self.audio_device = device

    def showEvent(self, event):
        super().showEvent(event)
        self._speak(self.guide_text)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.exit_voice_mode()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Space):
            self.toggle_recording()
        else:
            super().keyPressEvent(event)

    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.recording = True
        self.status_label.setText("正在录音，再次点击话筒结束")
        self.mic_button.setText("■")
        self.mic_button.setStyleSheet("""
            QPushButton {
                font-size: 100px;
                border-radius: 130px;
                background-color: #eb5757;
                color: white;
            }
        """)

        self.audio_data = QByteArray()
        self.audio_buffer = QBuffer(self.audio_data)
        self.audio_buffer.open(QIODevice.OpenModeFlag.WriteOnly)

        self.audio_source = QAudioSource(self.audio_device, self.audio_format)
        self.audio_source.start(self.audio_buffer)

        self._speak("开始录音。请说出你的指令。")

    def stop_recording(self):
        self.recording = False

        if self.audio_source:
            self.audio_source.stop()
        if self.audio_buffer:
            self.audio_buffer.close()

        self.status_label.setText("录音结束，正在识别")
        self.mic_button.setText("🎙")
        self.mic_button.setStyleSheet("""
            QPushButton {
                font-size: 110px;
                border-radius: 130px;
                background-color: #2f80ed;
                color: white;
            }
        """)

        wav_path = self._save_wav()
        self.current_audio_path = wav_path

        self.worker = FunctionWorker(self.asr_func, wav_path)
        self.worker.finished_ok.connect(self._on_asr_finished)
        self.worker.finished_error.connect(self._on_error)
        self.worker.start()

    def _save_wav(self) -> str:
        fd, path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)

        raw_data = bytes(self.audio_data)

        sample_width = 2
        channels = self.audio_format.channelCount()
        sample_rate = self.audio_format.sampleRate()

        with wave.open(path, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(sample_rate)
            wf.writeframes(raw_data)

        return path

    def _on_asr_finished(self, text: str):
        text = text.strip()
        if not text:
            self.status_label.setText("未识别到有效语音")
            self._speak("没有识别到有效语音，请重新点击话筒输入。")
            return

        self.status_label.setText(f"识别结果：{text}")
        self._speak(f"识别到：{text}。正在判断功能。")

        self.worker = FunctionWorker(self.intent_func, text)
        self.worker.finished_ok.connect(self._on_intent_finished)
        self.worker.finished_error.connect(self._on_error)
        self.worker.start()

    def _on_intent_finished(self, result):
        intent = self._normalize_intent(result)
        code = intent.code
        param = intent.param

        if code == 0:
            self.voice_new_chat_signal.emit()
            self.status_label.setText("已新建聊天，并切换至新聊天")
            self._speak("已新建聊天，并切换至新聊天")

        elif code == 1:
            self.voice_switch_chat_signal.emit(param)
            self.status_label.setText(f"已切换到第 {param} 个聊天")
            self._speak(f"已切换到第 {param} 个聊天。")

        elif code == 2:
            text = str(param).strip()
            if not text:
                self.status_label.setText("输入内容为空")
                self._speak("输入内容为空，请重新输入。")
                return

            self.voice_send_signal.emit(text)
            self.status_label.setText(f"已发送：{text}")
            self._speak("已发送问题。")

        elif code == 3:
            try:
                start_from = int(param)
            except Exception:
                start_from = 0
            self.voice_get_chat_content_signal.emit(start_from)

        elif code == 4:
            self.voice_get_chat_list_signal.emit()
        else:
            self.status_label.setText("无效功能")
            self._speak("没有识别到有效功能，请重新输入。")

    def on_get_chat_content(self):
        if not self.content:
            self.status_label.setText("当前没有可阅读的聊天内容")
            self._speak("当前没有可阅读的聊天内容。")
        else:
            self.status_label.setText("正在阅读聊天内容")
            self._speak(self.content)
        self.content = None

    def on_get_chat_list(self):
        if not self.content:
            self.status_label.setText("当前没有可阅读的聊天主题")
            self._speak("当前没有可阅读的聊天主题。")
        else:
            self.status_label.setText("聊天主题")
            self._speak(self.content)
        self.content = None

    def _normalize_intent(self, result) -> IntentResult:
        if isinstance(result, IntentResult):
            return result

        if isinstance(result, dict):
            return IntentResult(
                code=int(result.get("code", -1)),
                param=result.get("param", None)
            )

        if isinstance(result, tuple) or isinstance(result, list):
            code = int(result[0]) if len(result) > 0 else -1
            param = result[1] if len(result) > 1 else None
            return IntentResult(code=code, param=param)

        return IntentResult(code=-1, param=None)

    def _on_error(self, msg: str):
        self.status_label.setText("语音控制出现错误")
        self._speak("语音控制出现错误，请重试。")
        QMessageBox.warning(self, "错误", msg)

    def _speak(self, text: str):
        self.worker_tts = FunctionWorker(self.tts_func, text)
        self.worker_tts.start()

    def exit_voice_mode(self):
        if self.recording:
            self.stop_recording()

        self._speak("已退出语音控制模式。")
        self.exit_func()
