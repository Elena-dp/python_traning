class AddlineHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, addrress):
        wd = self.app.wd
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

    def edit_adr(self,addrress,app):
        wd = self.app.wd
        app.addline.select_first_adr()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        app.addline.fill_adr_form(addrress)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        app.addline.return_to_home()

    def select_first_adr(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        #or wd.find_element_by_xpath("//input[@id='45']").click()
        #or wd.find_element_by_id("45").click()


    def select_all(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()


    def return_to_home(self):
        wd = self.app.wd
        # retun home page
        wd.find_element_by_link_text("home page").click()


