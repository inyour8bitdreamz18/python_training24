# Login, logout теперь хранятся в conftest
from model.group import Group
import random
import allure

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    # Так как сортировка по index и по id разные, сделали по id через db
    with allure.step('When I delete the group %s from the list' % group):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_group_list()
        # Метод .count() выступает в роли хэш-функции
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
