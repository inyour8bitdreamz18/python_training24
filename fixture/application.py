from selenium import wd
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = wd.Firefox()
        self.wd.implicitly_wait(60)
        #ссылка на файл SessionHelper, чтобы не вызывать повторно драйвер
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # fill lastname
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # fill address
        wd.find_element_by_name("address").send_keys(contact.address)
        # fill mobile number
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # fill email 1
        wd.find_element_by_name("email").send_keys(contact.email)
        # fill email 2
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # fill email 3
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
        # submit contact creation
        wd.find_element_by_xpath("//input[20]").click()



    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()


