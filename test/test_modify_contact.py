from model.contact import Contact
from random import randrange
# Login, logout теперь хранятся в conftest

def test_modify_some_contact(app, db, data_contacts, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    new_contact_data = data_contacts
    old_contacts = db.get_contact_list()
    contact_index = randrange(len(old_contacts))
    contact = old_contacts[contact_index]
    app.contact.modify_contact_by_id(new_contact_data, contact.id)
    # Метод .count() выступает в роли хэш-функции
    # assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[contact_index] = new_contact_data
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


'''
def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(firstname="New name", lastname="New lastname"))


def test_modify_first_contact_date(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(bday="4", bmonth="May", byear="1992", aday="01", amonth="April", ayear="2004"))


def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    app.contact.modify_first_contact(Contact(email="new_email",email2="new_email2", email3="new_email3"))

'''

