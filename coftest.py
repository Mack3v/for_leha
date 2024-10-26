import pytest
from playwright.sync_api import sync_playwright


# Фикстура для запуска Playwright
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

# Фикстура для запуска браузера
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

# Фикстура для создания контекста браузера (для новых сессий)
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# Фикстура для страницы браузера, на которой будут проходить тесты
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
