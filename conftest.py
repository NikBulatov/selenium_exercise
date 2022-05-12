import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language: 'en', 'es', 'ru', 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()

    if len(language) >= 2:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print("\nstart browser for test...")
    else:
        raise pytest.UsageError("--language should be like 'es', 'en', 'fr', 'ru'")
    yield browser

    print("\nquit browser..")
    browser.quit()
