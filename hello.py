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
	return '<!Doctype html>\
	<html>\
	<head>\
     <title>INFORMATION</title>\
     </head>\
     <body>\
     <h3>INFORMATION</h3>\
     <p>the user is %s phone is %s</p>\
     </body>\
     </html> '  % (username,phone)

@app.route('/square/<float:x>')
def square (x):
	return 'the square of %s is %s' % (x, (x * x))

if __name__ == "__main__":
    app.run()
