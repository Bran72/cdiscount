# Python package: cdiscount

This is a [Python](https://www.python.org/) package to extract the price of a given [Cdiscount](https://www.cdiscount.com/) product reference.<br />
It uses 2 popular Python libraries: [Requests](https://requests.readthedocs.io/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Build Status](https://img.shields.io/pypi/wheel/requests.svg)


## About

Above to use this package, please make sure you have the 2 libs *(Requests & BeautifulSoup)* installed. If not, please run:

```
$ pip install requests
$ pip install BeautifulSoup4
```

Also, since a recent update, you're now able to install the script with pip:

```
$ cd cdiscount
$ pip install dist/cdiscount-0.0.1-py3-none-any.whl   
```

## Usage

Next you'll be able to use the `parse_price(sku)` method to check a product price.<br />
For example:

```
$ python
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

Also, to test you can run:

```
$ cd cdiscount
$ python setup.py test
```