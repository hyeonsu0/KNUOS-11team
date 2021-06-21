from flask import Flask, render_template, request
import mypkg

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
	if request.method == 'GET':
		index = mypkg.get_index()
		mypkg.getData()
		res = mypkg.search(index) 
		return render_template('crawl.html', data = res[0]['_source'])
#res[0]['_source'] 첫번째 항목 데이터전체
#res[0]['_source']['name'] 첫번째 항목의 종목명
#res[0]['_source']['price'] 첫번째 항목의 현재가
#res[0]['_source']['price_gap'] 첫번째 항목의 전일비
#res[0]['_source']['ratio'] 첫번째 항목의 등락률
#res[0]['_source']['individual_code'] 첫번째 항목의 종목코드

if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description="")
		parser.add_argument('--listen-port', type=str, requierd=True, help='REST service listen port')
		args = parser.parse_args()
	except Exception as e:
		print('Error: %s' % str(e))

	ipaddr = "127.0.0.1"
	listen_port = "5000"
	print ("Starting the service with ip_addr=" + ipaddr)

	app.run(debug=False, host=ipaddr, port=int(listen_port))
