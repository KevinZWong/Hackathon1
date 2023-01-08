from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel

from kivymd.uix.screen import Screen
from kivy.core.window import Window
Window.size = (1080, 1920)
class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        button1 = MDFillRoundFlatButton(
                    text="Get Started",
                    font_size =  '50sp',
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    size_hint = (.5, .15)
                )

        screen.add_widget(button1)

        return screen

MainApp().run()