import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_site_languages(browser):
    browser.get(link)
    # time.sleep(30)
    try:
        # button = WebDriverWait(browser, 5).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[class=\'btn btn-lg btn-primary btn-add-to-basket\']')))
        button = browser.find_element(By.CSS_SELECTOR, '[class=\'btn btn-lg btn-primary btn-add-to-basket\']')
    except Exception as e:
        print(e.__doc__)
    else:
        # assert button.text == 'Añadir al carrito'
        assert button.text == 'Ajouter au panier'
