#!/usr/bin/python3
"""
Create a Python function that generates personalized invitation files from
a template with placeholders and a list of objects.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    """
    Returns:
        str: The rendered HTML for the home page.
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Returns:
        str: The rendered HTML for the about page.
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    Returns:
        str: The rendered HTML for the contact page.
    """
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Returns:
        str: The rendered HTML for the items page.
    """
    with open('items.json') as f:
        data = json.load(f)

    items = data.get("items", [])

    return render_template('items.html', items=items)


@app.route('/products/')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        with open('products.json') as f:
            data = json.load(f)
            # Assumes that the data is directly in the JSON root
            items = data
    elif source == "csv":
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # Read all the products in a list
            items = [row for row in reader]
    elif source == "sql":
        conn = sqlite3.connect('products.db')
        # Retrieve lines in the form of dictionaries
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        items = cursor.fetchall()
        conn.close()
    else:
        return render_template('product_display.html',
                                error_message="Wrong source")

    # Filter by ID if supplied
    if product_id:
        filtered_items = [item for item in items if str(
            item['id']) == product_id]
        if not filtered_items:
            return render_template('product_display.html',
                                error_message="Product not found")
        items = filtered_items

    return render_template('product_display.html', items=items)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)