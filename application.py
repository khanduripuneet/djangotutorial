from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Root"

@app.route("/hello")
def abc ():
	return "hello"

@app.route('/user/<username>/telephone/<phone>')
def show_user_profile(username,phone):
	   return render_template('info.html', name = username, number = phone)

@app.route('/square/<float:x>')
def square (x):
	return 'the square of %s is %s' % (x, (x * x))

if __name__ == "__main__":
    app.run()
