from PyQt5.Qt import *
import sys
import math


# 超链接
class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str))
        return super().mousePressEvent(me)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(500, 500)
        # self.setWindowIcon(QIcon("D:\ICO\ooopic_1540562292.ico"))
        self.setup_ui()

    def setup_ui(self):
        te = MyTextEdit(self)
        self.te = te
        te.move(100, 100)
        te.resize(300, 300)
        te.setStyleSheet("background-color:cyan;")

        but = QPushButton(self)
        but.move(50, 50)
        but.setText("测试按钮")
        # self.占位文本的提示()
        self.文本内容的设置()
        # self.格式设置和合并()
        but.pressed.connect(self.but_test)
        # te.textCursor().insertTable(5,3)
        # te.insertHtml("xxx"*300+"<a name='lk' href='#itlike'>撩课</a>"+"aaa"*200)
        te.insertHtml(
            "xxx" * 300 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200
        )

        te.textChanged.connect(self.text_change)  # 文本发生改变
        te.selectionChanged.connect(self.selection_change)  # 选中的文本发生改变
        te.copyAvailable.connect(self.copy_a)  # 复制是否可用

    def copy_a(self, yes):
        print("复制是否可用", yes)

    def selection_change(self):
        print("文本选中的内容发生了改变")

    def text_change(self):
        print("文本内容发生了改变")

    def but_test(self):
        # self.te.clear()
        # self.光标插入内容()
        # self.内容和格式的获取()
        # self.字体设置()
        # self.颜色设置()
        # self.字符设置()
        # self.常用编辑操作()
        # self. 只读设置()
        # self.AB功能测试()
        self.打开超链接()

    def 打开超链接(self):
        pass

    def AB功能测试(self):
        # self.te.setTabChangesFocus(True)
        print(self.te.tabStopDistance())
        self.te.setTabStopDistance(100)

    def 只读设置(self):
        self.te.setReadOnly(True)
        self.te.insertPlainText("itlike")

    def 滚动到锚点(self):
        self.te.scrollToAnchor("lk")

    def 常用编辑操作(self):
        # self.te.copy()
        # self.te.paste()
        # self.te.selectAll()
        # self.te.setFocus()
        # QTextDocument.FindBackward
        print(
            self.te.find(
                "xx", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively
            )
        )
        self.te.setFocus()

    def 字符设置(self):
        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setFontPointSize(20)
        tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(100, 200, 150))
        self.te.setCurrentCharFormat(tcf)
        tcf2 = QTextCharFormat()
        tcf2.setFontOverline(True)
        # self.te.setCurrentCharFormat(tcf2)
        self.te.mergeCurrentCharFormat(tcf2)

    def 颜色设置(self):
        self.te.setTextBackgroundColor(QColor(200, 10, 10))
        self.te.setTextColor(QColor(10, 200, 10))

    def 字体设置(self):
        # QFontDialog.getFont()
        self.te.setFontFamily("幼圆")
        self.te.setFontWeight(QFont.Black)
        self.te.setFontItalic(True)
        self.te.setFontPointSize(30)
        self.te.setFontUnderline(True)
        # font=QFont()
        # font.setStrikeOut(True)
        # self.te.setCurrentFont(font)

    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter)

    def 光标设置(self):
        print(self.te.cursorWidth())
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False)
            self.te.setCursorWidth(1)
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(10)

    def 覆盖模式的设置(self):
        self.te.setOverwriteMode(True)
        print(self.te.overwriteMode())

    def 软换行模式(self):
        # self.te.setLineWrapMode(QTextEdit.NowWrap)
        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.te.setLineWrapColumnOrWidth(8)

    def 自动格式化(self):
        QTextEdit
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)  # 录入*号自动产生格式

    def 开始和结束编辑块(self):
        tc = self.te.textCursor()
        # tc.beginEditBlock()
        tc.insertText("123")
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        # tc.cndEditBlock()

        tc.insertText("789")
        tc.insertBlock()

    def 位置相关(self):
        tc = self.te.textCursor()  # 获取光标
        print("是否在段落的结尾", tc.atBlockEnd)
        print("是否在段落的开始", tc.atBlockStart())
        print("是否在文档的结尾", tc.atEnd())
        print("是否在文档的开始", tc.atStart())
        print("在第几列", tc.columnNumber())
        print("光标位置", tc.position())
        print("在文本块中的位置", tc.positionInBlock())

    def 文本字符的删除(self):
        tc = self.te.textCursor()
        # tc.deleteChar()#向右侧清除
        tc.deletePreviousChar()  # 向左侧清除
        self.te.setFocus()

    def 文本的其他操作(self):
        tc = self.te.textCursor()
        # print(tc.selectionStart())#获取选中起始
        # print(tc.selectionEnd())#获取选中结束
        # tc.clearSelection()#清除选中
        # self.te.setTextCursor()#设置光标
        # print(tc.hasSelection())
        tc.removeSelectedText()
        self.te.setFocus()

    def 文本选中内容的获取(self):
        tc = self.te.textCursor()
        print(tc.selectedText())
        QTextDocumentFragment
        print(tc.selection().toPlainText())
        print(tc.selectedTableCells())

    def 文本选中和清空(self):
        tc = self.te.textCursor()
        # tc.setPosition(6,QTextCursor,KeepAnchor)
        # tc.movePosition(QTextCursor.Up,QTextCursor.KeepAnchor,1)
        tc.select(QTextCursor.WordUnderCursor)
        self.te.setTextCursor(tc)

    def 格式设置和合并(self):
        # 设置上下间距
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setCharFormat(tcf)
        return None

        # 设置上下划线及字体大小
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        tc.setBlockCharFormat(tcf)
        pass

    def 内容和格式的获取(self):
        tc = self.te.textCursor()
        QTextLine
        print(tc.block().text())
        print(tc.blockNumber())
        # print(tc.currentList().count())
        pass

    def 文本内容的设置(self):
        # 设置普通文本内容
        self.te.setPlainText("<h1>ooo</h1>")
        self.te.insertPlainText("<h1>ooo</h1>")
        print(self.te.toPlainText())
        # 富文本的操作
        self.te.setHtml("<h1>ooo</h1>")
        self.te.insertHtml("<h6>社会我的顺哥</h6>")
        print(self.te.toHtml())

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入你的个人简介")

    def 光标插入内容(self):
        tc = self.te.textCursor()  # 获取焦点
        tff = QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(100, 50, 50))
        tff.setRightMargin(50)
        tc.insertFrame(tff)
        doc = self.te.document()
        root_frame = doc.rootFrame()
        root_frame.setFrameFormat()
        return None
        tc = self.te.textCursor()  # 获取光标
        tbf = QTextBlockFormat()
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontItalic(True)
        tcf.setFontPointSize(20)
        tbf.setAlignment(Qt.AlignRight)  # 对齐
        tbf.setRightMargin(100)
        tc.insertBlock(tbf, tcf)
        self.te.setFocus()  # 焦点
        return None
        # 创建或插入添加表格
        tc = self.te.textCursor()
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellSpacing(13)

        ttf.setColumnWidthConstraints(
            (
                QTextLength(QTextLength.PercentageLength, 50),
                QTextLength(QTextLength.PercentageLength, 40),
                QTextLength(QTextLength.PercentageLength, 10),
            )
        )  # 单元格长度比例

        table = tc.insertTable(5, 3, ttf)
        table.appendColumns(2)
        return None

        # 设置对齐
        tc = self.te.textCursor()
        # tl=tc.insertList(QTextListFormat.ListCircle)
        # tl=tc.insertList(QTectListFormat.ListDecimal)
        # tl=tc.createList(QTextListFormat.ListDecimal)
        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix("<<")
        tlf.setStyle(QTextListFormat.ListDecimal)
        tl = tc.createList(tlf)
        QTextList
        return None

        # 插入普通文本或者富文本
        tc = self.te.textCursor()
        tdf = QTextDocumentFragment.fromHtml("<h1>xxx</h1>")
        # tdf=QTextDocumentFragment.fromPlainText("<h1>xxx</h1>")
        tc.insertFragment(tdf)
        return None
        # 插入图片
        tc = self.te.textCursor()
        tif = QTextImageFormat()
        # tif.setName("D:\ICO\ooopic_1517621187.ico")
        tif.setWidth(100)
        tif.setHeight(100)
        # tc.insertImage("D:\ICO\mmmmm.JPG")

        return None
        # 插入接
        QTextCursor
        tcf = QTextCharFormat()
        tcf.setToolTip("撩课学院网址")
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(12)
        tc = self.te.textCursor()
        tc.insertText("itlike.com", tcf)
        tc.insertHtml("<a href='http://www.itlike.com'>撩课</a>")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Win = Window()
    Win.show()
    sys.exit(App.exec_())
