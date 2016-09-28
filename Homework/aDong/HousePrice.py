import requests


class HousePrice(object):
    url = "http://cd.lianjia.com/fangjia/priceTrend/gaoxin7"

    def get_house_price(self, city=None, start_date=None, end_date=None):
        r = requests.session()
        header = {"Content-Type": "application/json"}
        resp = r.get(url=self.url, headers=header)
        print(resp.json())
        deal_price = resp.json()['currentLevel']['dealPrice']
        total_deal_price = deal_price['total']
        print(total_deal_price)
        return total_deal_price

    def generate_chart(self):
        pass


if __name__ == '__main__':
    HouseInstance = HousePrice()
    HouseInstance.get_house_price()
