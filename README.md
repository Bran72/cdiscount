# Python package: cdiscount

This is a [Python](https://www.python.org/) package to extract the price of a given [Cdiscount](https://www.cdiscount.com/) product reference.<br />
It uses 2 popular Python libraries: [Requests](https://requests.readthedocs.io/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).

![Build Status](https://img.shields.io/pypi/l/requests.svg)
![Build Status](https://img.shields.io/pypi/wheel/requests.svg)


## About

Above to use this package, please make sure you have the 2 libs *(Requests & BeautifulSoup)* installed. If not, please run:

```
$ pip install requests
$ pip install beautifulsoup4
```

Next you'll be able to use the `parse_price(sku)` method to check a product price.<br />
For example:

```
>>> from cdiscount.price_parser import parse_price
>>> 
>>> sku = "del5397184246030" # your product identifier
>>> 
>>> parse_price(sku)
1776.6
```

## Testing

This project includes few tests maded with [unittest](https://docs.python.org/fr/3/library/unittest.html). If you want to run this tests, simply do the following:

```
$ cd cdiscount
$ python -m unittest
```
