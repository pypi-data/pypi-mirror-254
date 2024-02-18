from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QFileDialog, QStyleFactory


class EditorMenu(QObject):
    newFileRequested = pyqtSignal()
    openFileRequested = pyqtSignal(str)
    saveFileRequested = pyqtSignal()
    saveFileAsRequested = pyqtSignal()
    settingsRequested = pyqtSignal()
    aboutRequested = pyqtSignal()
    uiThemeChanged = pyqtSignal(str)
    aceThemeChanged = pyqtSignal(str)

    keyboardShortcutsRequested = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupMenus(parent)

    def setupMenus(self, parent):
        menu_bar = parent.menuBar()
        file_menu = menu_bar.addMenu("&File")
        self.addMenuAction(file_menu, "&New", self.newFile)  # Call newFile method on trigger
        self.addMenuAction(file_menu, "&Open...", self.openFile)  # Call openFile method on trigger

        self.addMenuAction(file_menu, "&Save", self.saveFileRequested)
        self.addMenuAction(file_menu, "Save &As...", self.saveFileAsRequested)
        file_menu.addSeparator()
        self.addMenuAction(file_menu, "E&xit", parent.close)

        # Add Options Menu
        options_menu = menu_bar.addMenu("&Options")
        self.addMenuAction(options_menu, "&Settings", self.settings)

        themes_menu = menu_bar.addMenu("&Themes")
        # UI Themes submenu
        ui_theme_submenu = themes_menu.addMenu("UI Themes")
        for style_name in QStyleFactory.keys():
            self.addThemeMenuAction(ui_theme_submenu, style_name, self.uiThemeChanged)

        # Ace Editor Themes submenu
        ace_theme_submenu = themes_menu.addMenu("Editor Themes")
        ace_themes = self.get_themes()
        for theme in ace_themes:
            self.addThemeMenuAction(ace_theme_submenu, theme, self.aceThemeChanged)

        # Add Help Menu
        help_menu = menu_bar.addMenu("&Help")
        # Inside your EditorMenuSystem or similar class
        keyboardShortcutsAction = help_menu.addAction("Keyboard Shortcuts")
        keyboardShortcutsAction.triggered.connect(self.keyboardShortcutsRequested.emit)

        self.addMenuAction(help_menu, "&About", self.about)



    def addThemeMenuAction(self, menu, theme_name, signal):
        action = QAction(theme_name, self)
        action.triggered.connect(lambda: signal.emit(theme_name))
        menu.addAction(action)
    def addMenuAction(self, menu, title, method):
        action = QAction(title, self)
        action.triggered.connect(method)  # Connect to a method
        menu.addAction(action)

    def newFile(self):
        self.newFileRequested.emit()


    def openFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self.parent(), "Open File", "", "All Files (*)")
        if file_path:
            self.openFileRequested.emit(file_path)

    def saveFile(self):
        self.saveFileRequested.emit()

    def saveFileAs(self):
        self.saveFileAsRequested.emit()

    def settings(self):
        self.settingsRequested.emit()

    def about(self):
        self.aboutRequested.emit()

    def get_themes(self):
        ace_themes = [
            "chrome",
            "clouds",
            "crimson_editor",
            "dawn",
            "dreamweaver",
            "eclipse",
            "github",
            "iplastic",
            "solarized_light",
            "textmate",
            "tomorrow",
            "xcode",
            "ambiance",
            "chaos",
            "clouds_midnight",
            "cobalt",
            "dracula",
            "gob",
            "gruvbox",
            "idle_fingers",
            "kr_theme",
            "merbivore",
            "mono_industrial",
            "monokai",
            "pastel_on_dark",
            "solarized_dark",
            "terminal",
            "tomorrow_night",
            "tomorrow_night_blue",
            "tomorrow_night_bright",
            "tomorrow_night_eighties",
            "twilight",
            "vibrant_ink"
        ]
        return ace_themes
