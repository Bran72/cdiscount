import requests, os
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/', methods=['POST', 'GET'])
def parse_price(sku: str = ''):
    sku = request.args.get('sku')

    if sku != '' and isinstance(sku, str):
        cdiscount_url = "https://www.cdiscount.com/f-0-"
        fetch_url = cdiscount_url + sku + ".html"

        # Make sure we have a correct status code answer
        sku_request = requests.get(fetch_url)
        if (sku_request.status_code == 200):
            parsed_response = BeautifulSoup(sku_request.content, 'html.parser')
        
            if(searchPrice(parsed_response) != False):
                product_price = searchPrice(parsed_response)
                html_price = '''<h1 class='success'>
                '''+product_price+''' €</h1>'''
                return render_template('product.html', sku=html_price)
            else:
                error = '''Unable to find a price for the reference
                    '''+sku+'''.</h2>'''
                return render_template('product.html', error=error)
        else:
            error = "Unable to reach the url: "+fetch_url+".\
                The status code is "+str(sku_request.status_code)+"</h2>"
            return render_template('product.html', error=error)
    else:
        if sku is None:
            return render_template('product.html')
        else:
            error = '''Warning: the passed sku "'''+sku+'''" insn't a
            valid reference'''
            return render_template('product.html', error=error)

# Function to search a price in an HTML parsed string
def searchPrice(string: str):
    str_content = string.find("div", {"class": "fpPriceBloc"})
    if(str_content != None):
        str_price = str_content.find("span", {"class": "fpPrice"})
        if(str_price != None):
            return str_price['content']
        else:
            return False
    else:    
        return False