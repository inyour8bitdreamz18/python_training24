# -*- coding: utf-8 -*-
from selenium import wd
import unittest
from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = wd.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd, username, password):
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        # submit
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd, contact):
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
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Anna", lastname="Pankova", address="Red square", mobile="89123456789", email="annutahse121@gmail.com",
                            email2="annutahse122@gmail.com", email3="annutahse123@gmail.com", nickname="annutahse12", company="OOO Test", title="Testing",
                            home="+74991234567", work="QA", fax="+7", homepage="google.com", bday="3", bmonth="April", byear="1994", aday="5", amonth="June", ayear="2006"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
