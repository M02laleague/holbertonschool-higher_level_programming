import sqlite3

def get_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in data]

@app.route('/products')
def products():
    source = request.args.get('source')
    if source == 'sql':
        products = get_sql_data()
    else:
        products = get_data(source)
    if not products:
        return render_template('product_display.html', error="Wrong source or no products found")
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
