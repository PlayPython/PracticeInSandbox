import re


class WordsFrequency(object):

    @staticmethod
    def word_frequency_method(file):
        # read file
        f = open(file, 'r')
        file_content_string = f.read()

        # split to line
        line_list = file_content_string.splitlines()
        print(line_list)

        # split to word
        words_list = []
        for line in line_list:
            line_words = line.split(' ')
            for word in line_words:
                words_list.append(word)
        print(words_list)

        # remove punctuation
        words_list_removed_punc = []
        # r = r'[!"#$%&\'()*+,-\./:;<=>?@[\\]^_`{|}~]+'
        r = r'[,\.!;:\?]'
        for word in words_list:
            word = re.sub(r, '', word)
            if(word != ''):
                words_list_removed_punc.append(word)
        print(words_list_removed_punc)

        # map word and frequency into dict
        dict = {}
        for word in words_list_removed_punc:
            dict[word] = 1
            words_list_removed_punc.remove(word)
            for word1 in words_list_removed_punc:
                if word1 in dict.keys():
                    dict[word1] += 1
                else:
                    dict[word1] = 1
                    words_list_removed_punc.remove(word1)
        print(dict)

    def run(self):
        file = 'test_file_w.txt'
        # file = '/Users/juan.wang/Documents/workspace/Python/PythonCodeCollecter/jira_ticket.py'
        self.word_frequency_method(file)


if __name__ == '__main__':
    e = WordsFrequency()
    e.run()

    # f = open(file, 'r')
    # 包含了try exception finally logic in with
    # with open() as f:
