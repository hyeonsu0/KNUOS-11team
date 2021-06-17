#!/usr/bin/python3
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import squarify
import pandas as pd

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
	pr = zip(names, ratios)
	squarify.plot(sizes=ratios, label=pr, color=colors, alpha=1.0)
	plt.axis('off')
	plt.show()

	if __name__ == '__main__':
		names=['a','b','c','d','e']
		ratios =[4,9,14,19,24]
		mktree(names,ratios)
