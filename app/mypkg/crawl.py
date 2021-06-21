import re
import requests
import sys
import time
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

url_rise = u'https://finance.naver.com/sise/sise_rise.nhn'
index = 20210619
doc_type = "finance"
url = "127.0.0.1"
port = "9200"
es = Elasticsearch(f'{url}:{port}')

def get_clearcode(code):
    code = ''.join(list(filter(str.isdigit,code)))
    return code

def getData():
    index = time.strftime('%Y%m%d',time.localtime(time.time()))
    if not create_index(index): # index 생성
        return False
    url = url_rise
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
        res = insert(index, doc_type, data)
        print(res)
        return True

def create_index(index):
	if not es.indices.exists(index=index):
		return es.indices.create(index=index)
	return False

def insert(index, doc_type, body):
	return es.index(index=index, doc_type=doc_type, body=body)

def search(index, data=None):
	if data is None:
		data = {"match_all": {}}
	else:
		data = {"match": data}
	body = {"query": data}
	res = es.search(index=index, body=body)
	return res



