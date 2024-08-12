# Login, logout теперь хранятся в conftest
from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname", lastname="Lastname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    # Метод .count() выступает в роли хэш-функции
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
