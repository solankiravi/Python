from flask import Flask, render_template

app= Flask(__name__)

#app.route defines the endpoints
@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

#run app
app.run(host='0.0.0.0', port='5000', debug=True)