from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app=app

    def open_groups_page(self):
        # open groups page, init group creation
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_specgroup(self):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("select[name=\"to_group\"] > option[value=\"42\"]").click()

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #open modification form
        wd.find_element_by_name("edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache=[]
            for element in wd.find_elements_by_css_selector("span.group"):
                text=element.text
                id=element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)

#до дз13
#    def delete_first_group(self):
#        wd = self.app.wd
#        self.open_groups_page()
#        self.select_first_group()
#        wd.find_element_by_name("delete").click()
#        self.return_to_groups_page()
#        self.group_cache = None

#    def select_first_group(self):
#        wd = self.app.wd
#        wd.find_element_by_name("selected[]").click()
#        #or wd.find_element_by_xpath("//input[@id='45']").click()
#        #or wd.find_element_by_id("45").click()

#    def modify_first_group(self, new_group_data):
#        wd = self.app.wd
#        self.open_groups_page()
#        self.select_first_group()
#        #open modification form
#        wd.find_element_by_name("edit").click()
#        #fill group form
#        self.fill_group_form(new_group_data)
#        #submit modification
#        wd.find_element_by_name("update").click()
#        self.return_to_groups_page()
#        self.group_cache = None