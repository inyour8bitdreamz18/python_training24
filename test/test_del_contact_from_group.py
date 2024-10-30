from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        default_group = Group(name="Group name")
        app.group.create(default_group)
    if len(db.get_contact_list()) == 0:
        default_contact = Contact(firstname="Contact name")
        app.contact.create(default_contact)

    random_group = random.choice(db.get_group_list())

    if len(orm.get_contacts_in_groups(random_group)) == 0:
        random_contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)

    old_contacts_in_group = orm.get_contacts_in_groups(random_group)
    random_contact_in_group = random.choice(old_contacts_in_group)
    app.contact.del_contact_from_group_by_id(random_contact_in_group.id, random_group.id)
    old_contacts_in_group.remove(random_contact_in_group)
    new_contacts_in_group = orm.get_contacts_in_groups(random_group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)


