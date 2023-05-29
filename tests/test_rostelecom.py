import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_email_password, valid_phone_password, valid_phone, valid_login, \
    valid_login_password, valid_ls, valid_ls_password


# Тест №1. Проверка наличия элементов страницы авторизации (Тест EXP-001)
def test_page_form():
    # Надпись-логотип Ростелеком в левом верхнем углу экрана
    pytest.driver.find_element(By.CSS_SELECTOR, 'header#app-header > div > div > svg')
    # Левая часть экрана с надписью Личный кабинет...
    pytest.driver.find_element(By.XPATH, '//*[@id="page-left"]')
    # Надпись Авторизация в правой части экрана
    pytest.driver.find_element(By.XPATH, '//html/body/div[@id="app"]')
    # Название вкладки Телефон
    pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-phone"]')
    # Название вкладки Почта
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']")
    # Название вкладки Логин
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-login']")
    # Название вкладки Лицевой счет
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-ls']")
    # Поле ввода логина
    pytest.driver.find_element(By.XPATH, "//input[@id='username']")
    # Поле ввода пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']")
    # Чекбокс Запомнить меня
    pytest.driver.find_element(By.XPATH, "//span[@class='rt-checkbox__label-desc']")
    # Название чекбокса Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']")
    # Кнопка Забыл пароль
    pytest.driver.find_element(By.XPATH, "//a[@id='forgot_password']")
    # Кнопка Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']")
    # Ссылка на пользовательское соглашение
    pytest.driver.find_element(By.XPATH, "//div[@class='card-container__content']")
    # Кнопка Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//a[@id='kc-register']")
    # Заголовок "или войдите с помощью соцсетей"
    pytest.driver.find_element(By.XPATH, "//div[@class='social-providers-container__desc']/span[2]")
    # Кнопка авторизации через сайт VK
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_vk']")
    # Кнопка авторизации через сайт OK
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ok']")
    # Кнопка авторизации через сайт mail
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_mail']")
    # Кнопка авторизации через сайт google
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_google']")
    # Кнопка авторизации через сайт yandex
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ya']")
    pytest.driver.save_screenshot('media/1.test_page_form.png')


# Тест №2. Авторизация по номеру телефона (Тест EXP-002)
def test_auth_by_phone():
    # Ввод номера телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_phone)
    # Ввод пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_phone_password)
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия заголовка Учетные данные
    assert WebDriverWait(pytest.driver, 20).\
        until(EC.presence_of_element_located((By.XPATH, "//h3[@class='card-title'][1]")))
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/2.test_auth_by_phone.png')
    # Нажать на кнопку Выйти
    pytest.driver.find_element(By.XPATH, "//div[@id='logout-btn']").click()


# Тест №3. Авторизация по email (Тест EXP-005)
def test_auth_by_email():
    # Переход на вкладку Почта
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    # Ввод email
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_email)
    # Ввод пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_email_password)
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия заголовка Учетные данные
    assert WebDriverWait(pytest.driver, 20). \
        until(EC.presence_of_element_located((By.XPATH, "//h3[@class='card-title'][1]")))
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/3.test_auth_by_email.png')
    # Нажать на кнопку Выйти
    pytest.driver.find_element(By.XPATH, "//div[@id='logout-btn']").click()


# Тест №4. Авторизация по логину (Тест EXP-008)
def test_auth_by_login():
    # Переход на вкладку Логин
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-login']").click()
    # Ввод логина
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_login)
    # Ввод пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_login_password)
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия заголовка Учетные данные
    assert WebDriverWait(pytest.driver, 20). \
        until(EC.presence_of_element_located((By.XPATH, "//h3[@class='card-title'][1]")))
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/4.test_auth_by_login.png')
    # Нажать на кнопку Выйти
    pytest.driver.find_element(By.XPATH, "//div[@id='logout-btn']").click()


