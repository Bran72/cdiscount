import requests
from bs4 import BeautifulSoup

def parse_price(sku: str):
    # Make sure sku is an str
    if isinstance(sku, str):
        cdiscount_url = "https://www.cdiscount.com/f-0-"
        fetch_url = cdiscount_url + sku + ".html"

        # Make sure we have a correct status code answer
        request = requests.get(fetch_url)
        if (request.status_code == 200):
            parsed_response = BeautifulSoup(request.content, 'html.parser')
            
            if(searchPrice(parsed_response) != False):
                product_price = searchPrice(parsed_response)
                return float(product_price)
            else:
                return "Unable to find a price."
        else:
            return "Unable to reach the url: "+fetch_url
    else:
        return "Warning: the passed sku insn't a valid product reference"

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