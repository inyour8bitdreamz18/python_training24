#Здесь хранятся все вспомогательные методы для работы с контактами

class ContactHelper:

    def __init__(self, app):
        # Ссылка на главный файл фикстуры Application
        self.app = app

    def fill_data(self, contact):
        wd = self.app.wd
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # fill lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # fill address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contact.address)
        # fill mobile number
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # fill email 1
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email)
        # fill email 2
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # fill email 3
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        # fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(contact.company)
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(contact.title)
        # fill phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home)
        # fill work
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact.work)
        # fill fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # fill homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # fill birth day
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys(contact.bday)
        # fill birth month
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        # fill birth year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # fill anniversary day
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys(contact.aday)
        # fill anniversary month
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        # fill anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)


    def create(self, contact):
        wd = self.app.wd
        # click to add new contact
        wd.find_element_by_link_text("add new").click()
        # init contact creation
        self.fill_data(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_home_page()


    def modify_first_contact(self, contact):
        wd = self.app.wd
        # open contact editing panel
        wd.get("http://localhost/addressbook/edit.php?id=3")
        # fill data
        self.fill_data(contact)
        # submit contact editing
        wd.find_element_by_xpath("//input[20]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to.alert.accept()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
