import csv
from flask import Flask,render_template, json, request


app = Flask(__name__)

'''
def get_csv():
	csv_path = './static/la-riots-deaths.csv'
	csv_file = open(csv_path,'rb')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list
'''
@app.route("/")
def index():
	#template = 'index1.html'
	#object_list = get_csv()
	#return render_template(template, object_list=object_list)
	return render_template('index1.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signup',methods=['POST'])
def signup():
	_name = request.form['inputName']
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']

	if _name and _email and _password:
		return json.dumps({'html':'<span>All fields good !!</span>'})
	else:
		return json.dumps({'html':'<span> Enter required fields </span>'})

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
