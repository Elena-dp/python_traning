class EditHelper:

    def __init__(self, app):
        self.app = app

    def edit_adr(self,addrress,app):
        wd = self.app.wd
        app.select.select_first_adr()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        app.addline.fill_adr_form(addrress)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        app.addline.return_to_home()

    def edit_group(self, group,app):
        wd = self.app.wd
        app.group.open_groups_page()
        app.select.select_first_adr()
        wd.find_element_by_name("edit").click()
        app.group.fill_group_form(group)
        wd.find_element_by_name("update").click()
        app.group.return_to_groups_page()
