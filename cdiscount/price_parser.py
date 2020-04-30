import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/<string:sku>')
def parse_price(sku: str):
    # Make sure sku is an str
    if isinstance(sku, str):
        CDISCOUNT_URL = "https://www.cdiscount.com/f-0-"
        fetch_url = CDISCOUNT_URL + sku + ".html"

        # Make sure we have a correct status code answer
        request = requests.get(fetch_url)
        if (request.status_code == 200):
            parsed_response = BeautifulSoup(request.content, 'html.parser')

            if (search_price(parsed_response) is not False):
                product_price = search_price(parsed_response)
                return float(product_price)
            else:
                return "Unable to find a price."
        else:
            return "Unable to reach the url: " + fetch_url + "\
                . The status code is " + str(request.status_code)
    else:
        return "Warning: the passed sku insn't a valid product reference"


# Function to search a price in an HTML parsed string
def search_price(string: str):
    str_content = string.find("div", {"class": "fpPriceBloc"})

    if (str_content is not None):
        str_price = str_content.find("span", {"class": "fpPrice"})

        if (str_price is not None):
            return str_price['content']
        else:
            return False
    else:
        return False
