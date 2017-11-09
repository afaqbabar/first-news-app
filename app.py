from flask import Flask,render_template,request
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://centos:centos@167.114.232.111/EmpData'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

'''
@app.route("/")
def index():
	print("Entering Index function")
	return render_template('article.html')
'''


@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'



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
	app.run(debug=True)
