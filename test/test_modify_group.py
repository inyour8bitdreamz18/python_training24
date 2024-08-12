from model.group import Group
# Login, logout теперь хранятся в conftest

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="Edited name", header="Edited header", footer="Edited footer")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    # Метод .count() выступает в роли хэш-функции
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_for_modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test_for_modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

'''