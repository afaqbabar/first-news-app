import csv
from flask import Flask,render_template, json, request
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='ArticleList'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

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
	try:

		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
	
		if _name and _email and _password:
			conn = mysql.connect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
			data = cursor.fetchall()
			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'User created sucessfully'})
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
