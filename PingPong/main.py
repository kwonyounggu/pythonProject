# step 1 - create the app
# step 2 - create the game
# step 3 - build the game
# step 4 - run the app

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

PongApp().run()