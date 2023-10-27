from Pages.inbox import Inbox
from browser import Driver


class Pages:
    def __init__(self):
        self.driver = Driver().get_instance()
        self.inbox = Inbox(self.driver)

    @property
    def inbox(self):
        return self.inbox
