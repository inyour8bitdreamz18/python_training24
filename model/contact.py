from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename = None, lastname=None, address=None, email=None, email2=None, email3=None, nickname=None, company=None, title=None,
                       home=None, mobile=None, work=None, fax=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None,
                        all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.nickname = nickname
        self.company = company
        self.title = title
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s, %s, %s, %s" % (self.id, self.lastname, self.firstname, self.all_emails_from_home_page, self.all_phones_from_home_page)

    # Сравнение по содержимому
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)  and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            # Maxsize выдает большое целое число
            return maxsize