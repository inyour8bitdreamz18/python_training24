# G W T используется как пометки
from pytest_bdd import given, when, then, parsers
from model.group import Group
import random
from random import randrange


@given('a group list', target_fixture="group_list")
def group_list(db):
    return db.get_group_list()

@given(parsers.parse('a group with {name}, {header}, {footer}'), target_fixture="new_group")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list', target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="some name"))
    return db.get_group_list()

@given('a random group from the list', target_fixture="random_group")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    # Метод .count() выступает в роли хэш-функции
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#------------Modification

@given('a non-empty group list', target_fixture="non_empty_group_list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    return db.get_group_list()

@given('a random group from the list', target_fixture="random_group")
def random_group(non_empty_group_list):
    group_index = randrange(len(non_empty_group_list))
    group = non_empty_group_list[group_index]
    return group

@given(parsers.parse('a new data for the chosen group {name}, {header}, {footer}'), target_fixture="new_data")
def new_data(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when("I modify the group with new data")
def modify_group(app, new_data, random_group):
    app.group.modify_group_by_id(new_data, random_group.id)

@then('the new group list is equal to the old list with the modified group')
def verify_group_modified(db, non_empty_group_list, new_data, random_group, app, check_ui):
    old_groups = non_empty_group_list
    group_index = old_groups.index(random_group)
    new_groups = db.get_group_list()
    old_groups[group_index] = new_data
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
