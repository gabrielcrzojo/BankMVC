from bottle import template


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
        return template('app/views/html/home')


    def sobre(self):
        return template('app/views/html/sobre')


    def servicos(self):
        return template('app/views/html/servicos')


    def contato(self):
        return template('app/views/html/contato')


