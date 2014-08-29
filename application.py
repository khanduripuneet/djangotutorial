from flask import Flask
from flask import render_template, request
from math import *
from flask import url_for
app = Flask(__name__)

@app.route("/")
def hello():
    #return render_template('add.html', firstnumber = 0, secondnumber = 0, thirdnumber = 0, result = 0)
    #return render_template('table.html' , number = 0, rows = [])
     return render_template('todo.html')
     
@app.route("/hello")
def abc ():
	return "hello"

@app.route('/user/<username>/telephone/<phone>')
def show_user_profile(username,phone):
	   return render_template('info.html', name = username, number = phone)

@app.route('/add', methods = ['POST', 'GET'])
def add():
    x = float(request.form['x1'])
    y = float(request.form['y1'])
    p = float(request.form['p1'])
    z = x + y + p
    return render_template('add.html', firstnumber = x, secondnumber = y, thirdnumber = p, result = z)

@app.route('/table', methods = ['POST', 'GET'])
def table():
    x = int(request.form['t1'])
    rows = [(x, i, x * i) for i in range(1, 11)]
    return render_template('table.html', number = x, rows = rows)

@app.route('/rows')
def rows():
    x = int(request.form['t1'])
    rows = [(x, i, x * i) for i in range(1, 11)]
    return rows

@app.route('/square/<float:x>')
def square (x):
	return 'the squareroot of %s is %s' % (x, sqrt(x))

if __name__ == "__main__":
    app.run()