from atf.ui import *
from controls import *

class TaskPage(Region):
    '''Реестр Задачи'''

    tasks = ControlsTreeGridView(By.CSS_SELECTOR, '.brTasksOnMe .controls-Grid', 'Задачи в работе')
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_master .controls-Grid', 'Папки')
    search = ControlsSearchInput()

    def check_load(self):
        '''Проверка загрузки реестра задач'''
        self.folders.check_load()
        self.tasks.check_load()

    def search_task(self, task_text: str):
        '''Поиск задачи в реестре по тексту'''
        self.search.search(task_text, search_btn_click=True)
        self.tasks.row(contains_text=task_text).should_be(Displayed)