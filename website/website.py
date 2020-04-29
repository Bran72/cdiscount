import os
from flask import Flask, render_template, request
from cdiscount.price_parser import parse_price

app = Flask(__name__)

# Our first route: the main (and only) page !
@app.route('/', methods=['POST', 'GET'])
def home(sku: str = ''):
    sku = request.args.get('sku')

    if sku != '' and isinstance(sku, str):
        product_price = parse_price(sku)

        if isinstance(product_price, float):
            html_price = '''<h1 class='success'>
                '''+str(product_price)+''' €</h1>'''
            return render_template('product.html', sku=html_price)
        else:
            error = '''Unable to find a price for the reference
                    "'''+sku+'''".</h2>'''
            return render_template('product.html', error=product_price)

    else:
        if sku is None:
            return render_template('product.html')
        else:
            error = '''Warning: the passed sku "'''+sku+'''" insn't a
            valid reference'''
            return render_template('product.html', error=error)

# Let's define the server
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)