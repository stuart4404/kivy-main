from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView

Window.clearcolor = (1,1,1,1)
Window.size = (400,600)

class EndGameScreen(ModalView):
    pass
    

class Progressbar(Widget):
    pass


class ImageBox(Widget):
    pass

class GameScreen(Widget):
    
    def show_end_game_popup(self):
        end_game_screen = EndGameScreen(size_hint= (.75,.6),auto_dismiss = False)
        end_game_screen.open()
        
    
    def show_answer_popup(self):
        content= Image(source='images/hacha.png')
        
        popup = Popup(
            title ='correct',
            size_hint= (.5,.4),
            content= content,
            title_align = 'center',
            title_color=(0,0,0,1),
            background='images/white.png',
            auto_dismiss =  True
            )
        popup.bind(on_dismiss=self.print_something)
        popup.open()

    def print_something(self,*args):
        print("popup dismissed")



class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()