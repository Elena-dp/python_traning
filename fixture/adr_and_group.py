class AdrInGroupHelper:

    def __init__(self, app):
        self.app=app

    def first_adr_fist_group(self, app):
        wd = self.app.wd
        app.select.select_first_adr()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()

    def first_adr_spec_group(self, app):
        wd = self.app.wd
        app.select.select_first_adr()
        app.select.select_specgroup()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()