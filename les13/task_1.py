'''
1. Переместить запись в другую папку и проверить перемещение
(убедиться в: наличии в папке и увеличении счётчика). И вернуть обратно.
2. Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах
3. Пометить сообщение эталонным тегом. Убедиться, что тег появился на сообщении, а счётчик тегов увеличился.
Снять тег и проверить.
'''

from atf.ui import *
from atf import *
from pages.auth_page import AuthSbis
from pages.contacts_page import ContactsPage


class TestTaskFolder(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthSbis(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.page = ContactsPage(cls.driver)

    def test_01_move_massage(self):
        '''Перемещение сообщения в другую папку и назад'''

        self.page = ContactsPage(self.driver)
        self.page.check_load()
        log('Перейти в Папку для автотеста, проверить, что пустая')
        self.page.folders.row(contains_text='Папка для автотеста').click()
        self.page.messages.check_size(0) # убедились что папка пустая
        delay(1)
        log('Вернуться во Все')
        self.page.folders.row(contains_text='Все сообщения').click()
        log('Переместить сообщение в Папку для автотеста, проверить')
        self.page.messages.item(contains_text='Диалог для автотеста').select_menu_actions('Переместить')
        delay(2)
        self.page.sel_folders.item(contains_text='Папка для автотеста').click()
        delay(2)
        self.page.folders.row(contains_text='Папка для автотеста').click()
        self.page.messages.check_size(1)
        self.page.messages.item(contains_text='Диалог для автотеста').should_be(Visible)
        delay(2)
        log('Переместить сообщение в папку Все')
        self.page.messages.item(contains_text='Диалог для автотеста').select_menu_actions('Переместить')
        self.page.sel_folders.item(contains_text='Все сообщения').click()
        self.page.messages.check_size(0)
        delay(2)
        self.page.folders.row(contains_text='Все сообщения').click()

    def test_02_compare_date(self):
        '''Сравнение дат в чатах и диалогах'''

        log('Проверить дату в чатах')
        self.page.select_tab('Чаты')
        self.page.chats.item(contains_text='Диалог для автотеста').should_be(ContainsText('21 июн 03:40'))
        delay(2)
        log('Проверить дату в диалогах')
        self.page.select_tab('Диалоги')
        self.page.messages.item(contains_text='Диалог для автотеста').should_be(ContainsText('21 июн 03:40'))
        delay(2)


    def test_03_tag(self):
        log('Пометить сообщение тегом для автотеста')
        delay(2)
        self.page.messages.item(contains_text='Диалог для автотеста').select_menu_actions('Пометить')
        delay(2)
        self.page.sel_tags.click()
        delay(3)
        log('Проверить тег на сообщении')
        self.page.messages.item(contains_text='Диалог для автотеста').should_be(ContainsText('Тег для автотеста'))
        log('Снять отметку сообщения')
        self.page.messages.item(contains_text='Диалог для автотеста').select_menu_actions('Пометить')
        delay(2)
        self.page.sel_tags.click()
        delay(2)





