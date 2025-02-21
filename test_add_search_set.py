import unitest
from add_search_set import create_number_set, add_number_to_set, number_search

class TestNumberSet(unitest.TestCase):

    def setUp(self):
        # This method is called before each test. Set up intial state.
        self.number_set = create_number_set()