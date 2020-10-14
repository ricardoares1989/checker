import kivy
kivy.require('1.11.1')
#apps
from app.components.checkerapp import CheckerApp

__version__ = "1.0.0"

if __name__ == '__main__':
    CheckerApp().run()