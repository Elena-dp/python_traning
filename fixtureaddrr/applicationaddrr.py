from selenium import webdriver
from fixtureaddrr.session import SessionHelper

class Applicationaddrr:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper(self)


    def return_to_home(self):
        wd = self.wd
        # retun page home
        wd.find_element_by_link_text("home").click()

    def add_new_string(self, addrress):
        wd = self.wd
        # add new string
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(addrress.fname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(addrress.mname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(addrress.lname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(addrress.niname)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(addrress.comp)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(addrress.addrr)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(addrress.homtel)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(addrress.mail)
        # submit....
        wd.find_element_by_name("submit").click()


    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/edit.php")

    def destroy (self):
        self.wd.quit()