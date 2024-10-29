from model.contact import Contact
from model.group import Group
import random




def test_add_contact_in_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group name if nothing is here"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Contact name if nothing is here"))

    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    old_contacts_in_group = db.get_contacts_by_group_id(group.id)
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    new_contacts_in_group = db.get_contacts_by_group_id(group.id)
    assert old_contacts_in_group == new_contacts_in_group
    #if check_ui:
    #    assert new_contacts_in_group == app.contact.get_contact_list_by_group_filter(group.id)


    '''
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

    '''

