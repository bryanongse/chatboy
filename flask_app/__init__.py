from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment') # shld create new file to be listened to and record voice
def increment(data):

    flag = 0 # if 1 means has started
    score = 0 # hit 9

    print ("Hello")
    return (1)

@app.route('/hello/<name>')
def hello(name):
    return "Hello %s" % name

app.run()