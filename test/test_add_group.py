# -*- coding: utf-8 -*-
from model.group import Group
# Login, logout теперь хранятся в conftest

def test_add_group(app):
    app.group.create(Group(name="abcd", header="efg", footer="higk"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

