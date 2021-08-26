import pytest
from selenium.webdriver.common.by import By


def test_exist_basket_button(browser, get_choose_language):
    lang = get_choose_language
    if lang is None:
        raise ValueError("Not set language")
    else:
        url = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
        browser.get(url)
        assert browser.find_element_by_class_name("btn-add-to-basket"), "basket button not found"
