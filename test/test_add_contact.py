# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
# Login, logout теперь хранятся в conftest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname="", lastname="", address="", email="",email2="", email3="",home="", mobile="", work="")]+[
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 10),
            email=random_string("email", 10),email2=random_string("email2", 10), email3=random_string("email3", 10),
            home=random_string("home", 15), mobile=random_string("mobile", 12), work=random_string("work", 12))
for i in range(5)
]


# ids - представляем данные группы в виде текста
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




'''contact = Contact(firstname="Anna", lastname="Pankova", address="Red square", mobile="89123456789", email="annutahse121@gmail.com",
                               email2="annutahse122@gmail.com", email3="annutahse123@gmail.com", nickname="annutahse12", company="OOO Test", title="Testing",
                               home="+74991234567", work="QA", fax="+7", homepage="google.com", bday="3", bmonth="April", byear="1994", aday="5", amonth="June", ayear="2006")

    contact = Contact(firstname="", lastname="", address="", mobile="", email="",
                               email2="", email3="", nickname="", company="", title="",
                               home="", work="", fax="", homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="")
'''
