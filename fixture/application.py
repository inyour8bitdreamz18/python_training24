from selenium import wd
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = wd.Firefox()
        self.wd.implicitly_wait(60)
        #ссылка на файл SessionHelper,GroupHelper
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")


    def destroy(self):
        self.wd.quit()


