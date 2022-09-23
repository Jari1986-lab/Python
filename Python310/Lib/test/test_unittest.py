import unittest.test

from sudoku_rivi import support


def load_tests(*_):
    # used by unittest
    return unittest.test.suite()


def tearDownModule():
    support.reap_children()


if __name__ == "__main__":
    unittest.main()
