from model.contact import Contact
from random import randrange
import allure

def test_modify_some_contact(app, db, data_contacts, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    new_contact_data = data_contacts
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact_index = randrange(len(old_contacts))
        contact = old_contacts[contact_index]
    with allure.step('When I modify the contact %s with new data %s' % (contact, new_contact_data)):
        app.contact.modify_contact_by_id(new_contact_data, contact.id)
    # Метод .count() выступает в роли хэш-функции
    # assert len(old_contacts) == app.contact.count()
    with allure.step('Then the new contact list is equal to the old list with the modified contact'):
        new_contacts = db.get_contact_list()
        old_contacts[contact_index] = new_contact_data
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


