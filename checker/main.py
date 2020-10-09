import kivy
kivy.require('1.11.1')

#apps
from app.components.checkerapp import CheckerApp

if __name__ == '__main__':
    CheckerApp().run()