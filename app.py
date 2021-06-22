#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, request
import mypkg
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
import squarify
import pandas as pd

path='/usr/share/fonts/truetype/nanum/NanumGothicLight.ttf'
fontprop=fm.FontProperties(fname=path)

app = Flask(__name__)

def mktree(names, ratios, rp):
	colors=[]
	for ratio in ratios:
		if ratio > 25:
			colors.append("red")
		elif ratio > 20:
			colors.append("r")
		elif ratio > 15:
			colors.append("darkred")
		elif ratio > 10:
			colors.append("firebrick")
		elif ratio > 5:
			colors.append("indianred")
		elif ratio > 0:
			colors.append("rosybrown")
	pr=list(map(lambda x: f'{x[0]}\n{x[1]}',zip(names,  rp)))
	squarify.plot(sizes=ratios, label=pr, color=colors, text_kwargs={"fontproperties": fontprop, "fontsize": 8, "color": "white"},  bar_kwargs=dict(linewidth=3,edgecolor="#eee"))
	plt.axis('off')
	plt.savefig('static/images/treemap.png')
	
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/crawl', methods=['GET', 'POST'])
def crawl():
	if request.method == 'GET':
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
	return render_template('crawl.html',image_file='images/treemap.png')
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
	index = mypkg.get_index()
	res = mypkg.search(index)
	
	names=[]
	ratios=[]
	rp=[]
	for i in range(30):
		names.append(res[i]['_source']['name'])
		ratios.append(res[i]['_source']['ratio'])
		rp.append(res[i]['_source']['ratio'])
	for x in range(30):
		ratios[x] = float(ratios[x][1:-1])
	mktree(names, ratios, rp)
	app.run(debug=False, host=ipaddr, port=int(listen_port))
