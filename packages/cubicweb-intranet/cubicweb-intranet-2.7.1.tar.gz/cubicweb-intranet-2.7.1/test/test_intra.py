"""intranet automatic tests"""

import unittest
import random

from cubicweb_web.devtools.testlib import AutomaticWebTest
from cubicweb.devtools.fill import ValueGenerator


class AutomaticWebTest(AutomaticWebTest):
    pass


def random_numbers(size):
    return "".join(random.choice("0123456789") for i in range(size))


class MyValueGenerator(ValueGenerator):
    def generate_Book_isbn10(self, entity, index):
        return random_numbers(10)

    def generate_Book_isbn13(self, entity, index):
        return random_numbers(13)


if __name__ == "__main__":
    unittest.main()
