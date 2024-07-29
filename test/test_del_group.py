# Login, logout теперь хранятся в conftest


def test_delete_first_group(app):
    app.group.delete_first_group()
