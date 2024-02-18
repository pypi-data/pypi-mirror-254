import os

from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QDialog


class KeyboardShortcutsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Keyboard Shortcuts")
        self.resize(600, 400)  # Adjust size as needed
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout(self)
        web_engine_view = QWebEngineView(self)
        current_dir = os.path.dirname(__file__)
        print(f"current dir: {current_dir}")
        shortcuts_html_path = os.path.join(current_dir, 'ace', 'ace_keys.html')
        print(f"loading: {shortcuts_html_path}")

        # ace_keys_html_path = os.path.join(current_dir, 'ace_keys.html')  # Adjust path as needed
        web_engine_view.load(QUrl.fromLocalFile(shortcuts_html_path))
        layout.addWidget(web_engine_view)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)