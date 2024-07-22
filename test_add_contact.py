# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    # Создает Фикстуру
    fixture =Application()
    # Разрушает Фикстуру
    request.addfinalizer(fixture.destroy)
    # Возвращает Фикстуру
    return  fixture

def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Anna", lastname="Pankova", address="Red square", mobile="89123456789", email="annutahse121@gmail.com",
                        email2="annutahse122@gmail.com", email3="annutahse123@gmail.com", nickname="annutahse12", company="OOO Test", title="Testing",
                        home="+74991234567", work="QA", fax="+7", homepage="google.com", bday="3", bmonth="April", byear="1994", aday="5", amonth="June", ayear="2006"))
    app.return_to_home_page()
    app.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", lastname="", address="", mobile="", email="",
                        email2="", email3="", nickname="", company="", title="",
                        home="", work="", fax="", homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear=""))
    app.return_to_home_page()
    app.logout()
