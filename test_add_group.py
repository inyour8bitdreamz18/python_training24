# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

# Функция, инициализирующая Фикстуру (обязательна метка перед самой функцией)
@pytest.fixture()
def app(request):
    # Создает Фикстуру
    fixture =Application()
    # Разрушает Фикстуру
    request.addfinalizer(fixture.destroy)
    # Возвращает Фикстуру
    return  fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="abcd", header="efg", footer="higk"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
