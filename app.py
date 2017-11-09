from flask import Flask,render_template,request
from flask_mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='ArticleList'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route("/")
def index():
	print("Entering Index function")
	return render_template('article.html')

@app.route('/showAddArticle')
def showSignUp():
	print("Entering showAddArticle Function")
	return render_template('addArticle.html')

@app.route('/addArticle',methods=['POST'])
def addWish():
	print("Entering addArticle Function")
	_title = request.form['inputTitle']
	_description = request.form['inputDescription']
	
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.callproc('sp_addWish',(_title,_description))
	data = cursor.fetchall()
	conn.commit()
	return redirect('/showAddArticle')
	cursor.close()
	conn.close()

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
