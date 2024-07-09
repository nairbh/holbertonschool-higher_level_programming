from flask import Flask, render_template
import os
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as file:
        _list = json.load(file).get("items", [])
    return render_template('items.html', items=_list)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
