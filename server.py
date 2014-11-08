from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/cs/<lang>')
def python_statement(lang):
	return lang + " is awesome!"

def question(number):
	if number == 1:
		return "What is the best programming language?"
	elif number == 2:
		return "What class uses Python?"
	elif number == 3:
		return "Fill in the blank: John ______"

@app.route('/quiz/<int:num>')
def game(num):
	s = question(num)
	return render_template("game.html", question=s, level=num)

@app.route('/quiz/<int:num>', methods=['POST'])
def check(num):
	ans = request.form['text'].lower()
	if num == 1:
		if ans == "python":
			return redirect('/quiz/'+str(num+1))
	if num == 2:
		if ans == "cs61a":
			return redirect('/quiz/'+str(num+1))
	if num == 3:
		if ans == "denero":
			return redirect('/quiz/'+str(num+1))
	return "Nope"		

if __name__ == '__main__':
	app.run(debug=True)