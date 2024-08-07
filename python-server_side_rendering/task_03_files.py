from flask import Flask, render_template, request, jsonify
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

def read_data(path, source):
    try:
        if source == 'json':
            if os.path.exists(path):
                with open(path, 'r') as file:
                    data = json.load(file)
                    print(f"JSON data read: {data}")
                    return data['products'] if isinstance(data, dict) and 'products' in data else []
            else:
                print(f"File {path} not found.")
                return []
        elif source == 'csv':
            if os.path.exists(path):
                products = []
                with open(path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        row['price'] = float(row['price'])
                        products.append(row)
                print(f"CSV data read: {products}")
                return products
            else:
                print(f"File {path} not found.")
                return []
    except json.JSONDecodeError:
        print("Error decoding JSON")
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source not in ['json', 'csv']:
        return jsonify({"error": "Wrong source"}), 400
    
    products_list = read_data(f'products.{source}', source)
    
    if product_id:
        products_list = [product for product in products_list if str(product['id']) == product_id]
        if not products_list:
            return jsonify({"error": "Product not found"}), 404
    
    return jsonify(products_list)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
