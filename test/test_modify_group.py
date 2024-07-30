from model.group import Group
# Login, logout теперь хранятся в conftest

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group2"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_for_modify"))
    app.group.modify_first_group(Group(header="New header2"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test_for_modify"))
    app.group.modify_first_group(Group(footer="New footer2"))

