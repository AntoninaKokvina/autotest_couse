# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()  # запуск браузера
test_site = 'https://fix-online.sbis.ru/auth/'
try:
    driver.get(test_site)
    assert driver.current_url == test_site, 'Неверная ссылка'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]').send_keys('оленьев')

finally:
    sleep(5)
    driver.quit()