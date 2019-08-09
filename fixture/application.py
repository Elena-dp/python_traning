from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.addline import AddlineHelper
from fixture.select import SelectHelper
from fixture.delete import DeleteHelper
from fixture.adr_and_group import AdrInGroupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper (self)
        self.group=GroupHelper(self)
        self.addline=AddlineHelper(self)
        self.select=SelectHelper(self)
        self.delete=DeleteHelper(self)
        self.adr_and_group=AdrInGroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()