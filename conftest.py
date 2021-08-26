import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        default=None,
        help="choose language")


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def get_choose_language(request):
    return request.config.getoption("--language")
    