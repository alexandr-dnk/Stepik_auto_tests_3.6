import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert button > 0, 'Кнопка отсутствует!'
