from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)


        for i in range(10):
            icon = IconLeftWidget(icon='language-python')
            items = ThreeLineIconListItem(text='Item ' + str(i+1), secondary_text = 'Hello', tertiary_text = 'This is thread line')       
            list_view.add_widget(items)
    
            items.add_widget(icon)
        screen.add_widget(scroll)
        return screen

DemoApp().run()