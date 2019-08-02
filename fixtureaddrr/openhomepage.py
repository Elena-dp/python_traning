class OpenhomepageHelper:

    def __init__(self, app):
        self.app=app

    def open(self):
        wd = self.app.wd
        # open home page
        wd.get("http://localhost/addressbook/edit.php")

