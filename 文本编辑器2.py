import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.simpledialog
from tkinter import *
from tkinter.filedialog import *
import tkinter.font as tf

# 创建应用程序窗口
app = tkinter.Tk()
app.title("whohowlong牌文本编辑器")
app["width"] = 1000
app["height"] = 800
textChanged = tkinter.IntVar(value=0)
fontStyle = tf.Font(family="Lucida Grande", size=20)

# 当前文件名
filename = ""
# 创建菜单
menu = tkinter.Menu(app)
# File 子菜单
submenu = tkinter.Menu(menu, tearoff=0)


def Open():
    global filename
    # 如果内容以改变，先保存
    if textChanged.get():
        yesno = tkinter.messagebox.askyesno(title="保存是否", message="你想保存吗？")
        if yesno == tkinter.YES:
            Save()
    filename = tkinter.filedialog.askopenfilename(
        title="打开文件", filetypes=[("Text files", "*.txt")]
    )
    if filename:
        # 清空内容，位置0.0是lineNumber.Column的表示方法，表示行好和列号
        txtContent.delete(0.0, tkinter.END)
        fp = open(filename, "r")
        txtContent.insert(tkinter.INSERT, "".join(fp.readlines()))
        fp.close()
        # 标记为尚未修改
        textChanged.set(0)
    # 创建Open菜单并绑定菜单事件处理函数


submenu.add_command(label="打开", command=Open)


def Save():
    global filename
    # 如果是第一次保存新建文件，则打开“另存为”窗口
    if not filename:
        SaveAs()
    # 如果内容发生改变，保存，可使用with关键字改写文件操作的代码
    elif textChanged.get():
        fp = open(filename, "w")
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        textChanged.set(0)


submenu.add_command(label="保存", command=Save)


def SaveAs():
    global filename
    # 打开“另存为”窗口
    newfilename = tkinter.filedialog.asksaveasfilename(
        title="另存为", initialdir=r"c:\\", initialfile="new.txt"
    )
    # 如果指定了文件名，则保存文件，可使用with改写
    if newfilename:
        fp = open(newfilename, "w")
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        filename = newfilename
        textChanged.set(0)


submenu.add_command(label="另存为", command=SaveAs)
submenu.add_separator()


def Close():
    global filename
    Save()
    txtContent.delete(0.0, tkinter.END)
    # 置空文件名
    filename = ""


submenu.add_command(label="关闭", command=Close)
# 将子菜单关联到主菜单上
menu.add_cascade(label="文件", menu=submenu)
# Edit子菜单
submenu = tkinter.Menu(menu, tearoff=0)


# 撤销最后一次操作
def Undo():
    txtContent["undo"] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass


submenu.add_command(label="撤销", command=Undo)


def Redo():
    txtContent["undo"] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass


submenu.add_command(label="恢复", command=Redo)
submenu.add_separator()


def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())


submenu.add_command(label="复制", command=Copy)


def Cut():
    Copy()
    # 删除所选内容
    txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)


submenu.add_command(label="剪切", command=Cut)


def Paste():
    # 如果没有选中内容，则直接粘贴到鼠标位置
    # 如果有所选内容，则先删除再粘贴
    try:
        txtContent.insert(tkinter.SEL_FIRST, txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        # 如果粘贴成功就结束本函数，以免异常处理结构执行完成之后再次粘贴
        return
    except Exception as e:
        pass
    txtContent.insert(tkinter.INSERT, txtContent, clipboard_get())


submenu.add_command(label="粘贴", command=Paste)
submenu.add_separator()


def Search():
    # 获取要查找的内容
    textToSearch = tkinter.simpledialog.askstring(
        title="查找", prompt="您想查找什么呢？"
    )
    start = txtContent.search(textToSearch, 0.0, tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title="寻找", message="Ok")


submenu.add_command(label="查找", command=Search)
menu.add_cascade(label="编辑", menu=submenu)


# Help子菜单
submenu = tkinter.Menu(menu, tearoff=0)

# 字号功能
menu.add_cascade(label="字号功能", menu=submenu)
labelExample = Label(submenu, text="20", font=fontStyle)
labelExample.pack(side=TOP)


def increase():  # 增大字体
    fontsize = fontStyle["size"]
    labelExample["text"] = fontsize + 2
    fontStyle.configure(size=fontsize + 2)


submenu.add_command(label="增大字号", command=increase)


def decrease():  # 减小字体
    fontsize = fontStyle["size"]
    labelExample["text"] = fontsize - 2
    fontStyle.configure(size=fontsize - 2)


submenu.add_command(label="减小字号", command=decrease)


def setfont():  # 设置字号
    t = Toplevel(app)
    t.title("字体")
    t.geometry("260x60+200+250")
    t.transient(app)

    def fontset():  # 自定义字号
        fontsize = int(e.get())
        labelExample["text"] = fontsize
        fontStyle.configure(size=fontsize)

    Label(t, text="请输入字号：").grid(row=0, column=0, sticky="e")
    e = Entry(t, width=5)
    e.insert(0, str(fontStyle["size"]))
    e.grid(row=0, column=1, sticky="e")
    e.focus_set()
    b = Button(t, text="确定", command=fontset)
    b.grid(row=0, column=2, sticky="e")

    def close():  # 关闭窗口
        t.destroy()

    t.protocol("关闭", close)


submenu.add_command(label="设置字号", command=setfont)


# Help子菜单
submenu = tkinter.Menu(menu, tearoff=0)


def About():
    tkinter.messagebox.showinfo(title="关于", message="Author:Who howlong")


submenu.add_command(label="关于", command=About)
menu.add_cascade(label="帮助", menu=submenu)
# 将创建的菜单关联到应用程序窗口
app.config(menu=menu)

# 创建文本编辑组件，并自动适应窗口大小
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)


def KeyPress(event):
    textChanged.set(1)


txtContent.bind("<KeyPress>", KeyPress)
txtContent = Text(app, font=fontStyle, undo=True)  # 文本框
txtContent.pack(expand=YES, fill=BOTH)
app.mainloop()
