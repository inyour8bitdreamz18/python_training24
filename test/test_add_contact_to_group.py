from model.contact import Contact
from model.group import Group
import random


def test_add_random_contact_to_random_group(app, db, orm, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group name"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Contact name"))
    random_group = random.choice(db.get_group_list())
    if len(orm.get_contacts_not_in_groups(random_group)) == 0:
        app.contact.create(Contact(firstname="Contact without group"))

    old_contacts_not_in_group = orm.get_contacts_not_in_groups(random_group)
    random_contact = random.choice(old_contacts_not_in_group)
    app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    old_contacts_not_in_group.remove(random_contact)
    new_contacts_not_in_group = orm.get_contacts_not_in_groups(random_group)
    assert sorted(old_contacts_not_in_group, key=Contact.id_or_max) == sorted(new_contacts_not_in_group, key=Contact.id_or_max)
    #if check_ui:
        #assert db.get_contacts_by_group_id(random_group.id) == app.contact.get_contact_list_by_group_filter(random_group.id)
