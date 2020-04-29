# Python package: cdiscount

This is a [Python](https://www.python.org/) package to extract the price of a given [Cdiscount](https://www.cdiscount.com/) product reference.<br />
It uses 3 popular Python libraries: [Requests](https://requests.readthedocs.io/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) and [waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Build Status](https://img.shields.io/pypi/wheel/requests.svg)


## About

Above to use this package, please make sure you have the 2 libs *(Requests & BeautifulSoup)* installed. If not, please run:

```
$ cd cdiscount
$ pip install requests BeautifulSoup4 waitress
```

Also, install the script with pip:

```
$ pip install dist/cdiscount-1.0.0-py3-none-any.whl   
```

## Usage

### The website
Yup. That's not because we're in Python that we don't have the right to a nice a friendly user-interface. <br />
So thanks to the next few commands, we'll run a server:

```
$ python website/website.py
```
And yeah, as mentioned in your shell, you can access the website via: [http://0.0.0.0:8080](http://0.0.0.0:8080) :-)
<br />

### The script

You're also able to use the `parse_price(sku)` method to check for a product price.<br />
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
> **Warning:** Run this in the main 'cdiscount' path

```
$ python -m unittest
```

Also, to test you can run:

```
$ python setup.py test
```