# Тест №5. Авторизация по номеру лицевого счета (Тест EXP-011)
def test_auth_by_ls():
    # Переход на вкладку Лицевой счет
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-ls']").click()
    # Ввод номера лицевого счета
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_ls)
    # Ввод пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_ls_password)
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия заголовка Учетные данные
    assert WebDriverWait(pytest.driver, 20). \
        until(EC.presence_of_element_located((By.XPATH, "//h3[@class='card-title'][1]")))
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/5.test_auth_by_ls.png')
    # Нажать на кнопку Выйти
    pytest.driver.find_element(By.XPATH, "//div[@id='logout-btn']").click()


# Тест №6. Некорректная связка номер телефона/пароль (Тест EXP-004)
def test_auth_by_phone_incorrect():
    # Ввести номер телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys('1234567891')
    # Ввести некорректный пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия сообщения о некорректном логине/пароле
    assert pytest.driver.find_element(By.XPATH, "//span[@id='form-error-message']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/6.test_auth_by_phone_incorrect.png')


# Тест №7. Некорректная связка email/пароль (Тест EXP-007)
def test_auth_by_email_incorrect():
    # Перейти на вкладку Почта
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']").click()
    # Ввести email
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_email)
    # Ввести некорректный пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия сообщения о некорректном логине/пароле
    assert pytest.driver.find_element(By.XPATH, "//span[@id='form-error-message']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/7.test_auth_by_email_incorrect.png')


# Тест №8. Некорректная связка логин/пароль (Тест EXP-010)
def test_auth_by_login_incorrect():
    # Перейти на вкладку Логин
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-login']").click()
    # Ввести логин
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_login)
    # Ввести некорректный пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия сообщения о некорректном логине/пароле
    assert pytest.driver.find_element(By.XPATH, "//span[@id='form-error-message']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/8.test_auth_by_login_incorrect.png')


# Тест №9. Некорректная связка номер лицевого счета/пароль (Тест EXP-013)
def test_auth_by_ls_incorrect():
    # Перейти на вкладку Лицевой счет
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-ls']").click()
    # Ввести номер лицевого счета
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_ls)
    # Ввести некорректный пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
    # Нажать на галочку Запомнить меня
    pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
    # Нажать на кнопку Войти
    pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
    # Проверка наличия сообщения о некорректном логине/пароле
    assert pytest.driver.find_element(By.XPATH, "//span[@id='form-error-message']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/9.test_auth_by_ls_incorrect.png')


# Тест №10. Появление капчи (Тест EXP-014)
def test_show_captha():
    i = 0
    # Трижды повторить следующий цикл: ввод логина, ввод пароля, нажать на галочку Запомнить меня,
    # нажать на кнопку Войти
    while i < 3:
        pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys('1234567891')
        pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
        pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
        pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
        i += 1
    # Проверка наличия капчи на странице
    assert pytest.driver.find_element(By.XPATH, "//div[@class='rt-captcha__left']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/10.test_show_captha.png')


# Тест №11. Некорректный ввод капчи (Тест EXP-016)
def test_captha_incorrect():
    i = 0
    # Трижды повторить следующий цикл: ввод логина, ввод пароля, нажать на галочку Запомнить меня,
    # нажать на кнопку Войти
    while i < 3:
        pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys('1234567891')
        pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys('12345678')
        pytest.driver.find_element(By.XPATH, "//main[@id='app-container']").click()
        pytest.driver.find_element(By.XPATH, "//button[@id='kc-login']").click()
        i += 1
    # Ввести корректный номер телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(valid_phone)
    # Ввести корректный пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_phone_password)
    # Ввести в поле капчи gggggggg
    pytest.driver.find_element(By.XPATH, "//input[@id='captcha']").send_keys('gggggggg')
    # Проверить наличие появления сообщения о неправильном вводе символов с картинки
    pytest.driver.find_element(By.XPATH, "//span[@id='form-error-message']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/11.test_captha_incorrect.png')


# Тест №12. Показ пользовательского соглашения (Тест EXP-022)
def test_show_agreement():
    # Нажать на кнопку "пользовательское соглашение"
    pytest.driver.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange']").click()
    # Определяем, что нужно переключить фокус на открывшееся окно. Создаем переменную с ID созданного окна
    window_after = pytest.driver.window_handles[2]
    # Передаем эту переменную драйверу
    pytest.driver.switch_to.window(window_after)
    # Проверяется элемент, присутствующий на странице с соглашением
    assert WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="title"]/h1[1]')))
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/12.test_show_agreement.png')


# Тест №13. Авторизация через сайт VK (Тест EXP-031)
def test_auth_by_vk():
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_vk']").click()
    WebDriverWait(pytest.driver, 20)
    assert pytest.driver.find_element(By.XPATH, "//div[@class='oauth_wrap_inner']")
    pytest.driver.save_screenshot('media/13.test_auth_by_vk.png')


# Тест №14. Авторизация через сайт OK (Тест EXP-032)
def test_auth_by_ok():
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ok']").click()
    assert pytest.driver.find_element(By.XPATH, "//*[@id='widget-el']/div[1]/div[1]")
    pytest.driver.save_screenshot('media/14.test_auth_by_ok.png')


# Тест №15. Авторизация через сайт mail (Тест EXP-033)
def test_auth_by_mail():
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_mail']").click()
    assert pytest.driver.find_element(By.XPATH, "//*[@id='wrp']/div[1]/span[1]")
    pytest.driver.save_screenshot('media/15.test_auth_by_mail.png')


# Тест №16. Авторизация через сайт google (Тест EXP-034)
def test_auth_by_google():
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_google']").click()
    assert pytest.driver.find_element(By.XPATH, "//div[@class='BHzsHc']']")
    pytest.driver.save_screenshot('media/16.test_auth_by_google.png')


# Тест №17. Авторизация через сайт yandex (Тест EXP-035)
def test_auth_by_ya():
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ya']").click()
    assert pytest.driver.find_element(By.XPATH, "//div[@class='passp-auth-content']")
    pytest.driver.save_screenshot('media/17.test_auth_by_ya.png')


# Тест №18. Форма регистрации (Тест EXP-026)
def test_registration_form():
    pytest.driver.find_element(By.XPATH, "//a[@id='kc-register']").click()
    # Заголовок Регистрация
    pytest.driver.find_element(By.XPATH, "//h1[@class='card-container__title']")
    # Заголовок Личные данные
    pytest.driver.find_element(By.XPATH, "//p[@class='register-form__desc'][1]")
    # Поле ввода текста Имя
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
    # Поле ввода текста Фамилия
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    # Поле выбора города
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]").\
        click()
    # Создание скриншота для подтверждения появления выпадающего списка с городами
    pytest.driver.save_screenshot('media/18.registration_form.list_of_cities.png')
    # Выпадающий список городов
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-select__list-wrapper rt-select__list-wrapper--rounded']")
    # Заголовок Данные для входа
    pytest.driver.find_element(By.XPATH, "//p[@class='register-form__desc'][2]")
    # Поле ввода email или номера телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='address']")
    # Поле ввода пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password']")
    # Поле ввода подтверждения пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password-confirm']")
    # Кнопка Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "register-form__reg-btn']")
    # Текст Нажимая кнопку «Зарегистрироваться», вы принимаете условия пользовательского соглашения
    pytest.driver.find_element(By.XPATH, "//div[@class='auth-policy']/span")
    # Ссылка на пользовательское соглашение
    pytest.driver.find_element(By.XPATH, "//a[@class='rt-link rt-link--orange']")
    # Сохранить скриншот
    pytest.driver.save_screenshot('media/18.test_registration_form.png')


# Тест №19. Показ сообщения о существующей учетной записи (Тест EXP-028)
def test_registration_message():
    # Нажать на кнопку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//a[@id='kc-register']").click()
    # Ввести текст в поле Имя
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]").\
        send_keys('Тест')
    # Ввести текст в поле Фамилия
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]").\
        send_keys('Тест')
    # Ввести номер телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='address']").send_keys('+71111111111')
    # Ввести пароль
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_phone_password)
    # Ввести подтверждение пароля
    pytest.driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys(valid_phone_password)
    # Нажать на кнопку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "register-form__reg-btn']").click()
    # Сообщение
    pytest.driver.find_element(By.XPATH, "//div[@class='card-modal__card']")
    # Заголовок сообщения Учетная запись уже существует
    pytest.driver.find_element(By.XPATH, "//h2[@class='card-modal__title']")
    # Надпись Попробуйте войти в неё. Если вы хотите создать новую учётную запись с данным номером,
    # то нажмите «Зарегистрироваться»
    pytest.driver.find_element(By.XPATH, "//div[@class='card-modal__card']/div[@class='card-modal__desc']")
    # Кнопка Войти
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded']")
    # Кнопка Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "rt-btn--transparent']")
    # Сделать скриншот сообщения
    pytest.driver.save_screenshot('media/19.test_registration_message.png')


