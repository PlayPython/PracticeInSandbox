from tkinter import *
from tkinter.filedialog import LoadFileDialog
import CodeComparer as cc


class Application(Frame):
    file1 = 's.json'
    file2 = 'f.json'

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widget()

    def create_widget(self):
        str1 = StringVar()
        str2 = StringVar()

        def dialog1():
            fd = LoadFileDialog(root)
            str1.set('%s' % fd.go())

        def dialog2():
            fd = LoadFileDialog(root)
            str2.set('%s' % fd.go())

        file_1_button = Button(self, text='Get your first file', command=dialog1).pack()
        entry1 = Entry(self, textvariable=str1, width=100)
        entry1.pack()

        file_2_button = Button(self, text="Get your second file", command=dialog2).pack()
        entry2 = Entry(self, textvariable=str2, width=100)
        entry2.pack(side="top")

        self.load_file_1 = Text(self, height=100, width=100)
        self.load_file_2 = Text(self, height=100, width=100)
        self.load_file_1.pack(side="left")
        self.load_file_2.pack(side="right")

        def set_file():
            if entry1.get() != "" and entry2.get() != "":
                self.file1 = entry1.get()
                self.file2 = entry2.get()
                self.load_file_1.delete(0.0, END)
                self.load_file_2.delete(0.0, END)
                self.file1_content = open(self.file1, 'r').read()
                self.file2_content = open(self.file2, 'r').read()
                self.load_file_1.insert(END, chars=self.file1_content)
                self.load_file_2.insert(END, chars=self.file2_content)
            else:
                raise Exception("At least one file is empty.")

        start_compare = Button(self, text="Yes, I want to compare the two files.", command=set_file).pack()
        compare = Button(self, text="Compare Now.", command=self.compare_two_file)
        compare.pack(side="bottom")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

    def compare_two_file(self):
        o = cc.CodeComparer(self.file1, self.file2)
        line_index = o.compare_two_files_return_different_line_numbers_and_index()
        # 高亮显示不同的部分
        self.load_file_2.tag_config('a', foreground="red")
        for i in line_index.keys():
            self.load_file_2.tag_add('a', '{0}.{1}'.format(i, line_index.get(i)), '{0}.end'.format(i))


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
