from atf.ui import *
from controls import *
from selenium.webdriver import Keys

class ContactsPage(Region):
    '''Реестр Контакты'''

    messages = ControlsListView(By.CSS_SELECTOR, '.Hint-ListWrapper_list .controls-ListViewV', 'Диалоги')
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.msg-dialogs-folder__list', 'Папки')
    search = ControlsSearchInput()
    sel_folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MoveDialog__scroll', 'Диалог выбора папки')
    sel_tags = ControlsTreeGridView(By.CSS_SELECTOR, '.tags-list.msg-tags-aggregate__tags.tags-Tag__show-border', 'Диалог выбора тега')
    tabs = ControlsTabsButtons()
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceDetail__view-dialogs', 'Чаты')
    tags = ControlsListView(By.CSS_SELECTOR, '.tags-list__view', 'Теги')


    def check_load(self):
        '''Проверка загрузки реестра контактов'''
        self.folders.check_load()
        self.messages.check_load()

    def search_message(self, mes_text: str):
        '''Поиск сообщения в реестре по тексту'''
        self.search.search(mes_text)
        self.search.type_in(Keys.ENTER)
        self.messages.should_be(ContainsText(mes_text))

    def select_tab(self, tab_name: str):
        self.tabs.select(contains_text=tab_name)
