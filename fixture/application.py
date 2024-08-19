from selenium import wd
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
             self.wd = wd.Firefox()
        elif browser == "chrome":
            self.wd = wd.Chrome()
        elif browser == "ie":
            self.wd = wd.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        #self.wd.implicitly_wait(30)
        #ссылка на файл SessionHelper, GroupHelper, ContactHelper
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()



