class SelectHelper:

    def __init__(self, app):
        self.app=app



    def select_specgroup(self):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_css_selector("select[name=\"to_group\"] > option[value=\"42\"]").click()


