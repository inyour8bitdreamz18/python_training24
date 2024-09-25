import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle

# Функция, инициализирующая Фикстуру (обязательна метка перед самой функцией)
# @pytest.fixture(scope="session") убрали scope, чтобы избежать падения браузера

fixture = None
target = None
# Чтобы не читать config_file при каждом запуске, также как и с fixture, вынесем глобальную переменную target
@pytest.fixture
def app(request):
    # Создает Фикстуру
    global fixture
    global target
    # Через объект request дали доступ к конфигам
    browser = request.config.getoption("--browser")
    if target is None:
        # Сначала преобразуем в абсолютный путь os.path.abspath(__file__), а затем найдем директорию os.path.dirname()
        # А потом приклеим наш путь с директорией к конфиг файлу (мы вычисляем путь относительно конфиг файла)
        # Теперь тесты будут запускаться вне зависимости от рабочей директории
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    # Пароль админа нужно указывать при запуске, и он нигде не сохраняется
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture



# Разрушает Фикстуру и разлогинивается
# autouse=True - автоматически будет вызываться
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

# Cохранили конфиги для вызова тестов через консоль
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")

# Генератор тестов, где динамически подставляются параметры
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return  jsonpickle.decode(f.read())