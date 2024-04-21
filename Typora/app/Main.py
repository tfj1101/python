import sys
import os
import uuid

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
IMAGE_EXTENSIONS = [".jpg", ".png", ".bmp"]
HTML_EXTENSIONS = [".htm", ".html"]


def hexuuid():
    return uuid.uuid4().hex


def splitext(p):
    return os.path.splitext(p)[1].lower()



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1300, 700)
        self.setWindowTitle("Typora")
        self.setWindowIcon(QIcon("D:/python_study/python课程设计/Typora/icon/img.png"))

        self.editor = QTextEdit()
        self.editor.resize(1250,650)
        self.editor.setAutoFormatting(QTextEdit.AutoAll)

        font = QFont("Times", 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)
        self.path = None
        self.setCentralWidget(self.editor)
        fileMenu = self.menuBar().addMenu("文件")

        actionAdd = fileMenu.addAction("新建")
        actionAdd.setShortcut("ctrl+N")
        actionAdd.triggered.connect(self.add_action)

        actionOpen = fileMenu.addAction("打开文件")
        actionOpen.setShortcut("ctrl+O")
        actionOpen.triggered.connect(self.open_action)

        actionSave = fileMenu.addAction("保存")
        actionSave.setShortcut("ctrl+S")
        actionSave.triggered.connect(self.save_action)

        actionSave_r = fileMenu.addAction("另存为")
        actionSave_r.setShortcut("")
        actionSave_r.triggered.connect(self.r_save_action)

        exitAct = fileMenu.addAction("退出应用")
        exitAct.setShortcut("ctrl+Q")
        exitAct.triggered.connect(qApp.quit)

        editMenu = self.menuBar().addMenu("编辑")

        cutAction = editMenu.addAction("剪切")
        cutAction.setShortcut("ctrl+X")
        cutAction.triggered.connect(self.cut_action)
        copyAction = editMenu.addAction("复制")
        copyAction.setShortcut("ctrl+C")
        copyAction.triggered.connect(self.copy_action)
        pasteAction = editMenu.addAction("粘贴")
        pasteAction.setShortcut("ctrl+V")
        pasteAction.triggered.connect(self.paste_action)
        findAction = editMenu.addAction("查找")
        findAction.setShortcut("ctrl+F")
        findAction.triggered.connect(self.find_action)
        replaceAction = editMenu.addAction("替换")
        replaceAction.setShortcut("ctrl+H")
        replaceAction.triggered.connect(self.replace_action)
        wrapAction = editMenu.addAction("自动换行")
        wrapAction.setCheckable(True)
        wrapAction.setChecked(True)
        wrapAction.triggered.connect(self.wrap_action)
        formatMenu = self.menuBar().addMenu("格式")
        self.strongAction = formatMenu.addAction("加粗")
        self.strongAction.setShortcut("ctrl+B")
        self.strongAction.setCheckable(True)
        self.strongAction.triggered.connect(
            lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal)
        )
        self.italicsAction = formatMenu.addAction("斜体")
        self.italicsAction.setShortcut("ctrl+I")
        self.italicsAction.setCheckable(True)
        self.italicsAction.triggered.connect(self.editor.setFontItalic)

        self.underlineAction = formatMenu.addAction("下划线")
        self.underlineAction.setShortcut("ctrl+U")
        self.underlineAction.setCheckable(True)
        self.underlineAction.triggered.connect(self.editor.setFontUnderline)

        # format_toolbar = QToolBar("格式")
        # self.fonts = QFontComboBox()
        # self.fonts.currentFontChanged.connect(self.editor.setCurrentFont)
        # format_toolbar.addWidget(self.fonts)
        #
        # self.fontsize = QComboBox()
        # self.fontsize.addItems([str(s) for s in FONT_SIZES])
        # self.fontsize.currentIndexChanged[str].connect(
        #     lambda s: self.editor.setFontPointSize(float(s))
        # )
        # format_toolbar.addWidget(self.fontsize)

        # self.update_format()
        self.update_title()
        self.show()

    def add_action(self):
        print("新建文件")
        file_name = 'newfile.txt'
        if not os.path.exists(file_name):
            open(file_name,"w")
            self.update_title()

    def open_action(self):
        print("打开文件")
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "*.txt")
        try:
            with open(path, "r+") as f:
                text = f.read()
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.editor.setText(text)
            self.update_title()

    def update_title(self):
        self.setWindowTitle(
            "%s - Typora" % (os.path.basename(self.path) if self.path else "Untitled")
        )

    def dialog_critical(self, s):
        dlog = QMessageBox(self)
        dlog.setText(s)
        dlog.setIcon(QMessageBox.Critical)
        dlog.show()

    def save_action(self):
        print("保存文件")
        if self.path is None:
            return self.r_save_action()
        text = (
            self.editor.toHtml()
            if splitext(self.path) in HTML_EXTENSIONS
            else self.editor.toPlainText()
        )
        try:
            with open(self.path, "w") as f:
                f.write(text)
        except Exception as e:
            self.dialog_critical(str(e))

    def r_save_action(self):
        print("另存为")
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "*.txt")
        if not path:
            return
        text = (
            self.editor.toHtml()
            if splitext(path) in HTML_EXTENSIONS
            else self.editor.toPlainText()
        )
        try:
            with open(path, "w") as f:
                f.write(text)
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.update_title()

    def copy_action(self):
        print("复制")
        self.editor.copy()

    def paste_action(self):
        print("粘贴")
        self.editor.paste()

    def cut_action(self):
        print("剪切")
        self.editor.cut()

    def find_action(self):
        print("查找")

    def replace_action(self):
        print("替换")

    # def update_format(self):
    #     self.fonts.setCurrentFont(self.editor.currentFont())
    #     self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))

    def wrap_action(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)


    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        cutAct = cmenu.addAction("剪切")
        cutAct.triggered.connect(self.editor.cut)
        copyAct = cmenu.addAction("复制")
        copyAct.triggered.connect(self.editor.copy)
        pasteAct = cmenu.addAction("粘贴")
        pasteAct.triggered.connect(self.editor.paste)
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
