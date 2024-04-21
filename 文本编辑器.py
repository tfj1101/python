from logging import root
from pydoc import text
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

import filepath


def new_file():
    text.delete("1.0", END)
    root.title("Untitled")


def open_file():

    filepath = askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if not filepath:

        return


text.delete("1.0", END)

with open(filepath, "r") as input_file:

    text.insert("1.0", input_file.read())

    root.title(f"{filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return


with open(filepath, "w") as output_file:

    text_content = text.get("1.0", END)

    output_file.write(text_content)

    root.title(f"{filepath}")


def find_text():

    search = search_box.get()

    text.tag_remove("match", "1.0", END)

    matches_found = 0

    if search:

        start_pos = "1.0"


while True:

    start_pos = text.search(search, start_pos, stopindex=END)

    if not start_pos:

        break

    end_pos = f"{start_pos}+{len(search)}c"

    text.tag_add("match", start_pos, end_pos)

    matches_found += 1

    start_pos = end_pos

    text.tag_config("match", foreground="red", background="yellow")


def replace_text():

    search = search_box.get()

    replace = replace_box.get()

    content = text.get("1.0", END)

    new_content = content.replace(search, replace)

    text.delete("1.0", END)

    text.insert("1.0", new_content)

    root = Tk()

    root.title("Untitled")

    root.geometry("800x600")

    menu_bar = Menu(root)

    file_menu = Menu(menu_bar, tearoff=0)

    file_menu.add_command(label="New", command=new_file)

    file_menu.add_command(label="Open", command=open_file)

    file_menu.add_command(label="Save", command=save_file)

    file_menu.add_separator()

    file_menu.add_command(label="Exit", command=root.quit)

    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)

    edit_menu.add_command(label="Find", command=find_text)

    edit_menu.add_command(label="Replace", command=replace_text)

    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    root.config(menu=menu_bar)

    text = Text(root, wrap="word", undo=True)

    text.pack(expand=True, fill=BOTH)

    scroll_bar = Scrollbar(text)

    text.configure(yscrollcommand=scroll_bar.set)

    scroll_bar.config(command=text.yview)

    scroll_bar.pack(side=RIGHT, fill=Y)

    search_box = Entry(root)

    search_box.pack(side=LEFT, padx=5, pady=5)

    replace_box = Entry(root)

    replace_box.pack(side=LEFT, padx=5, pady=5)

    search_button = Button(root, text="Find", command=find_text)

    search_button.pack(side=LEFT, padx=5, pady=5)

    replace_button = Button(root, text="Replace", command=replace_text)

    replace_button.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()
