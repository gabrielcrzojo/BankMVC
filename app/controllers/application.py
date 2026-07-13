from bottle import template
from app.utils.auth import get_current_user

class Application():

    def __init__(self):
        self.pages = {
            'home': self.home,
            'sobre': self.sobre,
            'servicos': self.servicos,
            'contato': self.contato,
        }

    def render(self, page, **kwargs):
        content = self.pages.get(page, self.home)
        return content(**kwargs)

    def home(self):
        return template('app/views/html/home', user=get_current_user())

    def sobre(self):
        return template('app/views/html/sobre', user=get_current_user())

    def servicos(self):
        return template('app/views/html/servicos', user=get_current_user())

    def contato(self):
        return template('app/views/html/contato', user=get_current_user())


