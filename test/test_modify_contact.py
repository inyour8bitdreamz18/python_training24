from model.contact import Contact
# Login, logout теперь хранятся в conftest

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Annuta", lastname="", address="Red street", mobile="", email="",
                               email2="", email3="", nickname="", company="", title="",
                               home="", work="QA", fax="+0", homepage="", bday="5", bmonth="April", byear="1990", aday="", amonth="", ayear=""))


def test_modify_first_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="New name", lastname="New lastname"))


def test_modify_first_contact_date(app):
    app.contact.modify_first_contact(Contact(bday="4", bmonth="May", byear="1992", aday="01", amonth="April", ayear="2004"))


def test_modify_first_contact_email(app):
    app.contact.modify_first_contact(Contact(email="new_email",email2="new_email2", email3="new_email3"))



