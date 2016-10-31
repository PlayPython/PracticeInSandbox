import tkinter as tk
import CodeComparer as cc


class Application(tk.Frame):
    file1 = 's.txt'
    file2 = 'f.txt'
    file1_content = ""
    file2_content = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file1_content = open(self.file1, 'r').read()
        self.file2_content = open(self.file2, 'r').read()

        self.load_file_1 = tk.Text(self)
        self.load_file_1.insert(tk.END, chars=self.file1_content)
        self.load_file_1.pack(side="left")

        self.load_file_2 = tk.Text(self)
        self.load_file_2.insert(tk.END, chars=self.file2_content)
        self.load_file_2.pack(side="right")

        self.compare = tk.Button(self, text="Compare", fg="green")
        self.compare["command"] = self.compare_two_file
        self.compare.pack(side="bottom")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

    def compare_two_file(self):
        o = cc.CodeComparer(self.file1, self.file2)
        line_contents = o.compare_two_files_return_different_line_numbers_and_conetent()
        line_index = o.compare_two_files_return_different_line_numbers_and_index()
        print(line_contents)
        # 高亮显示不同的部分没有成功，需要重写
        for i in line_contents.keys():
            print(line_contents.get(i))
            self.load_file_2.tag_add(line_contents.get(i), float(line_index.get(i)), tk.END)
            self.load_file_2.tag_config(line_contents.get(i), background="yellow")


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
