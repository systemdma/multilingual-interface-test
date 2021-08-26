import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        default=None,
        help="choose language")
    parser.addoption(
        "--browser",
        default="chrome",
        help="choose browser: chrome or firefox"
    )



@pytest.fixture
def browser(request):
    if request.config.getoption("--browser") == "chrome":
        browser = webdriver.Chrome()
    elif request.config.getoption("--browser") == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Uncorrect browser name")
    yield browser
    browser.quit()


@pytest.fixture
def get_choose_language(request):
    return request.config.getoption("--language")
    