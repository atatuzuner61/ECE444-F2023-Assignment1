#!/usr/local/bin/python3.7

from utils import utils

class utils_tests:
    def test_reversed():
        assert utils.reversed(123) == 321
        assert utils.reversed(123456789) == 987654321
        assert utils.reversed(10.1) == None
        assert utils.reversed("324") == None

    def test_formatter():
        assert utils.formatter(12) == ("0b1100", "0o14")
        assert utils.formatter(36) == ("0b100100", "0o44")
        assert utils.formatter(10.1) == None
        assert utils.formatter("324") == None

utils_tests.test_reversed()
utils_tests.test_formatter()