from flask import Flask, render_template, request
import os
import json
import csv
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


def read_data(path, src):
    try:
        if src == 'json':
            with open(path, 'r') as file:
                return json.load(file)
        elif src == 'csv':
            products = []
            with open(path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['price'] = float(row['price'])
                    products.append(row)
            return products
    except FileNotFoundError:
        return []


@app.route('/products')
def products():
    src = request.args.get('src')
    product_id = request.args.get('id')
    if src not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    products_list = read_data(f'products.{src}', src)
    
    if product_id:
        products_list = [product for product in products_list if str(product['id']) == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
