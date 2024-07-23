from model.group import Group

def test_modify_group(app):
    #Login, logout теперь хранятся в app.session
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    app.session.logout()