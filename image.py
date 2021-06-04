#!/usr/bin/python3
#-*- coding: utf-8 -*-


import tkinter as tk


def mkCanvas(txt, n):
	mw=tk.Tk()
	if n > 0:
		canvas=tk.Canvas(mw, bg='yellowgreen')
		canvas.pack()
	elif n < 0:
		canvas=tk.Canvas(mw, bg='maroon')
		canvas.pack()

	frame = tk.Frame(canvas, width=30, height=30)
	canvas.create_window((100,70), window=frame, anchor='nw')
	button = tk.Button(frame, width = 10, height = 2, font = ("나눔고딕코딩", 20), text=txt)
	button.pack()
	canvas.create_text((180,180) , font = ("나눔고딕코딩", 20) , text=n);
	mw.mainloop()

if __name__ == '__main__':
	names=['a','b']	
	ratios=[+10, -10]
	for name, ratio in zip(names, ratios):
		mkCanvas(name, ratio)
