from flask import Flask

app= Flask(__name__)

#app.route defines the endpoints
@app.route('/')
def hello():
    return "Hello World"

#run app
app.run()