import random
import unittest
import bs4
from bs4 import BeautifulSoup
from cdiscount.price_parser import parse_price, search_price


class RandomTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du package 'cdiscount'."""

    def test_result(self):
        """Test le fonctionnement de la fonction 'parse_price'."""
        sku = 'del5397184246030'
        self.assertIsInstance(parse_price(sku), float)

    def test_search_price(self):
        """Test le fonctionnement de la fonction 'search_price'."""
        string = '''<div class="fpPriceBloc jsFpPriceBloc">
        <span class="fpPrice" itemprop="price" content="1200.99">
        1200<sup>€99</sup></span></div>'''
        parsed_str = BeautifulSoup(string, 'html.parser')
        self.assertIsInstance(search_price(parsed_str), str)


if __name__ == '__main__':
    unittest.main()
