# count the English words from a file
import requests
from multiprocessing.dummy import Pool as ThreadPool
from collections import Counter

class CountWord(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.iciba_url = "http://www.iciba.com/index.php?callback=jQuery18308505977065421555_1475485177483&a=getWordMean&c=search&list=1,2,3,4,5,8,9,10,12,13,14,15,18,21,22,24,3003,3004,3005&word={0}&_=1475485178353"

    def count_words_sum(self):
        print("start to count the words in file: {0}".format(self.file_name))
        with open(self.file_name, encoding="utf-8", mode='r') as f:
            iciba_url_list = list(map(lambda x: self.iciba_url.format(x), f.read().split()))
        pool = ThreadPool(10)
        result_list = pool.map(self._call_iciba, iciba_url_list)
        print(Counter(result_list))
        counter_obj = Counter(result_list)
        print("{0}Sum number of this file: {1}{2}".format(10 * '=', counter_obj.get(True), 10 * '='))
        return counter_obj.get(True)
        
    # def check_word_spelling(self, line):
    #     assert isinstance(line, list)
    #     return list((filter(self._call_iciba, line)))

    def _call_iciba(self, check_spell_url=None):
        headers = {"Content-Encoding": "gzip"}
        resp = requests.get(url=check_spell_url, headers=headers)
        if resp.status_code == 200:
            if '"baesInfo"' in resp.text:
                return True
            else:
                print("This is the wrong English word url:=={0}==".format(check_spell_url))
                return False
        else:
            raise AssertionError("Status code is not 200 from site iciba")


if __name__ == '__main__':
    o = CountWord("test2.txt")
    result = o.count_words_sum()
    print(result)
