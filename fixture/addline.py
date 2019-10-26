from model.addrress import Addrress
import re

class AddlineHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, addrress):
        wd = self.app.wd
        self.control_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_adr_form(addrress)
        wd.find_element_by_name("submit").click()
        self.return_to_home()
        self.adrlist_cache = None

    def fill_adr_form(self, addrress):
        wd = self.app.wd
        self.change_field_value("firstname", addrress.fname)
        self.change_field_value("middlename", addrress.mname)
        self.change_field_value("lastname", addrress.lname)
        self.change_field_value("nickname", addrress.niname)
        self.change_field_value("company", addrress.comp)
        self.change_field_value("address", addrress.addrr)
        self.change_field_value("homephone", addrress.homephone)
        self.change_field_value("email", addrress.mail)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_adr(self,new_adr_date):
        self.select_adr_by_index(0)

    def edit_adr_by_index(self, index, new_adr_date):
        wd = self.app.wd
        self.control_home_page()
#        self.select_adr_by_index(index)
        #wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #wd.find_elements_by_css_selector("a")[index].click()
#        wd.find_elements_("edit.php?id=[]")[index].click()
        wd.find_elements_by_name("entry")[index].find_element_by_xpath(".//img[@alt='Edit']").click()
        self.fill_adr_form(new_adr_date)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home()
        self.adrlist_cache = None

    def open_adr_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_adr_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def select_first_adr(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_adr_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_all(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()

    def del_first_adr(self):
        self.del_adr_by_index(0)

    def del_adr_by_index(self, index):
        wd = self.app.wd
        self.control_home_page()
        self.select_adr_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        #wd.find_element_by_class_name("msgbox")
        #wd.find_element_by_link_text("Record successfull deleted")
        self.adrlist_cache = None

    def delete_alladr(self):
        wd = self.app.wd
        self.control_home_page()
        self.select_all()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        #wd.find_element_by_class_name("msgbox")
        #wd.find_element_by_link_text("Record successfull deleted")
        self.adrlist_cache = None

    def return_to_home(self):
        wd = self.app.wd
        # retun home page   просто home
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.control_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def control_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("http://localhost/addressbook/") and len(wd.find_elements_by_css_selector("strong"))>0:
            self.return_to_home()

    adrlist_cache = None

    def get_adr_list(self):
        if self.adrlist_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.adrlist_cache=[]
            #for element in wd.find_elements_by_css_selector("tr"):
            for element in wd.find_elements_by_name("entry"):
    #            text = element.find_element_by_name("selected[]").get_attribute("title")
    #            textL = element.find_element_by_css_selector("td").text
                cells = element.find_elements_by_css_selector("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id=element.find_element_by_name("selected[]").get_attribute("value")
                adr = cells[3].text
                mail = cells[4].text
                all_phones = cells[5].text
                self.adrlist_cache.append(Addrress(lname=lastname, fname=firstname, id=id, addrr = adr, mail = mail,
                                                   all_phones_from_home_page = all_phones))
        return list(self.adrlist_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_adr_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        adr = wd.find_element_by_name("address").get_attribute("textarea")
        mail1 = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Addrress(fname=firstname, lname=lastname, id=id, addrr=adr,
                        mail1=mail1, mail2=mail2, mail3=mail3,
                        homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_adr_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homephone = re.search("H: (.*)", text).group(1)
        else:
            homephone=None
        if re.search("M: (.*)", text) is not None:
            mobilephone = re.search("M: (.*)", text).group(1)
        else:
            mobilephone=None
        if re.search("W: (.*)", text) is not None:
            workphone = re.search("W: (.*)", text).group(1)
        else:
            workphone = None
        if re.search("P: (.*)", text) is not None:
            secondaryphone = re.search("P: (.*)", text).group(1)
        else:
            secondaryphone = None
        return Addrress(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)





#    def del_first_adr(self):
#        wd = self.app.wd
#        self.control_home_page()
#        self.select_first_adr()
#        wd.find_element_by_xpath("//input[@value='Delete']").click()
#        wd.switch_to_alert().accept()
#        wd.find_element_by_css_selector("div.msgbox")
#        #wd.find_element_by_class_name("msgbox")
#        #wd.find_element_by_link_text("Record successfull deleted")
#        self.adrlist_cache = None

#    def select_first_adr(self):
#        wd = self.app.wd
#        wd.find_element_by_name("selected[]").click()
#        #or wd.find_element_by_xpath("//input[@id='45']").click()
#        #or wd.find_element_by_id("45").click()

#    def edit_adr(self,new_adr_date):
#        wd = self.app.wd
#        self.control_home_page()
#        self.select_first_adr()
#        wd.find_element_by_xpath("//img[@alt='Edit']").click()
#        self.fill_adr_form(new_adr_date)
#        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
#        self.return_to_home()
#        self.adrlist_cache = None

#    def get_adr_list(self):
#        if self.adrlist_cache is None:
#            wd = self.app.wd
#            self.app.open_home_page()
#            self.adrlist_cache=[]
#            #for element in wd.find_elements_by_css_selector("tr"):
#            for element in wd.find_elements_by_name("entry"):
#    #            text = element.find_element_by_name("selected[]").get_attribute("title")
#    #            textL = element.find_element_by_css_selector("td").text
#                cells = element.find_elements_by_css_selector("td")
#                lastname = cells[1].text
#                firstname = cells[2].text
#                id=element.find_element_by_name("selected[]").get_attribute("value")
#                all_phones = cells[5].text.splitlines()
#                self.adrlist_cache.append(Addrress(lname=lastname, fname=firstname, id=id, homephone=all_phones[0],
#                                                   mobilephone=all_phones[1], workphone=all_phones[2],
#                                                   secondaryphone=all_phones[3]))

    def first_adr_fist_group(self):
        wd = self.app.wd
        self.control_home_page()
        self.select_first_adr()
        wd.find_element_by_name("add").click()
        self.return_to_home()

    def first_adr_spec_group(self, app):
        wd = self.app.wd
        self.control_home_page()
        self.select_first_adr()
        app.group.select_specgroup()
        wd.find_element_by_name("add").click()
        self.return_to_home()

    def alladr_in_specgroup(self, app):
        wd = self.app.wd
        self.control_home_page()
        self.select_all()
        app.group.select_specgroup()
        wd.find_element_by_name("add").click()
        self.return_to_home()