from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello world',pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        btn_Icon = MDIconButton(icon= 'language-python',pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        btn_Icon = MDFloatingActionButton(icon= 'language-python',pos_hint = {'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_Icon)
        return screen


DemoApp().run()