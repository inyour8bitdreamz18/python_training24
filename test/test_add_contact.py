# -*- coding: utf-8 -*-
from model.contact import Contact
import allure

'''
# ids - представляем данные группы в виде текста
#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact_py(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
'''

def test_add_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add the contact %s to the list' % contact):
        app.contact.create(contact)
    # Убрали хэширование, так как он работает медленно
    # Метод .count() выступает в роли хэш-функции
    # assert len(old_contacts) + 1 == app.contact.count()
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

