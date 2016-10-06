# count the English words from a file
import requests
import json


class CountWord(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.iciba_url = "http://www.iciba.com/index.php?callback=jQuery18308505977065421555_1475485177483&a=getWordMean&c=search&list=1,2,3,4,5,8,9,10,12,13,14,15,18,21,22,24,3003,3004,3005&word={0}&_=1475485178353"

    def count_words_sum(self):
        word_counter = 0
        with open(self.file_name, encoding="utf-8", mode='r') as f:
            for line in f.readlines():
                word_counter = word_counter + len(self.check_word_spelling(line.split()))

        print("{0}Sum number of this file:{1}{2}".format(10 * '=', word_counter, 10 * '='))
        return word_counter

    def check_word_spelling(self, line):
        assert isinstance(line, list)
        return list((filter(self._call_iciba, line)))

    def _call_iciba(self, word):
        check_work_url = self.iciba_url.format(word)
        resp = requests.get(url=check_work_url)
        if resp.status_code == 200:
            if '"errmsg":"success"' in resp.text:
                return word
            else:
                print("This is the wrong Englsih word{0}".format(word))


if __name__ == '__main__':
    # o = CountWord()
    list_a = range(20)
    print(list_a)
    b = filter(lambda x: x > 5 and x < 50, range(60))

    print(list(b))
