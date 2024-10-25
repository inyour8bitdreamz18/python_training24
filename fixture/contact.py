#Здесь хранятся все вспомогательные методы для работы с контактами
from model.contact import Contact
import re
from urllib3 import request

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


    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contact_table()
        self.open_editing_form_by_id(id)
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def add_contact_in_group_by_id(self, id):
        wd = self.app.wd
        self.open_contact_table()
        self.select_contact_by_id(id)
        self.get_list_of_groups()


        self.contact_cache = None

    def get_list_of_groups(self):
        wd = self.app.wd
        wd.find_elements_by_css_selector("select[name=to_group]")

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_table()
        self.open_editing_form_by_index(index)
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_editing_form_by_index(self, index):
        wd = self.app.wd
        self.open_contact_table()
        wd.find_elements_by_css_selector("td.center:nth-child(8)")[index].click()

    def open_editing_form_by_id(self, id):
        wd = self.app.wd
        self.open_contact_table()
        #wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector("a[href ='edit.php?id=%s']" % id).click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_table()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_table()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to.alert.accept()
        self.contact_cache = None


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("td.center:nth-child(1)")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        #wd.find_element_by_css_selector("td.center:nth-child(1)")[index].click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_contact_table(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@name='searchstring']")) > 0):
            wd.get(self.app.base_url)


    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_table()
        wd.find_elements_by_css_selector("tr[name=entry]>td:nth-child(7)")[index].click()


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
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        # Нужно разобраться с address field в хроме ибо почему то форма закрывается сразу после внесения данных в адрес
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("company", contact.company)
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
                lastname_info = element.find_element_by_css_selector("td:not([class]):nth-child(2)").text
                firstname_info = element.find_element_by_css_selector("td:not([class]):nth-child(3)").text
                phones_info = element.find_element_by_css_selector("td:not([class]):nth-child(6)").text
                emails_info = element.find_element_by_css_selector("td:not([class]):nth-child(5)").text
                address_info = element.find_element_by_css_selector("td:not([class]):nth-child(4)").text
                self.contact_cache.append(Contact(firstname=firstname_info, lastname=lastname_info, id=id,
                                                  address=address_info,
                                                  all_phones_from_home_page=phones_info,
                                                  all_emails_from_home_page=emails_info))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_editing_form_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        #fax = wd.find_element_by_name("fax").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work =  re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        #emails = re.search("\S+@\S+", text).group(2)
        return Contact(home=home, mobile=mobile, work=work, fax=fax)