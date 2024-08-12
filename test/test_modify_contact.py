from model.contact import Contact
# Login, logout теперь хранятся в conftest

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Annuta_modified", lastname="Pankova_modified", address="Red street", mobile="", email="",
                               email2="", email3="", nickname="", company="", title="",
                               home="", work="QA", fax="+0", homepage="", bday="5", bmonth="April", byear="1990", aday="", amonth="", ayear="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
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

