import unittest

from monty.inspect import all_subclasses, caller_name, find_top_pyfile


class LittleCatA:
    pass


class LittleCatB(LittleCatA):
    pass


class LittleCatC:
    pass


class LittleCatD(LittleCatB):
    pass


class InspectTest(unittest.TestCase):
    def test_func(self):
        # Not a real test. Need something better.
        assert find_top_pyfile()
        assert caller_name()

    def test_all_subclasses(self):
        assert all_subclasses(LittleCatA) == [LittleCatB, LittleCatD]


if __name__ == "__main__":
    unittest.main()
