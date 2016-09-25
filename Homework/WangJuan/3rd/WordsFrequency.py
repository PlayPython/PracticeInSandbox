import re

class WordFrequency(object):
    def word_frequency_method(self, file):
        f = open(file, 'r')
        file_content_string = ''
        r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        # remove punctuation
        for line in f:
            line = re.sub(r, '', line)
            file_content_string += line

        # split to word
        words_list = file_content_string.split(' ')

        dict = {}
        for word in words_list:
            dict[word] = 1
            words_list.remove(word)
            for word1 in words_list:
                if word1 in dict.keys():
                    dict[word1] += 1
                else:
                    dict[word1] = 1
                words_list.remove(word1)
        print(dict)


    def run(self):
        file = 'test_file.txt'
        self.word_frequency_method(file)


if __name__ == '__main__':
    e = WordFrequency()
    e.run()