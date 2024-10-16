# -*- coding: utf-8 -*-
from model.group import Group



# Можно импортировать отдельные переменные, переименовывать их (например для отладки)
# from data.add_group import constant as testdata

# Login, logout теперь хранятся в conftest
# Testdata вынесено в отдельный python package data

# ids - представляем данные группы в виде текста
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata]) - убрали, так как сделали динам. связывание тестов с данными через фикстуры
def test_add_group_py(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_json(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
