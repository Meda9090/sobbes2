import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Тесты Facebook")
@allure.feature("Авторизация")
class TestFacebookLogin:

    @allure.story("Успешный вход")
    def test_facebook_login(self):
        # Инициализация веб-драйвера
        driver = webdriver.Chrome(service=Service("C:\\chromedriver\\chromedriver.exe"))
        driver.maximize_window()

        try:
            # Открытие страницы входа Facebook
            driver.get("https://www.facebook.com/")

            # Ввод email и пароля
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("87074596405")
            driver.find_element(By.NAME, "pass").send_keys("Ayana2021Aa" + Keys.RETURN)

            # Ожидание загрузки страницы после авторизации
            WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))

            # Проверка успешной авторизации
            assert "facebook.com" in driver.current_url, "Не удалось авторизоваться!"

        finally:
            # Закрытие браузера
            driver.quit()

if __name__ == "__main__":
    pytest.main()
