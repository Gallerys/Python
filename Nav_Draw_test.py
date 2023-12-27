from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Window.size = (360, 640)

KV = '''
<ContentNavigationDrawer>:
    ScrollView:
    
                
        MDList:
            OneLineIconListItem:
                text: "Profile"
                IconLeftWidget:
                    icon: 'android'

            OneLineListItem:
                text: "Setting"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "setting"



Screen:
    MDTopAppBar:
        id: toolbar
        title: "Drawer"
        pos_hint: {"top": 1}
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    
    MDNavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager

            Screen:
                name: "profile"
                MDLabel:
                    text: "Profile"
                    halign: "center"
            Screen:
                name: "setting"
                MDLabel:
                    text: "Setting"
                    halign: "center"
                MDRectangleFlatButton:
                    text: 'Back'
                    pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                    #on_press: root.screen_manager.current = "back"

            Screen:
                name: "back"
                MDLabel:
                    text: "Back"
                    halign: "center"
            
                
        
        MDNavigationDrawer:
            id: nav_drawer
            orientation: 'vertical'

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'icon.png'

                MDLabel:
                    text: "Asad"
                    text_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "asad@gmail.com"
                    text_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

            



            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

            
                    
'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class DrawerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

DrawerApp().run()