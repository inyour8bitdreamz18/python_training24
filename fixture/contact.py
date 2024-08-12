#Здесь хранятся все вспомогательные методы для работы с контактами
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        # Ссылка на главный файл фикстуры Application
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # click to add new contact
        self.open_contact_table()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None


    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_table()
        # open first contact editing panel
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill data
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_table()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to.alert.accept()
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td").click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_contact_table(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@name='searchstring']")) > 0):
            wd.get("http://localhost/addressbook/")


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_list_value(self, list_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(list_name).click()
            wd.find_element_by_name(list_name).send_keys(text)


    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("home", contact.home)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("homepage", contact.homepage)
        self.change_list_value("bday", contact.bday)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_list_value("aday", contact.aday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)

    def count(self):
        wd = self.app.wd
        self.open_contact_table()
        return len(wd.find_elements_by_xpath("//td/input"))

    #Кэширование списка контактов
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_table()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                #td:not([class]):nth-child(2)
                lastname_info = element.find_element_by_css_selector("td:not([class]):nth-child(2)").text
                firstname_info = element.find_element_by_css_selector("td:not([class]):nth-child(3)").text
                self.contact_cache.append(Contact(firstname=firstname_info, lastname=lastname_info, id=id))
        return list(self.contact_cache)