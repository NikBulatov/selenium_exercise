import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_site_languages(browser):
    browser.get(link)
    # time.sleep(30)  # while sleep, should to switch language to 'francias' on the site
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[class=\'btn btn-lg btn-primary btn-add-to-basket\']')))
    # assert button.text == 'Ajouter au panier'  # assert for french language
    assert button.text == 'Añadir al carrito'
