
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

params=None
with open('config.json','r') as config_file:
    params= json.load(config_file)['params']

is_debug=True if params['debug'] == True else False

app= Flask(__name__)

if(is_debug):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_db_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_db_uri']

db = SQLAlchemy(app)



class Contacts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=False, nullable=False)
    phone_num= db.Column(db.String(80),  nullable=False)
    email=db.Column(db.String(80),  nullable=False)
    message=db.Column(db.String(80),  nullable=False)
    contacted_on=db.Column(db.String(80),  nullable=False)


class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    slug=db.Column(db.String, nullable=False)
    content=db.Column(db.String, nullable=False)
    post_date=db.Column(db.String, nullable=False)


#app.route defines the endpoints
@app.route('/')
@app.route('/index')
def index():
    posts=Posts.query.all()
    print(posts)
    for post in posts:
        print(post.title)
    return render_template('index.html', params=params,posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', params=params)

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
        return render_template('index.html', params=params)
        
    return render_template('contact.html', params=params)

@app.route('/posts')
def post():
   

    return render_template('post.html', params=params,posts=posts)


@app.route('/post/<string:post_slug>',methods=['GET'])
def get_post(post_slug):
    post= Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)
#run app
app.run(host=params['host'], port= params['port'], debug=True)