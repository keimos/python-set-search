import unittest
from add_search_set import create_number_set, add_number_to_set, number_search

class TestNumberSet(unittest.TestCase):

    def setUp(self):
        # This method is called before each test.
        self.number_set = create_number_set()

    def test_create_number_set(self):
        # Test if this initial number set is created properly
        expected_set = {23, 90, 78, 12, 34, 67}
        self.assertEqual(self.number_set, expected_set)

if __name__ == "__main__":
    unittest.main