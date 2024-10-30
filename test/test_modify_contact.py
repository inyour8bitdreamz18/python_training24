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


