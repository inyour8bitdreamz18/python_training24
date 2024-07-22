# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

# Функция, инициализирующая Фикстуру (обязательна метка перед самой функцией)
@pytest.fixture
def app(request):
    # Создает Фикстуру
    fixture = Application()
    # Разрушает Фикстуру
    request.addfinalizer(fixture.destroy)
    # Возвращает Фикстуру
    return  fixture


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
