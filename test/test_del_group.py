

def test_delete_first_group(app):
    #Login, logout теперь хранятся в app.session
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()