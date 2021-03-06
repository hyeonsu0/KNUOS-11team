from flask import Flask, render_template, request, url_for
import mypkg
import pandas as pd
import re

app = Flask(__name__)

def mkcsv(datas):
	temp = []
	temp0 = {'name':'name', 'parent':'parent','value':'value','price':'price','ratio':'ratio', 'ticker':'ticker'}
	temp01 = {'name':'Origin','parent':'','value':'','price':'','raito':'','ticker':''}
	temp.append(temp0)
	temp.append(temp01)
	for data in datas:
		temp2 ={'name':data['_source']['name'],
'parent':'Origin', 
'value':float(re.findall(r'\d+.\d+',data['_source']['ratio'])[0]), 'price':data['_source']['price'],
'ratio':data['_source']['ratio'],
'ticker':data['_source']['individual_code']}

		temp.append(temp2)
	dataframe = pd.DataFrame(temp)
	dataframe.to_csv("./static/asdf.csv", header=False, index=False)
#res[0]['_source'] 첫번째 항목 데이터전체
#res[0]['_source']['name'] 첫번째 항목의 종목명
#res[0]['_source']['price'] 첫번째 항목의 현재가
#res[0]['_source']['price_gap'] 첫번째 항목의 전일비
#res[0]['_source']['ratio'] 첫번째 항목의 등락률
#res[0]['_source']['individual_code'] 첫번째 항목의 종목코드	
	

@app.route('/')
def index():
	index = mypkg.get_index()
	try:
		res = mypkg.search(index)
		if len(res) <10:
			mypkg.getData()
	except:
		try:
			mypkg.delete_index(index)
			mypkg.getData()
		except:
			mypkg.getData()
	res = mypkg.search(index) 
	mkcsv(res)
	return render_template('crawl.html')
#res[0]['_source'] 첫번째 항목 데이터전체
#res[0]['_source']['name'] 첫번째 항목의 종목명
#res[0]['_source']['price'] 첫번째 항목의 현재가
#res[0]['_source']['price_gap'] 첫번째 항목의 전일비
#res[0]['_source']['ratio'] 첫번째 항목의 등락률
#res[0]['_source']['individual_code'] 첫번째 항목의 종목코드

if __name__ == '__main__':
	ipaddr = "127.0.0.1"
	listen_port = "5000"
	print ("Starting the service with ip_addr=" + ipaddr)

	app.run(debug=False, host=ipaddr, port=int(listen_port))
