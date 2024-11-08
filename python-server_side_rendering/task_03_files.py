import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)

def get_data(source):
    if source == 'json':
        with open('products.json') as f:
            return json.load(f)
    elif source == 'csv':
        with open('products.csv') as f:
            return list(csv.DictReader(f))
    return []

@app.route('/products')
def products():
    source = request.args.get('source')
    data = get_data(source)
    if not data:
        return render_template('product_display.html', error="Wrong source or empty data")
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
