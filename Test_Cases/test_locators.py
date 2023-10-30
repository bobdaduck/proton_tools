import unittest
from browser import Driver
from Pages.inbox import Inbox
from Pages.trash import Trash

class LocatorsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().get_instance()
        cls.trash = Trash(cls.driver)
        cls.inbox = Inbox(cls.driver)

    def test_inbox_locators(self):
        LocatorsTests.inbox.goto()

    def test_trash_locators(self):
        LocatorsTests.trash.goto()
        
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
