from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # The first method
    # login_page = page.go_to_login_page()  # можем пользоваться методами страницы и через него перейти на нужную
    # login_page.should_be_login_page()  # и проверять, что необходимо

    # The second method
    login_page = LoginPage(browser, browser.current_url)  # а можно самим инициализировать после перехода
    login_page.should_be_login_page()  # и уже пользоваться методами этой страницы


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# pytest -v --tb=line --language=en test_main_page.py::test_guest_should_see_login_link
