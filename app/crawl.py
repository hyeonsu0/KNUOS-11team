import re
import requests
import sys
import my_pkg
from bs4 import BeautifulSoup

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
        data = {
                'no' : no,
                'name' : name,
                'price' : price,
                'price_gap' : price_gap,
                'ratio' : ratio,
                'individual_code' : individual_code}
        res = my_pkg.insert(index, doc_type, data)
        print(res)


if __name__ == '__main__':
	url_rise = u'https://finance.naver.com/sise/sise_rise.nhn'
	index = "20210618"
	doc_type = "finance"
#	my_pkg.create_index(index) # index 생성
#	getData(url_rise) # 해당일의 index가 없을경우 Crawl
	print(my_pkg.search('finance')) #index를 파라미터로 데이터가져오기


