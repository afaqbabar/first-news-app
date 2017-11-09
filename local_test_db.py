import pymysql
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@167.114.232.111/EmpData'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(120), unique=True)

    def __init__(self, author_name, desc):
        self.article_name = article_name
        self.desc = desc

    def __repr__(self):
        return '<Article %r>' % self.article_name


db.create_all()     


db.session.commit() # This is needed to write the changes to database



# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return render_template('article.html') 
    except:
        return '<h1>Something is broken.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
