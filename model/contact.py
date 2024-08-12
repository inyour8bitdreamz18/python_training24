from sys import maxsize

class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, mobile=None, email=None, email2=None, email3=None, nickname=None, company=None, title=None,
                       home=None, work=None, fax=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.nickname = nickname
        self.company = company
        self.title = title
        self.home = home
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

    def __repr__(self):
        return "%s:%s, %s" % (self.id, self.lastname, self.firstname)

    # Сравнение по содержимому
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)  and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            # Maxsize выдает большое целое число
            return maxsize