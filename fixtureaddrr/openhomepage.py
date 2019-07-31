class OpenhomepageHelper:

    def __init__(self, app):
        self.app=app

    def open(self):
            wd = self.app.wd
            # open home page
            wd.get("http://localhost/addressbook/edit.php")

    def return_to_home(self):
        wd = self.app.wd
        # retun home page
        wd.find_element_by_link_text("home").click()