# Тест №20. В сообщении о существующей учетной записи нажать Войти (Тест EXP-028)
def test_reg_1():
    pytest.driver.find_element(By.XPATH, "//a[@id='kc-register']").click()
    pytest.driver.find_element(By.XPATH,
                               "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]").\
        send_keys('Тест')
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]"
                                         "/input[1]").send_keys('Тест')
    pytest.driver.find_element(By.XPATH, "//input[@id='address']").send_keys('+71111111111')
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_phone_password)
    pytest.driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys(valid_phone_password)
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "register-form__reg-btn']").click()
    # Сообщение
    pytest.driver.find_element(By.XPATH, "//div[@class='card-modal__card']")
    # Заголовок сообщения Учетная запись уже существует
    pytest.driver.find_element(By.XPATH, "//h2[@class='card-modal__title']")
    # Надпись Попробуйте войти в неё. Если вы хотите создать новую учётную запись с данным номером,
    # то нажмите «Зарегистрироваться»
    pytest.driver.find_element(By.XPATH,
                               "//div[@class='card-modal__card']/div[@class='card-modal__desc']")
    # Кнопка Войти
    pytest.driver.find_element(By.XPATH,
                               "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded']")
    # Кнопка Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "rt-btn--transparent']")
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium "
                                         "rt-btn--rounded']").click()
    assert pytest.driver.find_element(By.XPATH, '//html/body/div[@id="app"]')
    pytest.driver.save_screenshot('media/20.test_reg_1.png')


