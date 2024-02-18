import os
import base64
from PyQt6 import QtWidgets, QtWebEngineWidgets
from PyQt6.QtGui import QContextMenuEvent, QAction
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QUrl, QMimeData, pyqtSlot, QTimer, pyqtSignal
from PyQt6.QtWebChannel import QWebChannel

from sshifted.Library.editor_handler import Handler

class Editor(QtWebEngineWidgets.QWebEngineView):
    fileSaved = pyqtSignal(str)
    nextEditorId = 0

    def __init__(self, parent, doc_text=None):
        super().__init__(parent)
        self.channel = QWebChannel()
        self.handler = Handler(self)
        self.channel.registerObject('handler', self.handler)
        self.page().setWebChannel(self.channel)
        self.action = None
        self.doc_text = doc_text
        self.parent_window = parent
        self.new_file = False
        self.file_path = None
        self.editorId = Editor.nextEditorId
        Editor.nextEditorId += 1
        self.has_changed = False
        self.is_initial_load = True  # Add this flag

        # Load the HTML file for the editor
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # ace_html = current_dir.split("Library")[0] + "ace/editor.html"
        current_dir = os.path.dirname(__file__)
        ace_html_path = os.path.join(current_dir, '..', 'ace', 'editor.html')
        print(f"loading... {ace_html_path}")
        self.load(QUrl.fromLocalFile(ace_html_path))

        # Connect loadFinished signal to initializeEditor slot
        self.loadFinished.connect(self.initializeEditor)
        self.handler.contentChangedSignal.connect(self.onContentChanged)





    def initializeEditor(self, ok):
        if ok:
            # Enable developer tools
            settings = self.page().settings()
            #settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.WebAttribute.DeveloperExtrasEnabled, True)
            # Set up the web channel
            self.page().setWebChannel(self.channel)
            self.page().runJavaScript(f"initializeEditor({self.editorId});")

    def onContentChanged(self, editor_id):
        if self.is_initial_load:
            # Ignore changes during initial load
            self.is_initial_load = False
            return
        if editor_id == self.editorId:
            # Handle the content change for this editor
            print(f"onContentChanged: Change Detected Editor id: {editor_id}")
            self.has_changed = True

    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        # Create a custom context menu
        context_menu = QtWidgets.QMenu(self)

        # Add custom actions to the menu
        action1 = QAction("Copy", self)
        action1.triggered.connect(self.aceActionCopy)
        context_menu.addAction(action1)

        action2 = QAction("Cut", self)
        action2.triggered.connect(self.aceActionCut)
        context_menu.addAction(action2)

        action3 = QAction("Paste", self)
        action3.triggered.connect(self.aceActionPaste)
        context_menu.addAction(action3)

        action5 = QAction("Select All", self)
        action5.triggered.connect(self.aceActionSelectAll)
        context_menu.addAction(action5)

        # Show the context menu at the event's position
        context_menu.exec(self.mapToGlobal(event.pos()))

    def aceActionSelectAll(self):
        self.page().runJavaScript("editor.selectAll();")

    def aceActionCopy(self):
        self.action = "copy"
        self.page().runJavaScript("editor.getSelectedText();", self.processJavaScriptResult)

    def aceActionCut(self):
        self.action = "cut"
        self.page().runJavaScript("editor.getSelectedText();", self.processJavaScriptResult)

    def aceActionPaste(self):
        self.action = "paste"
        self.page().runJavaScript("editor.getSelectedText();", self.processJavaScriptResult)

    def saveFile(self, content):
        self.doc_text = content
        # Perform the save operation
        # You can implement your own logic here to save the content to a file or database

    def loadFile(self, file_path):
        self.file_path = file_path
        self.action = "load"
        self.parent_window.file_to_open = file_path
        self.is_initial_load = True  # Set the flag to True when starting to load a file

        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            self.doc_text = content
            QTimer.singleShot(500, self.loadContent)  # Delay for 500 ms


    def loadContent(self):
        self.page().runJavaScript(f"editor.setValue(``);")
        self.page().runJavaScript("replaceSelectionWithDecodedBase64", self.processJavaScriptResult)
        self.page().runJavaScript(f"contentChanged = false;;")
        QTimer.singleShot(100, self.resetInitialLoadFlag)  # Short delay before resetting the flag

    def resetInitialLoadFlag(self):
        self.is_initial_load = False  # Reset the flag after content has been loaded

    def requestSave(self):
        self.action = "save"
        self.page().runJavaScript("editor.getValue();", self.processJavaScriptResult)

    def requestSaveAs(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As", "", "All Files (*)")
        if fileName:
            self.file_path = fileName  # Update the file path
            self.action = "saveAs"
            self.page().runJavaScript("editor.getValue();", self.processJavaScriptResult)

    def processJavaScriptResult(self, result):
        # Handle the JavaScript result
        self.page().runJavaScript(f"console.log('{result}');")
        if self.action is not None:
            if self.action == "copy":
                print(f"copied text: {result}")
                # only did it this way due to the clipboard stuff
                self.copyPlainText(result)
                self.action = None

            if self.action == "cut":
                print(f"cut text to clipboard: {result}")
                # only did it this way due to the clipboard stuff
                self.copyPlainText(result)
                self.page().runJavaScript(f'''editor.session.replace(editor.selection.getRange(), ``);''')
                self.action = None

            elif self.action == "paste":
                print("Pasting...")
                # only did it this way due to the clipboard stuff
                self.page().runJavaScript(f'''replaceSelectionWithDecodedBase64(`{self.pastePlainTextAsBase64()}`);''')
                # self.page().runJavaScript(
                #     f'''editor.session.replace(editor.selection.getRange(), `hello from paste`);''')
                self.action = None

            elif self.action == "load":
                print("loading...")
                self.page().runJavaScript(f'''replaceSelectionWithDecodedBase64(`{self.loadPlainTextAsBase64(self.doc_text)}`);''')

            if self.action == "saveAs":
                # Directly save the file without additional prompts
                try:
                    with open(self.file_path, "w", encoding="utf-8") as f:
                        f.write(result)

                    self.new_file = False  # Update the file status
                    self.fileSaved.emit(self.file_path)
                    self.has_changed = False
                    self.parent_window.statusBar.showMessage(self.file_path)
                except Exception as e:
                    self.notify("File Error", f"Error saving file: {e}")
                self.action = None

            elif self.action == "save":
                # file_to_save = None
                # call save file dialog
                if not self.new_file:
                    file_to_save = self.parent_window.file_to_open
                    reply = QMessageBox.question(
                        self, f"Save File", f"Do you want to save {file_to_save}?",
                        QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel
                    )

                    if reply == QMessageBox.StandardButton.Save:
                        # User clicked Save, perform save operation
                        # TODO: Implement your save logic here
                        print("Save file operation")
                        content = str(result)
                        try:
                            with open(file_to_save, "w", encoding="utf-8") as f:
                                f.write(content)
                                self.fileSaved.emit(file_to_save)
                                self.has_changed = False
                                self.parent_window.statusBar.showMessage(file_to_save)
                        except Exception as e:
                            self.notify("File Error", f"Error saving file: {e}")
                    else:
                        print("Save Canceled")
                    self.action = None
                else:
                    # Never saved, ask for info
                    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save As", "", "All Files (*)")
                    print(f"Saving New Content as ... {fileName}")
                    if fileName:
                        with open(fileName, "w", encoding="utf-8") as f:
                            f.write(result)
                        self.fileSaved.emit(fileName)
                        self.file_to_open = fileName
                        self.parent_window.file_to_open = fileName


                        return

        else:
            print("self.action not set, JavaScript result:", result)

    def copyPlainText(self, text):
        # Create a mime data object and set the selected text as plain text
        mime_data = QMimeData()
        mime_data.setText(text)
        # Set the mime data as the clipboard data
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mime_data)

    def pastePlainTextAsBase64(self):
        # the is the right click event
        # Create a mime data object and set the selected text as plain text
        clipboard = QApplication.clipboard()
        text = clipboard.text()

        text = self.encode(text)
        # print(text)
        return text

    def loadPlainTextAsBase64(self, text):
        text = self.encode(text)
        # print(text)
        return text

    def encode(self, s):
        return base64.b64encode(s.encode()).decode()

    def notify(self, message, info):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(info)
        msg.setWindowTitle(message)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        retval = msg.exec()

    def changeEditorTheme(self, theme_name):
        js_code = f"changeEditorTheme('{theme_name}');"
        self.page().runJavaScript(js_code)

