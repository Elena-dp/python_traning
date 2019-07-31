from selenium import webdriver
from fixtureaddrr.session import SessionHelper
from fixtureaddrr.openhomepage import OpenhomepageHelper
from modeladdrr.addline import AddlineHelper

class Applicationaddrr:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper(self)
        self.openhomepage=OpenhomepageHelper(self)
        self.addline=AddlineHelper(self)


    def destroy (self):
        self.wd.quit()