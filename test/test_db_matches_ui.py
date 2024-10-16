from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    # Timeit будет вызываться много раз, нам достаточно 1 - посчитаем время запроса из UI
    print(timeit(lambda: app.group.get_group_list(), number=1))
    #ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    # Посчитали время на 1000 запросов из БД
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    #db_list = map(clean, db.get_group_list())
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)