# Тест №21. В сообщении о существующей учетной записи нажать Зарегистрироваться (Тест EXP-028)
def test_reg_2():
    pytest.driver.find_element(By.XPATH, "//a[@id='kc-register']").click()
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]"
                                         "/input[1]").send_keys('Тест')
    pytest.driver.find_element(By.XPATH, "//*[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]"
                                         "/input[1]").send_keys('Тест')
    pytest.driver.find_element(By.XPATH, "//input[@id='address']").send_keys('+71111111111')
    pytest.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(valid_phone_password)
    pytest.driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys(valid_phone_password)
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "register-form__reg-btn']").click()
    # Сообщение
    pytest.driver.find_element(By.XPATH, "//div[@class='card-modal__card']")
    # Заголовок сообщения Учетная запись уже существует
    pytest.driver.find_element(By.XPATH, "//h2[@class='card-modal__title']")
    # Надпись Попробуйте войти в неё. Если вы хотите создать новую учётную запись с данным номером,
    # то нажмите «Зарегистрироваться»
    pytest.driver.find_element(By.XPATH, "//div[@class='card-modal__card']/div[@class='card-modal__desc']")
    # Кнопка Войти
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded']")
    # Кнопка Зарегистрироваться
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "rt-btn--transparent']")
    pytest.driver.find_element(By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded "
                                         "rt-btn--transparent']").click()
    # Окно подтверждения номера телефона
    pytest.driver.find_element(By.XPATH, "//div[@class='card-container__wrapper']")
    # Заголовок Подтверждение телефона
    pytest.driver.find_element(By.XPATH, "//h1[@class='card-container__title']")
    pytest.driver.save_screenshot('media/21.test_reg_2.png')


