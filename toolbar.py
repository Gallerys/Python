from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (300, 500)

KV = '''
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: "vertical"
                    MDTopAppBar:
                        title: "MDToolbar"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        md_bg_color: app.theme_cls.accent_color
                        right_action_items: [["dots-vertical", lambda x: app.callback()]]
                        #right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["clock", lambda x: app.callback_2()]]
                        # specific_text_color: app.theme_cls.accent_color
                        elevation: 20
                    Widget:

        MDNavigationDrawer:
            in: nav_drawer

                    
#                     MDBottomAppBar:
#                         MDTopAppBar:
#                             icon: "git"
#                             type: "bottom"
#                             # left_action_items: [["menu", lambda x: x]]
#                             # on_action_button: app.callback(self.icon)
#                             # mode: "end"
#                             # mode: "free-end"
                        
#                     MDLabel:
#                         text: "Content"
#                         halign: "center"


'''
class Test(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        return Builder.load_string(KV)


Test().run()