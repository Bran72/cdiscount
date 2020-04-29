# Python package: cdiscount

This is a [Python](https://www.python.org/) package to extract the price of a given [Cdiscount](https://www.cdiscount.com/) product reference.<br />
It uses 4 popular Python libraries: [Requests](https://requests.readthedocs.io/en/master/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup), [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

![Build Status](https://img.shields.io/pypi/wheel/requests.svg?logo=python)
![Docker version](https://img.shields.io/docker/v/brandonle/pydiscount?logo=docker)
![Docker size](https://img.shields.io/docker/image-size/brandonle/pydiscount?logo=docker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About
> **"Un grand pouvoir implique de grandes responsabilités"**

Yep. If you want to discover and use this project, you'll have to make a choice: how did you want to install and use it ? <br />
Let's see...

### The docker image
You can download and test the website _(yes)_ by directly pulling the docker image and running it into a container:

```
$ docker pull brandonle/pydiscount:latest
$ docker run -d -p 8080:8080 brandonle/pydiscount
```
Once your container is started, you'll be able to access the website via: [http://0.0.0.0:8080](http://0.0.0.0:8080)

### Locally

If you want to explore this package, above to use it, please make sure you have the 4 libs *(Requests, BeautifulSoup, Flask & Waitress)* installed. If not, please run:

```
$ cd cdiscount
$ pip install flask requests BeautifulSoup4 waitress
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