#!/usr/bin/python3
"""
Create a Python function that generates personalized invitation files from
a template with placeholders and a list of objects.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: The rendered HTML for the home page.
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Render the about page.

    Returns:
        str: The rendered HTML for the about page.
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    Render the contact page.

    Returns:
        str: The rendered HTML for the contact page.
    """
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Render the items page.

    Returns:
        str: The rendered HTML for the items page.
    """
    with open('items.json') as f:
        data = json.load(f)

    items = data.get("items", [])

    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)