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
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()  # запуск браузера
driver.maximize_window()

test_site = 'https://fix-online.sbis.ru/auth/'
try:
    driver.get(test_site)
    assert driver.current_url == test_site, 'Неверная ссылка'
    sleep(2)

    # вводим логин, пароль
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]').send_keys('больничные', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]').send_keys('больничные123', Keys.ENTER)
    sleep(4)

    # переходим в Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    assert contacts.is_displayed(), 'Элемент Контакты не отображается'
    contacts.click()
    sleep(1)
    contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts.click()
    sleep(2)

    # создаем сообщение
    plus_message = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    assert plus_message.is_displayed(), 'Элемент Плюс не отображается'
    plus_message.click()
    sleep(2)

    # ищем получателя
    addressee = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content ' '.controls-InputBase__nativeField_hideCustomPlaceholder')
    addressee.click()
    addressee.send_keys('Тестовая12466 Вера')
    sleep(2)
    addressee = driver.find_element(By.CSS_SELECTOR, '[title="Тестовая12466 Вера"]')
    assert addressee.is_displayed(), 'Получатель не найден'
    addressee.click()
    sleep(2)

    # пишем и отправляем сообщение
    message_text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    assert message_text.is_displayed(), 'Не отображается поле ввода сообщения'
    message_text.click()
    message_text.send_keys('Привет, Олег =)')
    sleep(2)
    send_button = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    assert send_button.is_displayed(), 'Не отображается кнопка отправки'
    send_button.click()
    sleep(2)

    # проверяем, что сообщение пришло и открываем его
    incoming_mes = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert 'Привет, Олег =)' in incoming_mes.text, 'Сообщение не найдено в реестре'
    incoming_mes.click()
    sleep(2)

    # удаляем сообщение
    delete_button = driver.find_element(By.CSS_SELECTOR, '[title="Удалить"]')
    delete_button.click()
    sleep(2)
    incoming_mes = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item')
    assert not('Привет, Олег =)' in incoming_mes.text), 'Сообщение не удалено из реестра'


finally:
    sleep(5)
    driver.quit()