from atf.ui import *
from atf import log

class AuthSbis(Region):
    '''Страница авторизации'''

    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'Пароль')

    def auth(self, user_login: str, user_password: str):
        '''Авторизация'''

        log(f'Авторизация на {self.config.get("SBIS_SITE")}')
        self.browser.open(self.config.get('SBIS_SITE'))
        self.login.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        self.password.type_in(user_password + Keys.ENTER).should_not_be(Visible)