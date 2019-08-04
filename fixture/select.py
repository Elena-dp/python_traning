class SelectHelper:

    def __init__(self, app):
        self.app=app


    def select_first_adr(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        #or wd.find_element_by_xpath("//input[@id='45']").click()
        #or wd.find_element_by_id("45").click()

    def select_specgroup(self):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("select[name=\"to_group\"] > option[value=\"42\"]").click()



    def select_all(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
