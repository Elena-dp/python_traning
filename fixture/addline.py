class AddlineHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, addrress):
        wd = self.app.wd
        self.check_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_adr_form(addrress)
        wd.find_element_by_name("submit").click()
        self.return_to_home()

    def fill_adr_form(self, addrress):
        wd = self.app.wd
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

    def edit_adr(self,addrress):
        wd = self.app.wd
        self.check_home_page()
        self.select_first_adr()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_adr_form(addrress)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home()

    def select_first_adr(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        #or wd.find_element_by_xpath("//input[@id='45']").click()
        #or wd.find_element_by_id("45").click()

    def select_all(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()

    def del_first_adr(self):
        wd = self.app.wd
        self.check_home_page()
        self.select_first_adr()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        #wd.find_element_by_class_name("msgbox")
        #wd.find_element_by_link_text("Record successfull deleted")

    def delete_alladr(self):
        wd = self.app.wd
        self.check_home_page()
        self.select_all()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        #wd.find_element_by_class_name("msgbox")
        #wd.find_element_by_link_text("Record successfull deleted")

    def first_adr_fist_group(self):
        wd = self.app.wd
        self.check_home_page()
        self.select_first_adr()
        wd.find_element_by_name("add").click()
        self.return_to_home()

    def first_adr_spec_group(self, app):
        wd = self.app.wd
        self.check_home_page()
        self.select_first_adr()
        app.group.select_specgroup()
        wd.find_element_by_name("add").click()
        self.return_to_home()

    def alladr_in_specgroup(self, app):
        wd = self.app.wd
        self.check_home_page()
        self.select_all()
        app.group.select_specgroup()
        wd.find_element_by_name("add").click()
        self.return_to_home()


    def return_to_home(self):
        wd = self.app.wd
        # retun home page   просто home
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.check_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def check_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("http://localhost/addressbook/"):
            self.return_to_home()