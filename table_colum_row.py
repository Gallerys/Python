from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemosApp(MDApp):
    def build(self):
        screen = Screen()
        tables = MDDataTable(pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                            size_hint = (0.9, 0.6),
                            check = True,
                            rows_num = 15,
                            column_data=[
                                ("No.",dp(30)),
                                ("Food",dp(30)),
                                ("Eat",dp(30)),
                                ("Wate",dp(30))
                                
                            ],
                            row_data=[
                                ("1", "Burger", "240", "151"),
                                ("2", "Juse", "140", "212"),
                                ("3", "Juse", "140", "212"),
                                ("4", "Juse", "140", "212"),
                                ("5", "Juse", "140", "212"),
                                ("6", "Juse", "140", "212"),
                                ("7", "Juse", "140", "212"),
                                ("8", "Juse", "140", "212"),
                                ("9", "Juse", "140", "212"),
                                ("10", "Juse", "140", "212"),
                                ("11", "Juse", "140", "212"),
                                ("12", "Juse", "140", "212")
                                ]
                                )
        tables.bind(on_check_press = self.check_press)
        tables.bind(on_row_press = self.row_press)
        screen.add_widget(tables)
        return screen
    
    def check_press(self, insitance_table, current_row):
        print(insitance_table, current_row)

    def row_press(self, insitance_table, insitance_row):
        print(insitance_table, insitance_row)

DemosApp().run()