from selenium import webdriver
from fixtureaddrr.session import SessionHelper
from model.addline import AddlineHelper

class Applicationaddrr:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper(self)
        self.addline=AddlineHelper(self)

    def open(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/edit.php")

    def destroy (self):
        self.wd.quit()