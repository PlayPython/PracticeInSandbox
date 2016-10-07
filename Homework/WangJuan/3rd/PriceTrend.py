from time import sleep
from requests import get
from pandas import DataFrame, Series, Index
import numpy as np
import matplotlib.pyplot as plt
import json


class PriceTrend(object):
    @staticmethod
    def get_json_data():
        url = 'http://cd.lianjia.com/fangjia/priceTrend/gaoxin7'
        data = get(url)
        return data.text

    @staticmethod
    def data_handler(data):
        json_obj = json.loads(data)
        frame = DataFrame(json_obj)
        month = frame['currentLevel']['month']
        # month1 = ('九月', '十月', '十一月', '十二月', '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月')
        total = frame['currentLevel']['dealPrice']['total']
        index = Index(np.arange(12))
        val = Series(total, dtype=float, index=index)
        # plt.xticks(0, month1)
        plt.plot(val)
        plt.draw()
        sleep(2)

    def run(self):
        data = self.get_json_data()
        self.data_handler(data)


if __name__ == '__main__':
    e = PriceTrend()
    e.run()
