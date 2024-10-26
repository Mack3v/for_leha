import pytest

URL = 'https://www.saucedemo.com/'

class TestAuthorization:


    def test_positive_auth(self, page):
        page.goto(URL)
        assert page.title() == "Swag Labs"
        page.locator('[data-test="username"]').fill('standard_user')
        page.locator('[data-test="password"]').fill('secret_sauce')
        page.locator('[data-test="login-button"]').click()
        assert page.url == 'https://www.saucedemo.com/inventory.html', "Не ожидаемый url после успешной авторизации"
