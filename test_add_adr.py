# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddAdr(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_adr(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Le")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("An")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Ka")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("eldp")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("DiPi")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moj")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+77777777777")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("el@dprint.ru")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
