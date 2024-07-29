from model.group import Group
# Login, logout теперь хранятся в conftest

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group2"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header2"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New footer2"))

