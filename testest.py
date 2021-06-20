#!/usr/bin/python3
#-*- coding: utf-8 -*-

import argparse
from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import matplotlib.pyplot as plt
import squarify
import pandas as pd

app = Flask(__name__)

def mktree(names, ratios):
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
	pr=zip(names, ratios)
	squarify.plot(sizes=ratios, label=pr, color=colors,  
			bar_kwargs=dict(linewidth=3,edgecolor="#eee"))
	plt.axis('off')
	plt.savefig('static/images/treemap.png')
	return render_template('home.html', image_file='static/images/treemap.png')

@app.route('/')
def index():
	return render_template('home.html', image_file='images/treemap.png')


if __name__=='__main__':
	app.run(debug=False, host='0.0.0.0', port=5000)
	names=["a","b","c","d","e"]	
	ratios=[+4, +9, +14, +19, +24]
	mktree(names, ratios)
