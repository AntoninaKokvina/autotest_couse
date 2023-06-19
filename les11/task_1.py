# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

test_site = 'https://sbis.ru/'
driver = webdriver.Chrome()  # запуск браузера
try:
    driver.get(test_site)
    assert driver.current_url == test_site, 'Неверная ссылка'
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contacts.text == 'Контакты', 'Неверный текст ссылки "Контакты"'
    assert contacts.is_displayed(), 'Элемент "Контакты" не отображается'
    sleep(2)
    contacts.click()  # клик на Контакты
    banner_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    assert banner_tensor.is_displayed(), 'Элемент "баннер Тензор" не отображается'
    sleep(2)
    banner_tensor.click()  # клик на Тензор
    driver.switch_to.window(driver.window_handles[1]) #переходим на открывшуюся вкладку
    assert driver.current_url == 'https://tensor.ru/', 'Неверная ссылка'
    strenght = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content ' '.tensor_ru-Index__card-title')
    strenght.location_once_scrolled_into_view
    sleep(2)
    assert strenght.is_displayed(), 'Элемент "Сила в людях" не отображается'
    assert strenght.text == 'Сила в людях', 'Неверный заголовок новости'
    news_more = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__link[href="/about"]')
    news_more.location_once_scrolled_into_view
    assert news_more.is_displayed(), 'Элемент "Подробнее" не отображается'
    sleep(2)
    driver.execute_script("return arguments[0].scrollIntoView(true);", news_more)
    news_more.click()
    assert driver.current_url == 'https://tensor.ru/about'

finally:
    sleep(5)
    driver.quit()