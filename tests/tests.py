import unittest
import ratlib.api.names

"""
This is the Unit Test file for PipSqeak.
Test Classes should be per-module
"""


class RatlibNamesTests(unittest.TestCase):
    """
    Tests for ratlib.api.names
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_require_decorator(self):
        pass


class RatBoardTests(unittest.TestCase):
    """
    tests for the rat-board module
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass


class NamesTests(unittest.TestCase):
    """
    Tests for ratlib/api/names.py
    """
    @classmethod
    def setUpClass(cls):
        # init a mock object once for usage
        cls.bot = Bot()

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':  # this prevents script code from being executed on import. (bad!)
    unittest.main()

