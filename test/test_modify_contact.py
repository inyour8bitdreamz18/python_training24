from model.contact import Contact
# Login, logout теперь хранятся в conftest

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Annuta", lastname="", address="Red street", mobile="", email="",
                               email2="", email3="", nickname="", company="", title="",
                               home="", work="QA", fax="+0", homepage="", bday="5", bmonth="April", byear="1990", aday="", amonth="", ayear=""))
