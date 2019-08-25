from model.addrress import Addrress

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
        self.change_field_value("firstname", addrress.fname)
        self.change_field_value("middlename", addrress.mname)
        self.change_field_value("lastname", addrress.lname)
        self.change_field_value("nickname", addrress.niname)
        self.change_field_value("company", addrress.comp)
        self.change_field_value("address", addrress.addrr)
        self.change_field_value("home", addrress.homtel)
        self.change_field_value("email", addrress.mail)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_adr(self,new_adr_date):
        wd = self.app.wd
        self.check_home_page()
        self.select_first_adr()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_adr_form(new_adr_date)
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

    def get_adr_list(self):
        wd = self.app.wd
        self.check_home_page()
        adrlist=[]
        #for element in wd.find_elements_by_css_selector("tr"):
        for element in wd.find_elements_by_class_name("sortcompletecallback-applyZebra"):
            text = element.find_element_by_name("selected[]").get_attribute("title")
            id=element.find_element_by_name("selected[]").get_attribute("value")
            adrlist.append(Addrress(fnameandlname=text, id=id))
        return adrlist
