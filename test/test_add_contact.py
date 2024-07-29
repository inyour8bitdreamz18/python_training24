# -*- coding: utf-8 -*-
from model.contact import Contact
# Login, logout теперь хранятся в conftest

def test_add_contact(app):
    app.contact.create(Contact(firstname="Anna", lastname="Pankova", address="Red square", mobile="89123456789", email="annutahse121@gmail.com",
                               email2="annutahse122@gmail.com", email3="annutahse123@gmail.com", nickname="annutahse12", company="OOO Test", title="Testing",
                               home="+74991234567", work="QA", fax="+7", homepage="google.com", bday="3", bmonth="April", byear="1994", aday="5", amonth="June", ayear="2006"))

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email="",
                               email2="", email3="", nickname="", company="", title="",
                               home="", work="", fax="", homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear=""))
