from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/analysis', methods=['GET', 'POST'])
def info():
	error = None
	if request.method == 'POST':
		myname = request.form['name']
		return render_template('analysis.html', name=myname)
