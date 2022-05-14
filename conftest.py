import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: 'en', 'es', 'ru', 'fr'")
    parser.addoption('--browser_name', action='store', default='Edge', help="Choose browser: 'Chrome', 'Edge'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if language and browser_name:
        options = ChromeOptions() if browser_name == 'Chrome' else EdgeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Edge(options=options) if browser_name == 'Edge' else webdriver.Chrome(options=options)
        print("\nstart browser for test...")
    else:
        raise pytest.UsageError("need --language and --browser-name parameters"
                                "\nexample: --language=es --browser-name=Edge")
    yield browser

    print("\nquit browser..")
    browser.quit()