# Тест №22. Форма восстановления пароля (Тест EXP-023)
def test_forgot_password_form():
    pytest.driver.find_element(By.XPATH, "//a[@id='forgot_password']").click()
    # Заголовок Восстановление пароля
    pytest.driver.find_element(By.XPATH, "//h1[@class='card-container__title']")
    # Надпись Введите данные и нажмите «Продолжить»
    pytest.driver.find_element(By.XPATH, "//p[@class='card-container__desc']")
    # Вкладка Телефон
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-phone']")
    # Вкладка Почта
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-mail']")
    # Вкладка Логин
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-login']")
    # Вкладка Лицевой счет
    pytest.driver.find_element(By.XPATH, "//div[@id='t-btn-tab-ls']")
    # Поле ввода текста
    pytest.driver.find_element(By.XPATH, "//input[@id='username']")
    # Капча
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-captcha__left']")
    # Поле ввода капчи
    pytest.driver.find_element(By.XPATH, "//input[@id='captcha']")
    # Кнопка Продолжить
    pytest.driver.find_element(By.XPATH, "//button[@id='reset']")
    # Кнопка Вернуться назад
    pytest.driver.find_element(By.XPATH, "//button[@id='reset-back']")
    pytest.driver.save_screenshot('media/22.test_forgot_password_form.png')


# Тест №23. Форма авторизации по коду на email (Тест EXP-037)
def test_auth_by_code_form():
    pytest.driver.get('https://lk.rt.ru/')
    WebDriverWait(pytest.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[@class='card-container__title']")))
    # Текст "Укажите почту или номер телефона, на которые необходимо отправить код подтверждения
    pytest.driver.find_element(By.XPATH, "//p[@class='card-container__desc']")
    # Поле ввода email или номера телефона
    pytest.driver.find_element(By.XPATH, "//input[@id='address']")
    # Кнопка Получить код
    pytest.driver.find_element(By.XPATH, "//button[@id='otp_get_code']")
    # Кнопка Войти с паролем
    pytest.driver.find_element(By.XPATH, "//button[@id='standard_auth_btn']")
    # Заголовок "или войдите с помощью соцсетей"
    pytest.driver.find_element(By.XPATH, "//div[@class='social-providers-container__desc']/span[2]")
    # Кнопка авторизации через сайт VK
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_vk']")
    # Кнопка авторизации через сайт OK
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ok']")
    # Кнопка авторизации через сайт mail
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_mail']")
    # # Кнопка авторизации через сайт google
    # pytest.driver.find_element(By.XPATH, "//a[@id='oidc_google']")
    # Кнопка авторизации через сайт yandex
    pytest.driver.find_element(By.XPATH, "//a[@id='oidc_ya']")


# Тест №24. Авторизация по коду в электронной почте (Тест EXP-038)
def test_auth_by_code_in_email():
    pytest.driver.get('https://lk.rt.ru/')
    WebDriverWait(pytest.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[@class='card-container__title']")))
    pytest.driver.find_element(By.XPATH, "//input[@id='address']").send_keys(valid_email)
    pytest.driver.find_element(By.XPATH, "//button[@id='otp_get_code']").click()
    WebDriverWait(pytest.driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[@class='rt-link rt-link--orange otp-code-form__back-btn']")))
    pytest.driver.save_screenshot('media/24.test_auth_by_code_in_mail.png')


# Тест №25. Авторизация по коду в SMS (Тест EXP-039)
def test_auth_by_code_in_sms():
    pytest.driver.get('https://lk.rt.ru/')
    WebDriverWait(pytest.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[@class='card-container__title']")))
    pytest.driver.find_element(By.XPATH, "//input[@id='address']").send_keys(valid_phone)
    pytest.driver.find_element(By.XPATH, "//button[@id='otp_get_code']").click()
    WebDriverWait(pytest.driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[@class='rt-link rt-link--orange otp-code-form__back-btn']")))
    pytest.driver.save_screenshot('media/24.test_auth_by_code_in_sms.png')