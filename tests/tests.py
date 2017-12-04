# core import
import unittest
# import mocked classes
import tests.mock as mock
# import classes to be tested
import ratlib.api.names as name

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

    # @unittest.expectedFailure
    def test_require_decorator(self):
        level = name.Permissions.rat
        for level in name.Permissions:
            with self.subTest(permission=level):

                @name.require_permission(level)
                def foo(bot, trigger):
                    return 42
                i = 0
                for host in name.privlevels:
                    if i < level.value[0]:
                        self.assertNotEqual(foo(mock.Bot(), mock.Trigger(host=host)), 42)  # ensure func is not callable
                    else:
                        self.assertEqual(foo(mock.Bot(), mock.Trigger(host=host)), 42)  # ensure func is callable
                    i += 1


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

