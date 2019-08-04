class DeleteHelper:

    def __init__(self, app):
        self.app = app

    def del_first_adr(self,app):
        wd = self.app.wd
        app.select.select_first_adr()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def delete_first_group(self,app):
        wd = self.app.wd
        app.group.open_groups_page()
        #select first group
        app.select.select_first_adr()
        #submit deletion
        wd.find_element_by_name("delete").click()
        app.group.return_to_groups_page()