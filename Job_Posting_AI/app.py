from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

app = Flask(__name__)

app = Flask(__name__, template_folder='/path/to/templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
