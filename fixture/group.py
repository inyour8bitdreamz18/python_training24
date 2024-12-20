#Здесь хранятся все вспомогательные методы для работы с группами
from model.group import Group
class GroupHelper:

    def __init__(self, app):
        # Ссылка на главный файл фикстуры Application
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_index(self,new_group_data, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        self.open_modification_form()
        # edit info
        self.fill_group_form(new_group_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def modify_group_by_id(self,new_group_data, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        self.open_modification_form()
        # edit info
        self.fill_group_form(new_group_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def modify_first_group(self):
        wd = self.app.wd
        self.modify_group_by_index(0)


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def open_modification_form(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()


    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    #Кэширование списка групп
    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


