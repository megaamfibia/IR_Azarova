import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def test_chrome():
    pytest.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    pytest.driver.get('https://b2c.passport.rt.ru/')
    WebDriverWait(pytest.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/body/div[@id='app']")))

    yield

    pytest.driver.quit()

# Раскомментировать строки для тестирования в Firefox
# @pytest.fixture(autouse=True)
# def test_firefox():
#     pytest.driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
#     pytest.driver.get('https://b2c.passport.rt.ru/')
#     WebDriverWait(pytest.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/body/div[@id='app']")))
#
#     yield
#
#     pytest.driver.quit()


# Не получилось настроить одновременное тестирование на двух браузерах
#
# @pytest.fixture(autouse=True, params=["firefox", "chrome"])
# def init_driver(request):
#     if request.param == "firefox":
#         firefox_options = webdriver.FirefoxOptions()
#         web_driver = webdriver.Firefox(options=firefox_options, executable_path='drivers/geckodriver.exe')
#         web_driver.get('https://b2c.passport.rt.ru/')
#         WebDriverWait(web_driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/body/div[@id='app']")))
#
#     if request.param == "chrome":
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-gpu")
#         web_driver = webdriver.Chrome(options=chrome_options, executable_path='drivers/chromedriver.exe')
#         web_driver.get('https://b2c.passport.rt.ru/')
#         WebDriverWait(web_driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/body/div[@id='app']")))
#
#     yield web_driver
#
#     web_driver.quit()

