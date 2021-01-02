
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'
db = SQLAlchemy(app)



class Contacts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=False, nullable=False)
    phone_num= db.Column(db.String(80),  nullable=False)
    email=db.Column(db.String(80),  nullable=False)
    message=db.Column(db.String(80),  nullable=False)
    contacted_on=db.Column(db.String(80),  nullable=False)



#app.route defines the endpoints
@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry=Contacts(
            name=name,
            email=email,
            phone_num=phone,
            message=message,
            contacted_on=datetime.utcnow()
        )
        db.session.add(entry)
        db.session.commit()
        return render_template('index.html')
        
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

#run app
app.run(host='0.0.0.0', port='5000', debug=True)