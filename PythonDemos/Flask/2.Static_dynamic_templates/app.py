from flask import Flask, render_template

app= Flask(__name__)

#app.route defines the endpoints
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#run app
app.run(host='0.0.0.0', port='5000', debug=True)