from model.group import Group
from random import randrange

# Login, logout теперь хранятся в conftest

def test_modify_some_group(app, db, data_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    new_group_data = data_groups
    old_groups = db.get_group_list()
    group_index = randrange(len(old_groups))
    group = old_groups[group_index]
    app.group.modify_group_by_id(new_group_data, group.id)
    new_groups = db.get_group_list()
    # Метод .count() выступает в роли хэш-функции
    # assert len(old_groups) == len(new_groups)
    old_groups[group_index] = new_group_data
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
