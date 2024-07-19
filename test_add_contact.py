# -*- coding: utf-8 -*-
from selenium import wd
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = wd.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd):
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("Anna")
        # fill lastname
        wd.find_element_by_name("lastname").send_keys("Pankova")
        # fill address
        wd.find_element_by_name("address").send_keys("Red square")
        # fill mobile number
        wd.find_element_by_name("mobile").send_keys("89123456789")
        # fill email 1
        wd.find_element_by_name("email").send_keys("annutahse121@gmail.com")
        # fill email 2
        wd.find_element_by_name("email2").send_keys("annutahse122@gmail.com")
        # fill email 3
        wd.find_element_by_name("email3").send_keys("annutahse123@gmail.com")
        # fill nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("annutahse12")
        # fill company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("Test")
        # fill title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("Test")
        # fill phone number
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("+74991234567")
        # fill work
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys("QA")
        # fill fax
        wd.find_element_by_name("fax").send_keys("+7")
        # fill homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys("google.com")
        # fill birth day
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys("3")
        # fill birth month
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys("April")
        # fill birth year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys("1994")
        # fill anniversary day
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys("5")
        # fill anniversary month
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys("June")
        # fill anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys("2006")
        # submit contact creation
        wd.find_element_by_xpath("//input[20]").click()
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
