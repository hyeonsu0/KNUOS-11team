import re
import requests
import sys
from bs4 import BeautifulSoup

es_host = "127.0.0.1"
es_port = "9200"

class jusik:
    def setdata(self, name, price, price_gap, ratio, individual_code):
        self.name = name
        self.price = price
        self.price_gap = price_gap
        self.ratio = ratio
        self.individual_code = individual_code
    #def get_upjong(self):
        #url = u"https://finance.naver.com/item/main.nhn?code="+self.individual_code
        #upjong_code = 9999
        #return upjong_code

def get_clearcode(code):
    code = ''.join(list(filter(str.isdigit,code)))
    return code

def getData(url):
    result = ""
    res = requests.get(url)
    html = BeautifulSoup(res.content.decode('euc-kr','replace'), "html.parser")
    table = html.find("table", attrs={"class":"type_2"}).find_all("tr")
    for i in range(len(table)):
        td = table[i].select_one('td')
        if td is None:
            continue
        elif td.get_text() == '':
            continue
        tds = table[i].find_all('td')
        no = tds[0].get_text()
        individual_code = get_clearcode(tds[1].find('a')['href'])
        name = tds[1].get_text()
        price = tds[2].get_text()
        price_gap = tds[3].get_text().strip()
        ratio = tds[4].get_text().strip()
        print("No : " + no + " 종목명 : " + name + " price : " + price + " price_gap : " + price_gap + " ratio : " + ratio + " individual_code : " + individual_code)


if __name__ == '__main__':
    es_index = 'finance'
    es_type_fluct = "fluct"
    es_type_category = "category"

    jusik_list = []

    url_rise = u'https://finance.naver.com/sise/sise_rise.nhn'

    getData(url_rise)


