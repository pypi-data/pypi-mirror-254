from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QApplication
import base64

class Handler(QObject):
    contentChangedSignal = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.editor = parent

    @pyqtSlot()
    def requestPaste(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        # print(f"Pyqt: {text}")
        self.editor.page().runJavaScript(f'''replaceSelectionWithDecodedBase64(`{self.pastePlainTextAsBase64()}`);''')

    def pastePlainTextAsBase64(self):
        # Create a mime data object and set the selected text as plain text
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        text = self.encode(text)
        print(text)
        return text

    def encode(self, s):
        return base64.b64encode(s.encode()).decode()

    @pyqtSlot()
    def saveFromJs(self):
        # print(s)
        self.editor.requestSave()
        # saveFile
        # print(f"Not sure why this is called")

    @pyqtSlot(int)
    def contentChanged(self, editor_id):
        print(f"PyQt6: Content has changed in the editor {editor_id}.")
        self.contentChangedSignal.emit(editor_id)  # Emit the signal with editor ID


    @pyqtSlot()
    def checkContentChanged(self):
        # JavaScript call to check if content has changed
        self.editor.page().runJavaScript("hasContentChanged();", self.handleContentChanged)

    def handleContentChanged(self, changed):
        if changed:
            print("Content has changed.")
        else:
            print("No changes in content.")

    @pyqtSlot()
    def resetContentChangeFlag(self):
        # JavaScript call to reset content change flag
        self.editor.page().runJavaScript("resetContentChanged();")
