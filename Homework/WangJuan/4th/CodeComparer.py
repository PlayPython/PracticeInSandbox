
class CodeComparer(object):
    def __init__(self, file_name_1, file_name_2):
        self.file_name_1 = file_name_1
        self.file_name_2 = file_name_2

    # Return different line numbers only
    def compare_two_files_return_different_line_numbers(self):
        diff_line_numbers = []
        l1, l2 = self.split_files()
        compare_interation_numbers = self.compare_interation_numbers(len(l1), len(l2))
        for i in range(compare_interation_numbers):
            if l1[i] != l2[i]:
                diff_line_numbers.append(i + 1)
        return diff_line_numbers

    # I take file_name_1 as template, and return different parts ( line numbers and different contents) in file_name_2
    def compare_two_files_return_different_line_numbers_and_conetent(self):
        diff_content = {}
        l1, l2 = self.split_files()
        compare_interation_numbers = self.compare_interation_numbers(len(l1), len(l2))
        for i in range(compare_interation_numbers):
            if l1[i] != l2[i]:
                flag = self.different_content(l1[i], l2[i])
                content = l2[i][flag:]
                diff_content[i + 1] = content
        return diff_content

    # I take file_name_1 as template, and return different parts ( line numbers and index that different begins)
    # in file_name_2
    def compare_two_files_return_different_line_numbers_and_index(self):
        diff_content = {}
        l1, l2 = self.split_files()
        compare_interation_numbers = self.compare_interation_numbers(len(l1), len(l2))
        for i in range(compare_interation_numbers):
            if l1[i] != l2[i]:
                flag = self.different_content(l1[i], l2[i])
                diff_content[i + 1] = flag
        return diff_content

    # Split the files into lines
    def split_files(self):
        with open(self.file_name_1, encoding="utf-8", mode='r') as f1:
            l1 = f1.read().splitlines()
        with open(self.file_name_2, encoding="utf-8", mode='r') as f2:
            l2 = f2.read().splitlines()
        return l1, l2

    # Return interation numbers that the comparation needs
    @staticmethod
    def compare_interation_numbers(num1, num2):
        if num1 < num2:
            return num2
        return num1

    # Return index that str2 begins different from str1
    # Need refactor later, it's better if we know the index that different ends
    @staticmethod
    def different_content(str1, str2):
        # This method is very simple, but decide don't use it cause' is not what i want.
        # return set(str1 + str2) - set(str1)
        flag = 0
        for i in range(len(str2)):
            if str2[i] != str1[i]:
                flag = i
                break
        return flag


if __name__ == '__main__':
    o = CodeComparer("s.json", "f.json")
    # line_numbers = o.compare_two_files_return_different_line_numbers()
    # print(line_numbers)
    line_contents = o.compare_two_files_return_different_line_numbers_and_conetent()
    print(line_contents)
    # line_index = o.compare_two_files_return_different_line_numbers_and_index()
    # print(line_index)
