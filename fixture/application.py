from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.addline import AddlineHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(0.7) # ранее стояло 30, 60 - задержка на тесте "первый адр в первую группу"
        self.session=SessionHelper (self)
        self.group=GroupHelper(self)
        self.addline=AddlineHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()