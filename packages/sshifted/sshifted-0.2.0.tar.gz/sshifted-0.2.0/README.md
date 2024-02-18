# SShifted Text Editor

Welcome to SShifted, a multi-tabbed text editor based on Ace and PyQt6. This application offers a rich text editing experience with multiple tabs, enabling you to work on various files simultaneously. 

## Features

- **Multi-Tab Interface**: Easily manage multiple documents in tabs.
- **Ace Editor Integration**: Enjoy a full-featured code editor, with Ace light and dark themes.
- **Cross-Platform**: Runs on any platform that supports Python and PyQt6.

## Screen Shot

<div align="center">
  <img src="https://raw.githubusercontent.com/scottpeterman/sshifted/main/screen-shots/welcome.png" alt="UglyPTY Dark" width="400px"> 
  <hr>
<img src="https://raw.githubusercontent.com/scottpeterman/sshifted/main/screen-shots/light.png" alt="UglyPTY Dark" width="400px">
</div>

## Installation

Before installing SShifted, ensure you have Python installed on your system. Then, you can install SShifted via pip:

```bash
pip install sshifted
```

## Getting Started

After installation, you can start the SShifted Text Editor from your command line. On windows you can use pythonw so you don't have to keep a cmd window open, or use it in a shortcut on your desktop, and you wont ever see a cmd window:

```bash
python -m  sshifted
pythonw -m sshifted
```

## Usage

- **Opening Files**: Use the 'File' menu to open new or existing files.
- **Saving Files**: Save your work using the 'Save' or 'Save As' options.
- **Settings**: Customize your experience through the 'Settings' menu.
- **Shortcuts**: Utilize common keyboard shortcuts like 'Ctrl+N' for a new file, 'Ctrl+S' for save etc.

## About

SShifted Text Editor is free software under the GNU General Public License v3. For more details, refer to the 'About' section in the application.

## Support

For more information about SShifted, visit our repo [https://github.com/scottpeterman/sshifted](#)

## Acknowledgments

SShifted uses the Ace editor. For more about Ace, visit [Ace official website](https://ace.c9.io/).
Learn more about PyQt and Qt at [Riverbank Computing](https://www.riverbankcomputing.com/) and [Qt Group](https://www.qt.io/), respectively.

---
#### Install build dependendancies
`pip install wheel setuptools`
#### Run Build
`python setup.py sdist bdist_wheel`
