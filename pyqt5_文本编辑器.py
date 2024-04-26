from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import os
import sys
import uuid

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288]
# IMAGE_EXTENSIONS = [".jpg", ".png", ".bmp"]
HTML_EXTENSIONS = [".htm", ".html"]


def hexuuid():
    return uuid.uuid4().hex


def splitext(p):
    return os.path.splitext(p)[1].lower()


# class TextEdit(QTextEdit):
#     def canInsertFromMimeData(self, source):
#         if source.hasImage():
#             return True
#         else:
#             return super(TextEdit, self).canInsertFromMimeData(source)
#     # 此函数用于将源指定的MIME数据对象的内容插入到当前光标位置的文本编辑中。
#     # 每当由于剪贴板粘贴操作而插入文本时，或当文本编辑从拖放操作接受数据时，都会调用该函数。
#     # 重新实现此函数以启用对其他MIME类型的拖放支持。
#     def insertFromMimeData(self, source):
#         cursor = self.textCursor()
#         document = self.document()
#
#         if source.hasUrls():
#             for u in source.urls():
#                 file_ext = splitext(str(u.toLocalFile()))
#                 if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
#                     image = QImage(u.toLocalFile())
#                     document.addResource(QTextDocument.ImageResource, u, image)
#                     cursor.insertImage(u.toLocalFile())
#                 else:
#                     break
#             else:
#                 return
#
#         elif source.hasImage():
#             image = source.imageData()
#             uuid = hexuuid()
#             document.addResource(QTextDocument.ImageResource, uuid, image)
#             cursor.insertImage(uuid)
#             return
#
#         super(TextEdit, self).insertFromMimeData(source)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.editor = QTextEdit()
        self.setWindowIcon(QIcon("D:/python_study/python课程设计/Typora/icon/img.png"))

        self.editor.setAutoFormatting(QTextEdit.AutoAll)
        self.editor.selectionChanged.connect(self.update_format)

        font = QFont("Times", 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)
        self.path = None
        layout.addWidget(self.editor)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # self.setCentralWidget(self.editor)
        # self.status = QStatusBar()
        # self.setStatusBar(self.status)

        文件工具栏 = QToolBar("文件")
        文件工具栏.setIconSize(QSize(20, 20))
        self.addToolBar(文件工具栏)
        文件菜单 = self.menuBar().addMenu("&文件")

        打开_action = QAction(
            QIcon("D:/python_study/python课程设计/Typora/icon/打开文件.png"),
            "打开文件",
            self,
        )
        打开_action.setStatusTip("从本地磁盘中读取文件..")
        打开_action.triggered.connect(self.file_open)
        文件菜单.addAction(打开_action)
        文件工具栏.addAction(打开_action)

        保存_action = QAction(
            QIcon(os.path.join("Typora/icon", "保存文件.png")), "保存", self
        )
        # print(os.path.join("Typora/icon", "保存文件.png"))
        保存_action.setStatusTip("保存到本地磁盘..")
        保存_action.triggered.connect(self.file_save)
        文件菜单.addAction(保存_action)
        文件工具栏.addAction(保存_action)

        另存为_action = QAction(
            QIcon(os.path.join("Typora/icon", "另存为.png")), "另存为",
            self
        )
        另存为_action.setStatusTip("另存为文件..")
        另存为_action.triggered.connect(self.file_saveas)
        文件菜单.addAction(另存为_action)
        文件工具栏.addAction(另存为_action)

        编辑工具栏 = QToolBar("编辑")
        编辑工具栏.setIconSize(QSize(20, 20))
        self.addToolBar(编辑工具栏)
        编辑菜单 = self.menuBar().addMenu("&编辑")

        撤回_action = QAction(
            QIcon(os.path.join("Typora/icon", "撤回.png")), "撤回", self
        )
        撤回_action.setStatusTip("撤回上一个操作..")
        撤回_action.triggered.connect(self.editor.undo)
        编辑菜单.addAction(撤回_action)

        重做_action = QAction(
            QIcon(os.path.join("Typora/icon", "重做.png")), "重做", self
        )
        重做_action.setStatusTip("重做撤回的操作..")
        重做_action.triggered.connect(self.editor.redo)
        编辑工具栏.addAction(重做_action)
        编辑菜单.addAction(重做_action)

        编辑菜单.addSeparator()

        剪切_action = QAction(
            QIcon(os.path.join("Typora/icon", "剪切.png")), "剪切", self
        )
        剪切_action.setStatusTip("剪切选定内容..")
        剪切_action.setShortcut(QKeySequence.Cut)
        剪切_action.triggered.connect(self.editor.cut)
        编辑工具栏.addAction(剪切_action)
        编辑菜单.addAction(剪切_action)

        复制_action = QAction(
            QIcon(os.path.join("Typora/icon", "复制.png")), "复制", self
        )
        复制_action.setStatusTip("复制选定内容..")
        剪切_action.setShortcut(QKeySequence.Copy)
        复制_action.triggered.connect(self.editor.copy)
        编辑工具栏.addAction(复制_action)
        编辑菜单.addAction(复制_action)

        粘贴_action = QAction(
            QIcon(os.path.join("Typora/icon", "粘贴.png")),
            "粘帖",
            self,
        )
        粘贴_action.setStatusTip("从剪贴板粘帖..")
        剪切_action.setShortcut(QKeySequence.Paste)
        粘贴_action.triggered.connect(self.editor.paste)
        编辑工具栏.addAction(粘贴_action)
        编辑菜单.addAction(粘贴_action)

        全选_action = QAction(
            QIcon(os.path.join("Typora/icon", "selection-input.png")), "全选", self
        )
        全选_action.setStatusTip("全选所有文字..")
        剪切_action.setShortcut(QKeySequence.SelectAll)
        全选_action.triggered.connect(self.editor.selectAll)
        编辑菜单.addAction(全选_action)

        编辑菜单.addSeparator()

        换行 = QAction(
            QIcon(os.path.join("Typora/icon", "arrow-continue.png")), "自动换行", self
        )
        换行.setStatusTip("当文字长度超过边框大小时自动换行..")
        换行.setCheckable(True)
        换行.setChecked(True)
        换行.triggered.connect(self.edit_toggle_wrap)
        编辑菜单.addAction(换行)

        格式工具栏 = QToolBar("格式")
        格式工具栏.setIconSize(QSize(20, 20))
        self.addToolBar(格式工具栏)
        格式菜单 = self.menuBar().addMenu("&格式")

        self.字体 = QFontComboBox()
        self.字体.currentFontChanged.connect(self.editor.setCurrentFont)
        格式工具栏.addWidget(self.字体)

        self.字体大小 = QComboBox()
        self.字体大小.addItems([str(s) for s in FONT_SIZES])
        self.字体大小.currentIndexChanged[str].connect(
            lambda s: self.editor.setFontPointSize(float(s))
        )
        格式工具栏.addWidget(self.字体大小)

        self.加粗 = QAction(
            QIcon(os.path.join("Typora/icon", "字体加粗.png")), "加粗", self
        )
        self.加粗.setStatusTip("加粗选定内容..")
        self.加粗.setShortcut(QKeySequence.Bold)
        self.加粗.setCheckable(True)
        self.加粗.toggled.connect(
            lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal)
        )
        格式工具栏.addAction(self.加粗)
        格式菜单.addAction(self.加粗)

        self.斜体 = QAction(
            QIcon(os.path.join("Typora/icon", "字体斜体.png")), "斜体", self
        )
        self.斜体.setStatusTip("将选定内容设为斜体..")
        self.斜体.setShortcut(QKeySequence.Italic)
        self.斜体.setCheckable(True)
        self.斜体.toggled.connect(self.editor.setFontItalic)
        格式工具栏.addAction(self.斜体)
        格式菜单.addAction(self.斜体)

        self.下划线 = QAction(
            QIcon(os.path.join("Typora/icon", "字体下划线.png")), "下划线", self
        )
        self.下划线.setStatusTip("将选定内容加下划线..")
        self.下划线.setShortcut(QKeySequence.Underline)
        self.下划线.setCheckable(True)
        self.下划线.toggled.connect(self.editor.setFontUnderline)
        格式工具栏.addAction(self.下划线)
        格式菜单.addAction(self.下划线)

        格式菜单.addSeparator()

        self.左对齐_action = QAction(
            QIcon(os.path.join("Typora/icon", "左对齐.png")), "靠左对齐", self
        )
        self.左对齐_action.setStatusTip("将文本靠左对齐..")
        self.左对齐_action.setCheckable(True)
        self.左对齐_action.triggered.connect(
            lambda: self.editor.setAlignment(Qt.AlignLeft)
        )
        格式工具栏.addAction(self.左对齐_action)
        格式菜单.addAction(self.左对齐_action)

        self.居中_action = QAction(
            QIcon(os.path.join("Typora/icon", "居中对齐.png")), "居中对齐", self
        )
        self.居中_action.setStatusTip("将文本居中对齐..")
        self.居中_action.setCheckable(True)
        self.居中_action.triggered.connect(
            lambda: self.editor.setAlignment(Qt.AlignCenter)
        )
        格式工具栏.addAction(self.居中_action)
        格式菜单.addAction(self.居中_action)

        self.右对齐_action = QAction(
            QIcon(os.path.join("Typora/icon", "右对齐.png")), "靠右对齐", self
        )
        self.右对齐_action.setStatusTip("将文本靠右对齐..")
        self.右对齐_action.setCheckable(True)
        self.右对齐_action.triggered.connect(
            lambda: self.editor.setAlignment(Qt.AlignRight)
        )
        格式工具栏.addAction(self.右对齐_action)
        格式菜单.addAction(self.右对齐_action)

        self.左右对齐_action = QAction(
            QIcon(os.path.join("Typora/icon", "左右对齐.png")),
            "左右对齐",
            self
        )
        self.左右对齐_action.setStatusTip("分散对齐文本..")
        self.左右对齐_action.setCheckable(True)
        self.左右对齐_action.triggered.connect(
            lambda: self.editor.setAlignment(Qt.AlignJustify)
        )
        格式工具栏.addAction(self.左右对齐_action)
        格式菜单.addAction(self.左右对齐_action)
        
        # 单选框
        对齐_group = QActionGroup(self)
        对齐_group.setExclusive(True)
        对齐_group.addAction(self.左对齐_action)
        对齐_group.addAction(self.居中_action)
        对齐_group.addAction(self.右对齐_action)
        对齐_group.addAction(self.左右对齐_action)

        格式菜单.addSeparator()

        self._format_actions = [
            self.字体,
            self.字体大小,
            self.加粗,
            self.斜体,
            self.下划线,
        ]
        self.update_format()
        self.update_title()
        self.show()

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        self.block_signals(self._format_actions, True)
        self.字体.setCurrentFont(self.editor.currentFont())
        self.字体大小.setCurrentText(str(int(self.editor.fontPointSize())))
        self.斜体.setChecked(self.editor.fontItalic())
        self.下划线.setChecked(self.editor.fontUnderline())
        self.加粗.setChecked(self.editor.fontWeight() == QFont.Bold)
        self.左对齐_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        self.居中_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        self.右对齐_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        self.左右对齐_action.setChecked(self.editor.alignment() == Qt.AlignJustify)
        self.block_signals(self._format_actions, False)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "打开文件",
            "",
            "HTML documents (*.html);Text documents (*.txt);All files (*.*)",
        )
        try:
            with open(path, "r+") as f:
                text = f.read()
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.editor.setText(text)
            self.update_title()

    def file_save(self):
        if self.path is None:
            return self.file_saveas()
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

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "保存文件",
            "",
            "HTML documents (*.html);Text documents (*.txt);All files (*.*)",
        )
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

    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle(
            "%s - 文本编辑器"
            % (os.path.basename(self.path) if self.path else "Untitled")
        )

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("文本编辑器")
    window = MainWindow()
    window.resize(1300, 750)
    app.exec_()
