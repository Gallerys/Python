from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class Page_Layout_Demo(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.button1 = Button(text="Page1")
        self.add_widget(self.button1)
        
        self.button2 = Button(text="Page2")
        self.add_widget(self.button2)
        
        self.button3 = Button(text="Page3")
        self.add_widget(self.button3)
        
class DemoApp(App):
    def build(self):
        return Page_Layout_Demo()
DemoApp().run()