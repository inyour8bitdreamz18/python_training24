# -*- coding: utf-8 -*-
from model.group import Group

# Login, logout теперь хранятся в conftest

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="abcd", header="efg", footer="higk")
    app.group.create(group)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''
def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''