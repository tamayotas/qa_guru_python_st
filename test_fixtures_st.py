import pytest

@pytest.fixture
def browser():
    print ("Я выполняюсь перед тестом. Открывается браузер")

    yield "Browser"

    print ("Я выполняюсь после теста. Закрывается браузер")

@pytest.fixture
def login_page(browser):
    pass

@pytest.fixture
def credentials():
    return 'admin', "12345"

def test_login(login_page, credentials):
    assert credentials == ("admin", "12345"), "Неверный логин/пароль админа"
