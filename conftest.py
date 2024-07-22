import pytest
from fixture.application import Application

# Функция, инициализирующая Фикстуру (обязательна метка перед самой функцией)

@pytest.fixture(scope="session")
def app(request):
    # Создает Фикстуру
    fixture = Application()
    # Разрушает Фикстуру
    request.addfinalizer(fixture.destroy)
    # Возвращает Фикстуру
    return  fixture
