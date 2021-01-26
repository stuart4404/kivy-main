from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty

class GameScreen(Widget):
    
    def press_me(self):
        print("boom")




class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()