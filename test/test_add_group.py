# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    #Login, logout теперь хранятся в app.session
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="abcd", header="efg", footer="higk"))
    app.session.logout()

def test_add_empty_group(app):
    #Login, logout теперь хранятся в app.session
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
