from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from random import randint

Window.clearcolor = (1,1,1,1)
Window.size = (400,600)

class EndGameScreen(ModalView):
    pass
    

class Progressbar(Widget):
    pass


class ImageBox(Widget):
    index = NumericProperty(0)
    image_name = StringProperty("")
    
    def get_image_path(self,image_name):
        return "images/" + image_name + ".png"


class GameScreen(Widget):
    correct_answer_index = NumericProperty(0)
    display_image_names = ListProperty([
        "bote",
        "diamante",
        "espada",
        "hacha",
        ])

    correct_answer_text = StringProperty("bote")
    
    
    item_names = [
        "bote",
        "diamante",
        "espada",
        "hacha",
        "ladrillos",
        "manzana",
        "pala",
        "pasto",
        "roca",
        "tierra"
    ]


    def __init__(self,**kwargs):
        super(GameScreen,self).__init__(**kwargs)
        self.load_new_question()

        #starts program with load new question function
    

    def make_selection(self,index):
        if self.check_if_answer_correct(index):
            print("you got it!")
            self.show_answer_popup(True)
        else:
            print("wrongo")
            self.show_answer_popup(False)
        


    def check_if_answer_correct(self, index):
        if index == self.correct_answer_index:
            return True
        return False
    
    
    def get_random_image_names(self):
        temp_item_names = self.item_names.copy()
        items = []
        for _ in range(4):
            rand_index = randint(0,len(temp_item_names)-1)
            items.append(temp_item_names[rand_index])
            del temp_item_names[rand_index]
        return items

        #choose 4 random names into list items[]


    def load_new_question(self, *args):
        self.display_image_names = self.get_random_image_names()
        self.correct_answer_index = randint(0,3)
        self.correct_answer_text = self.display_image_names[self.correct_answer_index]    

    
    def show_end_game_popup(self):
        end_game_screen = EndGameScreen(
            size_hint= (.75,.6),
            auto_dismiss = False)
        end_game_screen.open()
        
    
    def show_answer_popup(self, is_correct):
        content= Image(source='images/' + self.correct_answer_text + '.png')
        
        popup = Popup(
            title ='correct' if is_correct else 'Wrong dummo',
            size_hint= (.5,.4),
            content= content,
            title_align = 'center',
            title_color=(0,0,0,1),
            background='images/white.png',
            auto_dismiss =  True
            )
        popup.bind(on_dismiss=self.load_new_question)
        popup.open()

    



class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()