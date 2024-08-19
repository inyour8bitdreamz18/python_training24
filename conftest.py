import pytest
from fixture.application import Application

# Функция, инициализирующая Фикстуру (обязательна метка перед самой функцией)
# @pytest.fixture(scope="session") убрали scope, чтобы избежать падения браузера

fixture = None

@pytest.fixture
def app(request):
    # Создает Фикстуру
    global fixture
    if fixture is None:
        # Через объект request дали доступ к конфигам
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture



# Разрушает Фикстуру и разлогинивается
# autouse=True - автоматически будет вызываться
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    # Возвращает Фикстуру
    return  fixture

# Cохранили конфиги для вызова тестов через консоль
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
