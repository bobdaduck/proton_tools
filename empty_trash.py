from Pages import pages


class Begin():
    _pages = pages.Pages()
    _pages.inbox.goto()

if __name__ == '__main__':
    Begin()
