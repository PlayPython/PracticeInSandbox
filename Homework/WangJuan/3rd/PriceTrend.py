from requests import get
from pandas import DataFrame, Series, Index
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt


class PriceTrend(object):
    @staticmethod
    def get_json_data():
        url = 'http://cd.lianjia.com/fangjia/priceTrend/gaoxin7'
        data = get(url)
        return data.json()

    @staticmethod
    def data_handler(data):
        frame = DataFrame(data)
        month = frame['currentLevel']['month']
        total = frame['currentLevel']['dealPrice']['total']
        index = Index(np.arange(12))
        val = Series(total, dtype=float, index=index)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(val)
        ax.set_xticks(index)
        ax.set_xticklabels(month)
        ax.set_title('House Trend in Gaoxin from 2015')
        plt.draw()
        # use the following to save plotting data to disk
        # plt.savefig('house_trend.png', dpi=400)
        # use the following to save plotting data to buffer
        buffer = StringIO()
        plt.savefig(buffer)
        plot_data = buffer.getvalue()
        return plot_data

    def run(self):
        data = self.get_json_data()
        plot_data = self.data_handler(data)


if __name__ == '__main__':
    e = PriceTrend()
    e.run()
